// Local artifact QA through Chromium's debugging pipe; no browser profile or npm dependencies.
import assert from 'node:assert/strict';
import {spawn} from 'node:child_process';
import {readFile, writeFile, mkdir, mkdtemp, rm} from 'node:fs/promises';
import {resolve, sep} from 'node:path';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {StringDecoder} from 'node:string_decoder';

const executable = process.argv[2];
assert(executable, 'Pass the installed Chromium browser executable');
const qa = resolve('.verification');
await mkdir(qa, {recursive: true});
const profile = await mkdtemp(resolve(qa, 'browser-'));
assert(profile.startsWith(qa + sep));
const browser = spawn(executable, [
  '--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
  '--disable-background-networking', '--disable-component-update',
  '--remote-debugging-pipe', '--user-data-dir=' + profile,
], {stdio: ['ignore', 'ignore', 'pipe', 'pipe', 'pipe'], windowsHide: true});
let identifier = 0, buffered = '', diagnostics = '';
const pending = new Map(), errors = [], decoder = new StringDecoder('utf8');
browser.stderr.on('data', chunk => {diagnostics = (diagnostics + chunk).slice(-2000);});
browser.on('error', error => {for (const entry of pending.values()) entry.reject(error);});
browser.stdio[4].on('data', chunk => {
  buffered += decoder.write(chunk);
  let boundary;
  while ((boundary = buffered.indexOf('\0')) !== -1) {
    const message = JSON.parse(buffered.slice(0, boundary));
    buffered = buffered.slice(boundary + 1);
    if (message.method === 'Runtime.exceptionThrown') errors.push(message.params.exceptionDetails.text);
    const entry = pending.get(message.id);
    if (!entry) continue;
    clearTimeout(entry.timer); pending.delete(message.id);
    if (message.error) entry.reject(new Error(JSON.stringify(message.error)));
    else entry.resolve(message.result);
  }
});
function call(method, params = {}, sessionId) {
  return new Promise((resolveCall, reject) => {
    const id = ++identifier;
    const timer = setTimeout(() => {pending.delete(id);reject(new Error(method + ' timed out: ' + diagnostics));}, 15000);
    pending.set(id, {resolve: resolveCall, reject, timer});
    browser.stdio[3].write(JSON.stringify({id, method, params, ...(sessionId ? {sessionId} : {})}) + '\0');
  });
}
let session;
async function evaluate(expression) {
  const response = await call('Runtime.evaluate', {expression, returnByValue: true, awaitPromise: true}, session);
  assert(!response.exceptionDetails, JSON.stringify(response.exceptionDetails));
  return response.result.value;
}
async function screenshot(name) {
  const image = await call('Page.captureScreenshot', {format: 'png'}, session);
  await writeFile(resolve(qa, name), Buffer.from(image.data, 'base64'));
}
const results = {};
try {
  const target = await call('Target.createTarget', {url: 'about:blank'});
  session = (await call('Target.attachToTarget', {targetId: target.targetId, flatten: true})).sessionId;
  await call('Page.enable', {}, session);
  await call('Runtime.enable', {}, session);
  await call('Emulation.setDeviceMetricsOverride', {width: 1365, height: 1000, deviceScaleFactor: 1, mobile: false}, session);
  await call('Page.navigate', {url: pathToFileURL(resolve('knowledge-cards/docs.streamlit.io/index.html')).href}, session);
  await evaluate('new Promise(resolve => {if(document.readyState === "complete") resolve(true); else window.addEventListener("load", () => resolve(true), {once:true});})');
  const collection = JSON.parse(await readFile('knowledge-cards/docs.streamlit.io/collection.json', 'utf8'));
  const completed = collection.pages.filter(p => p.status === 'done');
  const documentText = () => evaluate('Array.from(document.querySelectorAll("[data-block-id]")).map(b => b.textContent)');
  assert.equal(completed.length,6);
  assert.equal(await evaluate('document.querySelector("#d2c-document h1").textContent.trim()'),'Streamlit 文档');
  assert.equal(await evaluate('document.documentElement.scrollWidth <= innerWidth'),true);
  assert.equal(await evaluate('performance.getEntriesByType("resource").some(r => /^https?:/.test(r.name))'),false);
  await screenshot('desktop-full.png');
  results.desktop={pages:completed.length,homepage:true,noRemoteAssets:true};

  const before = await documentText();
  await evaluate('document.getElementById("d2c-show-cards").click()');
  assert.equal(await evaluate('Array.from(document.querySelectorAll("[data-ai-explanation]")).every(c => getComputedStyle(c).display === "none")'),true);
  assert.deepEqual(await documentText(),before);
  await evaluate('document.getElementById("d2c-show-cards").click()');
  results.supplementalToggle=true;

  async function search(value){
    await evaluate('document.getElementById("d2c-search").value='+JSON.stringify(value)+';document.getElementById("d2c-search").dispatchEvent(new Event("input"))');
    return evaluate('document.querySelectorAll(".d2c-page-link:not([hidden])").length');
  }
  assert((await search('st.button'))>0);
  assert.equal(await search('no-match-123456'),0);
  assert.equal(await evaluate('document.getElementById("d2c-no-results").hidden'),false);
  assert.deepEqual(await documentText(),before);
  await search('');
  results.searchDoesNotHideBody=true;

  await call('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true},session);
  await evaluate('new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)))');
  assert.equal(await evaluate('document.getElementById("d2c-toc").open'),false);
  assert.equal(await evaluate('document.documentElement.scrollWidth <= innerWidth'),true);
  await screenshot('mobile-full.png');
  results.mobile={width:390,collapsedDirectory:true};

  results.documents=[];
  for(const page of completed){
    const name=page.url.replace(/\/$/,'')===collection.root_url.replace(/\/$/,'')?'index.html':'page-'+createHash('sha256').update(page.url).digest('hex').slice(0,12)+'.html';
    await call('Emulation.setDeviceMetricsOverride',{width:1365,height:1000,deviceScaleFactor:1,mobile:false},session);
    await call('Page.navigate',{url:pathToFileURL(resolve('knowledge-cards/docs.streamlit.io',name)).href},session);
    await evaluate('new Promise(resolve => {if(document.readyState === "complete") resolve(true);else window.addEventListener("load",()=>resolve(true),{once:true})})');
    assert.deepEqual(await evaluate('Array.from(document.querySelectorAll("[data-block-id]")).map(b=>b.dataset.blockId)'),page.source_blocks.map(b=>b.id),page.title);
    const sourceHtml=page.source_blocks.map(b=>b.html).join('');
    const expectedCode=await evaluate('Array.from(new DOMParser().parseFromString('+JSON.stringify(sourceHtml)+',"text/html").querySelectorAll("pre")).map(p=>p.textContent)');
    const actualCode=await evaluate('Array.from(document.querySelectorAll("#d2c-document pre")).filter(p=>!p.closest("[data-ai-explanation]")).map(p=>p.textContent)');
    assert.deepEqual(actualCode,expectedCode,'Official code changed: '+page.title);
    assert.equal(await evaluate('Array.from(document.querySelectorAll("#d2c-document img")).every(i=>i.complete&&i.naturalWidth>0)'),true,page.title+' image failed');
    assert.equal(await evaluate('document.documentElement.scrollWidth <= innerWidth'),true,page.title+' desktop overflow');
    if(page.title==='通过命令行安装')await screenshot('installation-full.png');
    await call('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true},session);
    await evaluate('new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)))');
    assert.equal(await evaluate('document.documentElement.scrollWidth <= innerWidth'),true,page.title+' mobile overflow');
    results.documents.push({title:page.title,blocks:page.blocks.length,officialCodeBlocks:actualCode.length});
  }
  const python = JSON.parse(await readFile('knowledge-cards/docs.python.org-3-tutorial/collection.json', 'utf8'));
  const pythonPage = python.pages.find(p => p.status === 'done');
  await call('Page.navigate',{url:pathToFileURL(resolve('knowledge-cards/docs.python.org-3-tutorial/index.html')).href},session);
  await evaluate('new Promise(resolve => {if(document.readyState === "complete") resolve(true);else window.addEventListener("load",()=>resolve(true),{once:true})})');
  assert.deepEqual(await evaluate('Array.from(document.querySelectorAll("[data-block-id]")).map(b=>b.dataset.blockId)'),pythonPage.source_blocks.map(b=>b.id));
  const pythonSource = pythonPage.source_blocks.map(b=>b.html).join('');
  const pythonCode = await evaluate('Array.from(new DOMParser().parseFromString('+JSON.stringify(pythonSource)+',"text/html").querySelectorAll("pre")).map(p=>p.textContent)');
  assert.deepEqual(await evaluate('Array.from(document.querySelectorAll("#d2c-document pre")).filter(p=>!p.closest("[data-ai-explanation]")).map(p=>p.textContent)'),pythonCode);
  assert.equal(await evaluate('document.documentElement.scrollWidth <= innerWidth'),true,'Python mobile overflow');
  results.python={blocks:pythonPage.blocks.length,officialCodeBlocks:pythonCode.length};
  assert.deepEqual(errors,[]);
  results.runtimeErrors=errors;
  await writeFile(resolve(qa,'viewer-checks-full.json'),JSON.stringify(results,null,2));
  console.log(JSON.stringify(results));
} finally {
  for (const entry of pending.values()) clearTimeout(entry.timer);
  await call('Browser.close').catch(() => browser.kill());
  await new Promise(resolveExit => {if(browser.exitCode !== null) resolveExit();else {browser.once('exit',resolveExit);setTimeout(() => {browser.kill();resolveExit();},2000);}});
  await rm(profile, {recursive: true, force: true, maxRetries: 3, retryDelay: 200});
}
