import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "docs-to-zh-cards" / "scripts" / "build_cards.py"


def collection():
    return {
        "schema_version": 2,
        "title": "示例中文知识卡片",
        "root_url": "https://docs.example.org/guide/",
        "catalog": {"sources": ["https://docs.example.org/llms.txt"],
                    "coverage": "已读取文档索引，正文分批处理。"},
        "glossary": {"widget": "交互组件"},
        "pages": [{
            "id": "intro", "url": "https://docs.example.org/guide/intro",
            "title": "入门", "section": "入门", "status": "done",
            "read_at": "2026-10-17T12:00:00+08:00", "version": "1.0",
            "source_blocks": [
                {"id": "b001", "html": "<h1>Get started</h1>"},
                {"id": "b002", "html": "<p>First paragraph.</p>"},
                {"id": "b003", "html": "<p>Second paragraph.</p>"},
                {"id": "b004", "html": '<pre><code>if True:\n    print("hello")</code></pre>'}],
            "blocks": [
                {"id": "b001", "html": "<h1>开始使用</h1>"},
                {"id": "b002", "html": "<p>第一段完整译文。</p>"},
                {"id": "b003", "html": "<p>第二段完整译文。</p>"},
                {"id": "b004", "html": '<pre><code>if True:\n    print("hello")</code></pre>'}],
            "cards": [{"id": "hello", "title": "第一个按钮", "summary": "显示一个交互组件。",
                       "after": "b002",
                       "when_to_use": "需要用户点击时。", "steps": ["导入模块。"],
                       "notes": ["点击后观察结果。"],
                       "example": {"language": "python", "code": 'if True:\n    print("你好")',
                                   "origin": "ai", "tested": False}}]
        }]
    }


class CardsCLI(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix=".cards-test-", dir=ROOT)
        assert Path(self.temp.name).resolve().is_relative_to(ROOT)
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.source = self.folder / "collection.json"
        self.output = self.folder / "output"

    def run_cli(self, data, *args):
        self.source.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(self.source), "--output", str(self.output), *args],
            capture_output=True, encoding="utf-8", errors="replace",
        )

    def test_generates_matching_offline_html_and_markdown(self):
        result = self.run_cli(collection())
        self.assertEqual(result.returncode, 0, result.stderr)
        html = (self.output / "index.html").read_text(encoding="utf-8")
        markdown = (self.output / "cards.md").read_text(encoding="utf-8")
        for content in (html, markdown):
            self.assertIn("第一个按钮", content)
            self.assertIn("https://docs.example.org/guide/intro", content)
            self.assertIn("未运行验证", content)
            self.assertIn('    print(', content)
        self.assertNotIn('<script src=', html)
        self.assertNotIn('fetch(', html)
        self.assertIn('widget', html)
        document = html.split('<article id="d2c-document"', 1)[1]
        self.assertLess(document.index("第一段完整译文"), document.index("第一个按钮"))
        self.assertLess(document.index("第一个按钮"), document.index("第二段完整译文"))
        self.assertIn("第一段完整译文", markdown)
        self.assertIn('    print("hello")', markdown)

    def test_invalid_data_preserves_existing_outputs(self):
        self.assertEqual(self.run_cli(collection()).returncode, 0)
        previous = {name: (self.output / name).read_bytes() for name in ("index.html", "cards.md")}
        invalid = []
        data = collection()
        data["catalog"]["sources"] = []
        invalid.append(data)
        data = collection()
        del data["pages"][0]["url"]
        invalid.append(data)
        data = collection()
        data["pages"][0]["url"] = "javascript:alert(1)"
        invalid.append(data)
        data = collection()
        data["pages"][0]["url"] = "https://another.example.org/guide/intro"
        invalid.append(data)
        data = collection()
        data["pages"][0]["read_at"] = ""
        invalid.append(data)
        data = collection()
        data["pages"][0]["status"] = "failed"
        data["pages"][0]["error"] = "无法读取正文"
        invalid.append(data)
        data = collection()
        data["pages"].append(dict(data["pages"][0]))
        invalid.append(data)
        for case, data in enumerate(invalid):
            with self.subTest(case=case):
                result = self.run_cli(data)
                self.assertNotEqual(result.returncode, 0)
                self.assertTrue(result.stderr.strip())
                for name, content in previous.items():
                    self.assertEqual((self.output / name).read_bytes(), content)

    def test_document_html_and_code_remain_text(self):
        data = collection()
        payload = '<img src=x onerror="alert(1)"><script>alert(2)</script>'
        data["pages"][0]["cards"][0]["summary"] = payload
        data["pages"][0]["cards"][0]["example"]["code"] = '```\n' + payload
        result = self.run_cli(data)
        self.assertEqual(result.returncode, 0, result.stderr)
        html = (self.output / "index.html").read_text(encoding="utf-8")
        markdown = (self.output / "cards.md").read_text(encoding="utf-8")
        self.assertNotIn(payload, html)
        self.assertIn('&lt;img', html)
        self.assertIn('````python', markdown)

    def test_continue_selects_only_next_pending_pages_without_writing(self):
        data = collection()
        data["pages"].extend([
            {"id": "button", "url": "https://docs.example.org/guide/button", "title": "按钮",
             "section": "组件", "status": "pending", "cards": []},
            {"id": "cache", "url": "https://docs.example.org/guide/cache", "title": "缓存",
             "section": "进阶", "status": "failed", "cards": [], "error": "HTTP 503；已重试一次"},
            {"id": "input", "url": "https://docs.example.org/guide/input", "title": "输入",
             "section": "组件", "status": "pending", "cards": []},
        ])
        result = self.run_cli(data, "--next", "--limit", "1")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([p["id"] for p in json.loads(result.stdout)["pages"]], ["button"])
        self.assertFalse(self.output.exists())
        self.assertEqual(json.loads(self.source.read_text(encoding="utf-8")), data)
        for arguments, expected in [(("--next", "--section", "组件"), ["button", "input"]),
                                    (("--next", "--retry-failed"), ["cache"]),
                                    (("--next", "--section", "不存在的章节"), [])]:
            result = self.run_cli(data, *arguments)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual([p["id"] for p in json.loads(result.stdout)["pages"]], expected)
        invalid_limit = self.run_cli(data, "--next", "--limit", "0")
        self.assertNotEqual(invalid_limit.returncode, 0)

    def test_reading_a_page_moves_it_out_of_next_batch_and_keeps_existing_cards(self):
        data = collection()
        data["pages"].append({"id": "next", "url": "https://docs.example.org/guide/next", "title": "下一课",
                              "section": "入门", "status": "pending", "cards": []})
        self.assertEqual(self.run_cli(data).returncode, 0)
        data["pages"][1].update(status="done", read_at="2026-10-17T13:00:00+08:00",
                                cards=[{"id": "next-concept", "title": "下一课知识点", "summary": "继续学习。",
                                        "after": "b001", "when_to_use": "学完第一课后。", "steps": ["阅读正文。"]}],
                                source_blocks=[{"id": "b001", "html": "<p>Next lesson.</p>"}],
                                blocks=[{"id": "b001", "html": "<p>下一课。</p>"}])
        self.assertEqual(self.run_cli(data).returncode, 0)
        result = self.run_cli(data, "--next")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["pages"], [])
        html = (self.output / "index.html").read_text(encoding="utf-8")
        markdown = (self.output / "cards.md").read_text(encoding="utf-8")
        self.assertEqual(markdown.count('第一个按钮'), 1)
        self.assertEqual(markdown.count('下一课知识点'), 1)

    def test_translation_cannot_omit_reorder_or_modify_official_code(self):
        for change in ('omit','reorder','code','empty','duplicate'):
            data = collection()
            blocks = data['pages'][0]['blocks']
            if change == 'omit': blocks.pop()
            if change == 'reorder': blocks[0],blocks[1] = blocks[1],blocks[0]
            if change == 'code': blocks[-1]['html'] = '<pre><code>print("rewritten")</code></pre>'
            if change == 'empty': blocks[2]['html'] = '<p></p>'
            if change == 'duplicate': blocks.append(dict(blocks[-1]))
            with self.subTest(change=change):
                result = self.run_cli(data)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(self.output.exists())

    def test_complete_translation_does_not_require_ai_cards(self):
        data = collection()
        data['pages'][0]['cards'] = []
        result = self.run_cli(data)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn('第二段完整译文',(self.output/'cards.md').read_text(encoding='utf-8'))

    def test_nested_explanation_list_must_keep_its_parent(self):
        data = collection()
        data['pages'][0]['source_blocks'][1]['html'] = '<ul><li>Parent<ul><li>Child</li></ul></li></ul>'
        data['pages'][0]['blocks'][1]['html'] = '<ul><li>父项</li><ul><li>子项</li></ul></ul>'
        result = self.run_cli(data)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.output.exists())

    def test_function_signature_outside_code_tag_cannot_be_rewritten(self):
        data = collection()
        data['pages'][0]['source_blocks'].append({'id':'signature','html':'<div class="function-signature">run(arg=1)</div>'})
        data['pages'][0]['blocks'].append({'id':'signature','html':'<div class="function-signature">run(arg=2)</div>'})
        self.assertNotEqual(self.run_cli(data).returncode,0)

    def test_tables_images_and_copied_assets_survive_generation(self):
        data = collection()
        data['theme_css']='assets/official.css'
        data['assets']={'https://docs.example.org/image.png':'assets/image.png'}
        assets=self.folder/'assets';assets.mkdir()
        (assets/'official.css').write_text('body{color:#123456}',encoding='utf-8')
        (assets/'image.png').write_bytes(b'fixture-image')
        source='<table><tr><th>Name</th><th>Meaning</th></tr><tr><td><code>key</code></td><td>Identifier</td></tr></table><p><a href="https://docs.example.org/guide/intro">Introduction</a><img src="https://docs.example.org/image.png" alt="Example"></p>'
        translated='<table><tr><th>名称</th><th>含义</th></tr><tr><td><code>key</code></td><td>标识符</td></tr></table><p><a href="https://docs.example.org/guide/intro">入门</a><img src="https://docs.example.org/image.png" alt="示例"></p>'
        data['pages'][0]['source_blocks'].append({'id':'media','html':source})
        data['pages'][0]['blocks'].append({'id':'media','html':translated})
        result=self.run_cli(data)
        self.assertEqual(result.returncode,0,result.stderr)
        html=(self.output/'index.html').read_text(encoding='utf-8')
        markdown=(self.output/'cards.md').read_text(encoding='utf-8')
        self.assertIn('src="assets/image.png"',html)
        self.assertIn('alt="示例"',html)
        self.assertIn('| 名称 | 含义 |',markdown)
        self.assertIn('| --- | --- |',markdown)
        self.assertIn('标识符',markdown)
        self.assertIn('![示例](<assets/image.png>)',markdown)
        self.assertEqual((self.output/'assets/image.png').read_bytes(),b'fixture-image')

    def test_markdown_keeps_blank_lines_inside_official_code(self):
        data=collection()
        source_code='value = 1\n\n\nprint(value)\n'
        fragment='<pre><code>'+source_code+'</code></pre>'
        data['pages'][0]['source_blocks'][-1]['html']=fragment
        data['pages'][0]['blocks'][-1]['html']=fragment
        result=self.run_cli(data)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn(source_code,(self.output/'cards.md').read_text(encoding='utf-8'))


if __name__ == "__main__":
    unittest.main()
