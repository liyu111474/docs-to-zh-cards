# 英文文档完整翻译与辅助知识卡片

## 项目解决什么问题

打开英文技术文档却看不懂时，可以使用 `docs-to-zh-cards`，让 Codex 按原文顺序逐段翻译为中文，保留完整正文，并用少量辅助知识卡片解释术语和难点。

这是一个 Codex Skill。Codex 负责联网阅读、理解和翻译，Python 负责校验数据、选择批次及生成本地文件。翻译按批推进，每页完整翻译并核对后才计入完成进度。

## 主要功能

- **完整中文文档**：保留标题、段落、列表、表格、参数说明、提示和图片；代码、命令、函数签名、代码中的字符串与注释保持原样。
- **辅助知识卡片**：在相关小节后插入标明“AI 补充讲解”的卡片，可整体隐藏；隐藏后正文仍完整连续。
- **本地阅读与导出**：生成可直接打开的 HTML 和包含完整译文的 Markdown，布局尽量贴近原站；正文及已保存的静态资源支持离线阅读，动态演示保留在线入口。
- **目录与状态**：分层目录支持中文、英文和 API 名称搜索；已译页面本地跳转，未译项标注状态并提供官方原文入口，进度集中显示在辅助区域。
- **分批继续**：默认每批处理 5 页，保存原文、译文及进度，支持继续下一批、指定章节和重试失败页面。

版式保留程度取决于原站结构和可获取的静态资源。官方示例保持原样，不代表已运行验证。

## 安装方法

需要可使用技能及联网阅读工具的 Codex，以及可通过 `python` 命令调用的 Python。生成器只依赖 Python 标准库，无需安装 Streamlit 或单独配置翻译 API。

将整个 `docs-to-zh-cards` 文件夹复制到 `$CODEX_HOME/skills/`；未设置 `CODEX_HOME` 时，使用 `~/.codex/skills/`（Windows 默认为 `%USERPROFILE%\.codex\skills\`）。已有同名技能时，先备份并将旧目录移出安装位置。

在项目根目录执行以下 PowerShell 命令可安装；目标已存在时会停止，避免直接覆盖：

```powershell
$codexSkillHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
$skillTarget = Join-Path $codexSkillHome 'skills\docs-to-zh-cards'
if (Test-Path -LiteralPath $skillTarget) { throw '目标已存在，请先备份并移出旧版本，再安装。' }
New-Item -ItemType Directory -Path (Split-Path -Parent $skillTarget) -Force | Out-Null
Copy-Item -LiteralPath '.\docs-to-zh-cards' -Destination $skillTarget -Recurse
```

安装后重新启动 Codex，在需要保存翻译结果的项目中使用。技能说明见 [SKILL.md](docs-to-zh-cards/SKILL.md)，界面元信息见 [agents/openai.yaml](docs-to-zh-cards/agents/openai.yaml)。

## 使用方法

### 在 Codex 中翻译

首次提供公开英文文档链接，明确需要完整翻译：

```text
使用 $docs-to-zh-cards 完整翻译 https://docs.streamlit.io/，保留官网首页、目录和全部示例，先处理首批页面。
```

后续可在同一项目中分别输入：

| 需求 | 输入示例 |
| --- | --- |
| 处理下一批 | `继续` |
| 指定章节 | `继续翻译入门章节` |
| 重试读取失败的页面 | `重试失败页面` |

首次建立目录后分批阅读正文；发现页面并不表示已经翻译完成。完成一批后打开生成的 `index.html` 阅读，或查看 `cards.md`。

### 从已有数据生成文件

在项目根目录执行：

```powershell
# 校验已有数据，并在集合目录生成 HTML 和 Markdown
python .\docs-to-zh-cards\scripts\build_cards.py .\knowledge-cards\docs.streamlit.io\collection.json

# 只查看下一批待译页面，不修改文件
python .\docs-to-zh-cards\scripts\build_cards.py .\knowledge-cards\docs.streamlit.io\collection.json --next
```

`--next` 只选择页面并输出 JSON，不会自行联网、翻译或更新进度。可配合 `--limit 5` 指定批量大小、`--section "入门"` 筛选章节，或 `--retry-failed` 选择失败页面。生成时可用 `--output <目录>` 指定输出位置。

数据格式见 [版本 2 数据说明](docs-to-zh-cards/references/collection-format.md)。无效数据会报错，校验失败时保留已有产物。

### 本地验证

```powershell
python -m unittest discover -s tests -p test_cards.py
```

技能格式使用官方 `skill-creator/scripts/quick_validate.py` 校验，目标为本地 `docs-to-zh-cards` 目录；该校验工具自身依赖 PyYAML，生成器不需要。已有文章测试与浏览器检查记录见 [验证记录](.verification/skill-review.md)。

### 公开文件范围

`.verification/` 仅保留验证记录、最新浏览器检查结果，以及桌面首页、手机首页和安装页三张截图用于公开。下载依赖、临时原文快照、初始化副本和旧版验证结果仅在本地保留，由 `.gitignore` 排除；`archive/`、Python 缓存及临时生成文件也不纳入公开范围。

完整文件清单与复查结果见 [公开文件清单](PUBLIC_FILES.md)。本地备份和临时文件仍保存在磁盘上；分享文件时应按清单选择，直接压缩整个项目不会自动应用 `.gitignore`。

## 输入与输出示例

**输入**：公开文档链接 `https://docs.streamlit.io/`，以及上面的完整翻译请求。

**输出**：默认保存到当前项目的 `knowledge-cards/<站点及文档路径>/`，Streamlit 示例为：

```text
knowledge-cards/docs.streamlit.io/
├── index.html           中文文档首页
├── page-<稳定标识>.html  已翻译的正文页
├── pending.html         页面状态与官方原文入口
├── cards.md             所有已译页的完整译文与辅助卡片
├── collection.json      文档目录、原文、译文、术语、卡片与进度
└── assets/              本地样式、字体、图片及许可说明等资源
```

| 文件 | 可打开的现有示例 |
| --- | --- |
| 中文首页 | [Streamlit 中文文档](knowledge-cards/docs.streamlit.io/index.html) |
| 已译正文页 | [通过命令行安装 Streamlit](knowledge-cards/docs.streamlit.io/page-10fe4049bc7c.html) |
| 完整 Markdown | [cards.md](knowledge-cards/docs.streamlit.io/cards.md) |
| 目录与断点数据 | [collection.json](knowledge-cards/docs.streamlit.io/collection.json) |
| 其他站点 | [Python 教程中文示例](knowledge-cards/docs.python.org-3-tutorial/index.html) |

当前随附的 Streamlit 示例已完成 **6／385 页**：官网首页、命令行安装、基础概念、创建应用、`st.write` 和 `st.button`。385 是已发现的目录页面数，剩余 379 页仍待翻译，不表示整站翻译已完成。后续进度以 `collection.json` 为准。
