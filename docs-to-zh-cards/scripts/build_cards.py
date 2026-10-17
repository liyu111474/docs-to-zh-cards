"""Build a local reading page and Markdown from a knowledge-card collection."""

import argparse
from collections import Counter
from datetime import datetime
from html import escape
import json
from pathlib import Path
import re
from string import Template
import sys
import shutil
from hashlib import sha256
from document_html import Fragment, html as document_html, markdown as html_md, plain, verify_translation, elements
from urllib.parse import urlsplit, urlunsplit, urljoin, urldefrag


ASSETS = Path(__file__).resolve().parents[1] / "assets"
STATUS = {"done": "已翻译", "pending": "待翻译", "failed": "读取失败"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value):
    require(isinstance(value, str) and bool(value.strip()), "Expected nonempty text")


def url(value):
    text(value)
    parsed = urlsplit(value)
    require(parsed.scheme in ("http", "https") and bool(parsed.netloc)
            and not parsed.username and not parsed.password
            and not re.search(r'[\s<>"\\\x00-\x1f]', value), "Expected a public HTTP(S) URL")
    return parsed


def validate(data):
    require(isinstance(data, dict) and data.get("schema_version") == 2, "Expected schema_version 2; legacy summaries must be translated fully")
    text(data.get("title"))
    root = url(data.get("root_url"))
    catalog = data.get("catalog")
    require(isinstance(catalog, dict), "Missing catalog")
    text(catalog.get("coverage"))
    require(isinstance(catalog.get("sources"), list) and bool(catalog["sources"]), "Missing catalog sources")
    for source in catalog["sources"]:
        url(source)
    require(isinstance(data.get("glossary", {}), dict), "Expected a glossary object")
    for en, zh in data.get("glossary", {}).items():
        text(en)
        text(zh)
    pages = data.get("pages")
    require(isinstance(pages, list) and bool(pages), "Missing document pages")
    ids, urls = set(), set()
    for page in pages:
        require(isinstance(page, dict), "Expected a page object")
        for field in ("id", "title", "section", "status"):
            text(page.get(field))
        require(bool(re.fullmatch(r"[a-z0-9][a-z0-9-]*", page["id"])), "Invalid page id")
        address = url(page.get("url"))
        path = root.path.rstrip("/")
        require(address.netloc.lower() == root.netloc.lower() and address.scheme == root.scheme
                and (address.path.rstrip("/") == path or address.path.startswith(path + "/")),
                "Page URL is outside the document scope")
        canonical = urlunsplit(address._replace(fragment="")).rstrip("/")
        require(page["id"] not in ids and canonical not in urls, "Duplicate page id or URL")
        ids.add(page["id"])
        urls.add(canonical)
        require(page["status"] in STATUS, "Unknown page status")
        cards = page.get("cards", [])
        require(isinstance(cards, list), "Expected a cards list")
        if page["status"] == "done":
            text(page.get("read_at"))
            require(datetime.fromisoformat(page["read_at"]).tzinfo is not None, "read_at needs a timezone")
            require(isinstance(page.get("source_blocks"), list) and bool(page["source_blocks"]), "Missing complete source")
            require(isinstance(page.get("blocks"), list) and bool(page["blocks"]), "Missing complete translation")
            for block in page["source_blocks"] + page["blocks"]:
                require(isinstance(block, dict), "Expected document block")
                text(block.get("id"))
                text(block.get("html"))
                Fragment(block["html"])
            source_ids = [b["id"] for b in page["source_blocks"]]
            require(len(source_ids) == len(set(source_ids)), "Duplicate source block id")
            require(source_ids == [b["id"] for b in page["blocks"]], "Translation must preserve every source block in order")
            for original, translated in zip(page["source_blocks"], page["blocks"]):
                verify_translation(original["html"], translated["html"])
        else:
            require(not cards and not page.get("read_at") and not page.get("blocks"), "Unread pages cannot contain completed cards")
        if page["status"] == "failed":
            text(page.get("error"))
        if page.get("version") is not None:
            text(page["version"])
        card_ids = set()
        anchors = set()
        block_ids = {b["id"] for b in page.get("blocks", [])}
        for card in cards:
            require(isinstance(card, dict), "Expected a card object")
            for field in ("id", "title", "summary", "when_to_use"):
                text(card.get(field))
            require(bool(re.fullmatch(r"[a-z0-9][a-z0-9-]*", card["id"])) and card["id"] not in card_ids,
                    "Invalid or duplicate card id")
            card_ids.add(card["id"])
            require(card.get("after") in block_ids and card["after"] not in anchors, "Explanations need unique existing anchors")
            anchors.add(card["after"])
            for reference in card.get("references", []):
                url(reference)
            require(isinstance(card.get("steps"), list) and bool(card["steps"]), "Missing how-to steps")
            require(isinstance(card.get("notes", []), list), "Expected notes list")
            for item in card["steps"] + card.get("notes", []):
                text(item)
            if "example" in card:
                example = card["example"]
                require(isinstance(example, dict), "Expected an example object")
                text(example.get("code"))
                require(isinstance(example.get("language"), str) and bool(re.fullmatch(r"[a-zA-Z0-9#+.-]+", example["language"])), "Invalid code language")
                require(example.get("origin") in ("official", "ai"), "Example origin must be official or ai")
                require(isinstance(example.get("tested"), bool), "Example needs a tested boolean")
                if example["tested"]:
                    text(example.get("test_evidence"))


def md(text):
    text = escape(text, quote=False)
    return re.sub(r"([\\`*_[\]#])", r"\\\1", text)


def fence(code, language):
    size = max([2] + [len(run) for run in re.findall(r"`+", code)]) + 1
    marker = "`" * size
    return f"{marker}{language}\n{code}\n{marker}"



def filename(page, data):
    return "index.html" if page["url"].rstrip("/") == data["root_url"].rstrip("/") else "page-" + sha256(page["url"].encode()).hexdigest()[:12] + ".html"


def explanation(card):
    pieces = ['<aside class="d2c-card" data-ai-explanation><div class="d2c-card-label">AI 补充讲解</div>',
              '<h3>'+escape(card["title"])+'</h3><p>'+escape(card["summary"])+'</p>',
              '<p><strong>什么时候用：</strong>'+escape(card["when_to_use"])+'</p><ol>']
    pieces.extend('<li>'+escape(step)+'</li>' for step in card["steps"])
    pieces.append('</ol>')
    notes = ['\n\n> **AI 补充讲解：'+md(card["title"])+'**\n>\n> '+md(card["summary"])+'\n>\n> 什么时候用：'+md(card["when_to_use"])]
    notes.extend('> '+str(i)+'. '+md(step) for i,step in enumerate(card["steps"],1))
    if card.get("example"):
        sample = card["example"]
        label = ("官方示例" if sample["origin"]=="official" else "AI 补充示例")+"；"+("已运行验证："+sample["test_evidence"] if sample["tested"] else "未运行验证")
        pieces.append('<small>'+escape(label)+'</small><pre><code>'+escape(sample["code"])+'</code></pre>')
        notes.extend(['> '+md(label), '\n'.join('> '+line for line in fence(sample["code"],sample["language"]).splitlines())])
    if card.get("notes"):
        pieces.append('<ul>'+''.join('<li>'+escape(note)+'</li>' for note in card["notes"])+'</ul>')
        notes.extend('> 注意：'+md(note) for note in card["notes"])
    for reference in card.get("references", []):
        pieces.append('<p><a href="'+escape(reference)+'" target="_blank" rel="noopener noreferrer">相关官方说明</a></p>')
        notes.append('> [相关官方说明](<'+reference+'>)')
    return ''.join(pieces)+'</aside>', '\n'.join(notes)+'\n\n'


def render(data, base):
    pages = data["pages"]
    counts = Counter(p["status"] for p in pages)
    known = {p["url"].rstrip("/"):p for p in pages}
    generated = {}
    theme = ""
    if data.get("theme_css"):
        source = (base/data["theme_css"]).resolve()
        require(source.is_relative_to(base.resolve()), "Theme path must stay in collection directory")
        theme = source.read_text(encoding="utf-8")
        require("</style" not in theme.lower(), "Unsafe stylesheet")
    template = Template((ASSETS/"viewer.html").read_text(encoding="utf-8"))
    progress = ''.join('<li id="pending-'+p["id"]+'"><span>'+STATUS[p["status"]]+'</span> '+escape(p["title"])+
                       ' <a href="'+escape(p["url"])+'" target="_blank" rel="noopener noreferrer">原文</a>'+
                       ('<p>'+escape(p["error"])+'</p>' if p["status"]=="failed" else '')+'</li>' for p in pages)
    glossary = ''.join('<div><dt>'+escape(en)+'</dt><dd>'+escape(zh)+'</dd></div>' for en,zh in data.get("glossary",{}).items())
    source_links = '、'.join('<a href="'+escape(u)+'" target="_blank" rel="noopener noreferrer">来源 '+str(i)+'</a>' for i,u in enumerate(data["catalog"]["sources"],1))
    completed = [p for p in pages if p["status"]=="done"]
    markdown_pages = ['# '+md(data["title"])+'\n\n'+md(data["catalog"]["coverage"])+'\n']

    def target(page):
        return filename(page,data) if page["status"]=="done" else "pending.html#pending-"+page["id"]

    def navigation(current):
        groups = {}
        for p in pages:
            if p["url"].rstrip("/") == data["root_url"].rstrip("/"): continue
            root,_,sub = p["section"].partition(" / ")
            groups.setdefault(root,{}).setdefault(sub,[]).append(p)
        output = ['<a class="d2c-home" href="index.html">文档首页</a>']
        for index,(root,subs) in enumerate(groups.items()):
            output.append('<section class="d2c-nav-group d2c-color-'+str(index%4)+'"><h2>'+escape(root)+'</h2>')
            for sub,entries in subs.items():
                if sub: output.append('<details'+(' open' if current in entries else '')+'><summary>'+escape(sub)+'</summary>')
                for p in entries:
                    search = p["title"]+' '+p.get("source_title","")+' '+p["url"]+' '+''.join(plain(Fragment(b["html"]).root) for b in p.get("blocks",[]))
                    output.append('<a class="d2c-page-link'+(' d2c-current' if p is current else '')+'" data-search="'+escape(search)+'" href="'+target(p)+'">'+escape(p["title"])+
                                  ('<small>待翻译</small>' if p["status"]!="done" else '')+'</a>')
                if sub: output.append('</details>')
            output.append('</section>')
        return ''.join(output)

    def wrap(content, current):
        return template.substitute(title=escape(current["title"] if current else "待翻译文档"),site_title=escape(data["title"]),
            theme_css=theme, navigation=navigation(current),content=content,glossary=glossary,
            done=counts["done"],total=len(pages),failed=counts["failed"],coverage=escape(data["catalog"]["coverage"]),
            source_links=source_links,progress=progress,source_url=escape(current["url"] if current else data["root_url"]),
            read_at=escape(current.get("read_at","") if current else ""),version=escape(current.get("version","") if current else ""),
            official_license='<a href="assets/LICENSE-Streamlit.txt">原文许可</a>' if (base/"assets/LICENSE-Streamlit.txt").exists() else "")

    for page in completed:
        def resolve_url(value, kind):
            absolute = urljoin(page["url"],value)
            address,fragment = urldefrag(absolute)
            linked = known.get(address.rstrip("/"))
            if kind=="href" and linked:
                return target(linked)+("#"+fragment if fragment and linked["status"]=="done" else "")
            if kind in {"src","poster"} and absolute in data.get("assets",{}): return data["assets"][absolute]
            return absolute
        annotations = {c["after"]:c for c in page.get("cards",[])}
        content = []
        notes = ['\n\n---\n\n## '+md(page["title"])+'\n\n原文：[打开原文](<'+page["url"]+'>)\n\n']
        for block in page["blocks"]:
            fragment = Fragment(block["html"]).root
            content.append(document_html(fragment,resolve_url,block["id"]))
            markdown_root = Fragment(block["html"]).root
            for node in elements(markdown_root):
                for kind in ("href", "src", "poster"):
                    if node[1].get(kind):
                        address = urljoin(page["url"], node[1][kind])
                        node[1][kind] = data.get("assets", {}).get(address, address) if kind != "href" else address
            notes.append(html_md(markdown_root))
            if block["id"] in annotations:
                supplemental,supplemental_md = explanation(annotations[block["id"]])
                content.append(supplemental);notes.append(supplemental_md)
        generated[filename(page,data)] = wrap(''.join(content),page)
        markdown_pages.append(''.join(notes))
    generated["pending.html"] = wrap('<h1>此页尚未翻译</h1><p>可以在聊天中指定这一页，或说“继续”处理下一批。下列每页均提供官方原文入口。</p><ul class="d2c-pending-list">'+progress+'</ul>',None)
    if "index.html" not in generated:
        generated["index.html"] = generated[filename(completed[0],data)] if completed else generated["pending.html"]
    markdown_pages.append('\n\n## 中英术语对照\n\n'+'\n'.join('- '+md(en)+'：'+md(zh) for en,zh in data.get("glossary",{}).items()))
    generated["cards.md"] = ''.join(markdown_pages)+'\n'
    return generated

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("collection", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--next", action="store_true", help="List the next batch without modifying files")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--section", default="", help="Match part of a Chinese chapter path")
    parser.add_argument("--retry-failed", action="store_true", help="Select failed pages instead of pending pages")
    args = parser.parse_args()
    try:
        require(args.limit > 0, "limit must be greater than zero")
        data = json.loads(args.collection.read_text(encoding="utf-8-sig"))
        validate(data)
        if args.next:
            status = "failed" if args.retry_failed else "pending"
            pages = [p for p in data["pages"] if p["status"] == status
                     and args.section.casefold() in p["section"].casefold()]
            print(json.dumps({"remaining": len(pages), "pages": [
                {key: page[key] for key in ("id", "title", "url", "section", "status")}
                for page in pages[:args.limit]]}, ensure_ascii=True))
            return 0
        generated = render(data, args.collection.parent)
        output = args.output or args.collection.parent
        output.mkdir(parents=True, exist_ok=True)
        if output.resolve() != args.collection.parent.resolve() and (args.collection.parent / "assets").exists():
            shutil.copytree(args.collection.parent / "assets", output / "assets", dirs_exist_ok=True)
        for name, content in generated.items():
            temporary = output / (name + ".tmp")
            temporary.write_text(content, encoding="utf-8", newline="\n")
            temporary.replace(output / name)
        print(json.dumps({"html": str(output / "index.html"), "markdown": str(output / "cards.md")}, ensure_ascii=True))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
