# 文档集合格式（版本 2）

collection.json 是目录、原文、译文、补充卡片和进度的数据源，使用 UTF-8。原文快照只读，新增译文时不得修改它以绕过校验。

~~~json
{
  "schema_version": 2,
  "title": "示例中文文档",
  "root_url": "https://docs.example.org/guide/",
  "catalog": {
    "sources": ["https://docs.example.org/llms.txt"],
    "coverage": "说明索引来源、发现时间、版本范围和已知覆盖限制。"
  },
  "glossary": {"widget": "交互组件"},
  "pages": [
    {
      "id": "intro",
      "url": "https://docs.example.org/guide/intro",
      "title": "快速入门",
      "source_title": "Getting started",
      "section": "入门 / 基础概念",
      "status": "done",
      "read_at": "2026-10-17T12:00:00+08:00",
      "version": "1.0",
      "source_blocks": [
        {"id": "b001", "html": "<h1>Getting started</h1>"},
        {"id": "b002", "html": "<p>A widget accepts user input.</p>"},
        {"id": "b003", "html": "<pre><code>print(1 + 1)</code></pre>"}
      ],
      "blocks": [
        {"id": "b001", "html": "<h1>快速入门</h1>"},
        {"id": "b002", "html": "<p>交互组件用于接收用户输入。</p>"},
        {"id": "b003", "html": "<pre><code>print(1 + 1)</code></pre>"}
      ],
      "cards": [
        {
          "id": "widget-note",
          "after": "b002",
          "title": "怎样理解交互组件？",
          "summary": "可以把它理解为页面上的输入入口。",
          "when_to_use": "需要理解用户输入与后续代码的关系时。",
          "steps": ["先确定需要接收哪一种输入。"],
          "notes": ["这张卡是补充解释，不替代上面的官方译文。"]
        }
      ]
    },
    {
      "id": "next",
      "url": "https://docs.example.org/guide/next",
      "title": "下一课",
      "section": "入门 / 基础概念",
      "status": "pending",
      "cards": []
    }
  ]
}
~~~

## 正文与完整性

- source_blocks 和 blocks 都是非空的有序列表，ID 唯一，两者 ID 列表必须完全一致。每块 html 是完整、闭合的 HTML 片段。
- 原文与译文使用相同标签、层级、链接和媒体属性；可翻译文本及 alt/title。HTML 只允许文档语义标签和必要的静态属性，不允许脚本、事件处理器、任意样式或可执行 URL。
- pre/code/kbd/samp/tt 和函数签名区域的内容保持原样，包括缩进、注释、字符串和空行。需要额外示例时放入补充卡片。
- 可保留的主要节点包括标题、段落、列表、表格、说明区、图片、折叠区和代码。装饰图标可以规范化；无法支持的语义内容须记录并解决，不能删除后假称完整。
- done 表示该页已完整读到末尾、全部正文完成翻译并核对；不要求有卡片。必须设置带时区的 read_at，version 仅填写明确的官方文档版本。
- pending 不设置 read_at，不在集合中保存部分译文或卡片；过程稿单独保存，完成后原子更新整页。
- failed 同 pending，并必须给出非空 error，说明重试后仍无法获取的具体原因。

## 目录与路径

- root_url 为该次文档的实际范围。页面同源且位于该路径范围；若输入单篇文章，不把文章 URL 错当整站目录。
- 页面 id 为稳定的小写英文/数字/连字符名称；URL 去除片段后唯一。不要随译文标题修改 ID。
- pages 保持原站目录顺序，首页也纳入。section 使用中文父级路径区分同名章节。
- catalog.sources 为实际读取过的目录或索引 URL；coverage 说明版本、时间和覆盖限制，不把目录发现率当作正文完成率。

## 辅助卡片

- 每张卡片必须包含 id、after、title、summary、when_to_use 和非空字符串列表 steps。notes 为可选字符串列表。
- after 必须指向本页存在的正文块 ID；同一块最多一张卡片。作者还需核对同一逻辑小节最多一张，不仅依赖 ID 校验。
- references 为可选的官方说明 URL 列表，用于版本差异等需要明确出处的补充。
- 卡片字段使用纯文本，不写 HTML/Markdown。可选 example 的格式如下：

~~~json
{
  "language": "python",
  "code": "print(1 + 1)",
  "origin": "ai",
  "tested": false
}
~~~

origin 仅为 official 或 ai。tested 为 true 时必须提供 test_evidence，写清实际运行命令和结果。官方正文中的代码无需用 example 重录。

## 本地样式与媒体（选填）

~~~json
{
  "theme_css": "assets/official.css",
  "assets": {
    "https://docs.example.org/images/diagram.png": "assets/diagram.png"
  }
}
~~~

样式文件必须位于集合目录内，引用的字体和图片也应本地化。HTML 使用媒体映射，文档内部已译链接改为本地页面；Markdown 链接解析到原始官方 URL，媒体使用本地映射。在线演示在原位置保留明确的联网入口，不嵌入来源脚本。

## 命令与产物

- 生成：python scripts/build_cards.py <collection.json> --output <目录>；默认输出至集合目录。运行只需要 Python 标准库。
- 首页保留 index.html；已译内容页使用稳定文件名；未译内容通过 pending.html 显示状态和官方原文入口；cards.md 汇总完整译文和明确标记的补充卡片。
- 继续：--next，仅输出 remaining 和本批 pages，不写文件。默认 --limit 5，必须为正整数。
- 章节：--next --section "章节路径子串"；失败重试：--next --retry-failed。
- 无效数据返回非零并说明原因，校验完成前不覆盖已有产物。

