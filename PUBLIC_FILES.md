# 公开文件清单

本清单根据当前项目文件及 .gitignore 整理，列出拟纳入版本管理和公开范围的文件。忽略规则不会删除本地文件，直接压缩整个目录也不会自动应用这些规则。

## 公开范围

共 **75 个文件**。验证目录仅公开 5 份已审阅材料：验证说明、最新浏览器检查结果及三张截图。旧版备份、下载依赖、临时快照、初始化副本、Python 缓存及临时生成文件保持在本地，排除在公开范围之外。

| 分组 | 文件数 |
| --- | ---: |
| .verification | 5 |
| docs-to-zh-cards | 6 |
| knowledge-cards | 58 |
| tests | 2 |
| 根目录 | 4 |

## 复查结果

- 公开清单中没有 archive/、__pycache__ 目录或 .pyc 文件。
- 未发现本机用户名、个人目录或本机真实绝对路径。Python 官方教程中的虚构路径示例按原文保留。
- 未发现常见 API Key、访问令牌或私钥；README 的项目内链接均指向公开文件。
- 截图已检查可见内容，未见个人信息；PNG 中没有文本或 EXIF 元数据。
- 源码、测试、译文、资源及本地备份保持原样；仅新增忽略规则与本清单，并更新 README 的公开范围说明。

## 完整文件列表

以下均为相对于项目根目录的路径，包含本清单自身。

~~~text
.gitignore
.verification/desktop-full.png
.verification/installation-full.png
.verification/mobile-full.png
.verification/skill-review.md
.verification/viewer-checks-full.json
LICENSE
PUBLIC_FILES.md
README.md
docs-to-zh-cards/SKILL.md
docs-to-zh-cards/agents/openai.yaml
docs-to-zh-cards/assets/viewer.html
docs-to-zh-cards/references/collection-format.md
docs-to-zh-cards/scripts/build_cards.py
docs-to-zh-cards/scripts/document_html.py
knowledge-cards/docs.python.org-3-tutorial/cards.md
knowledge-cards/docs.python.org-3-tutorial/collection.json
knowledge-cards/docs.python.org-3-tutorial/index.html
knowledge-cards/docs.python.org-3-tutorial/page-dcff5d405c8a.html
knowledge-cards/docs.python.org-3-tutorial/pending.html
knowledge-cards/docs.streamlit.io/assets/0354e9c659f2d4a0.woff2
knowledge-cards/docs.streamlit.io/assets/0a9f49cc4ca33684.woff2
knowledge-cards/docs.streamlit.io/assets/12a1759e170417bc.woff
knowledge-cards/docs.streamlit.io/assets/177e532832b157ff.woff2
knowledge-cards/docs.streamlit.io/assets/23949f3e88dadc25.woff
knowledge-cards/docs.streamlit.io/assets/2acfef0229601d33.woff2
knowledge-cards/docs.streamlit.io/assets/2b80d36518d6e736.woff
knowledge-cards/docs.streamlit.io/assets/3a76d02e63d3d082.woff2
knowledge-cards/docs.streamlit.io/assets/3a847d4562151148.woff2
knowledge-cards/docs.streamlit.io/assets/416a12e79a748ea8.woff2
knowledge-cards/docs.streamlit.io/assets/43e5a80df569bb41.woff2
knowledge-cards/docs.streamlit.io/assets/460471a12f4a0044.woff
knowledge-cards/docs.streamlit.io/assets/469eb7c77382d620.ttf
knowledge-cards/docs.streamlit.io/assets/4788e390385a08b5.woff
knowledge-cards/docs.streamlit.io/assets/4cd904ad989bc9d0.woff
knowledge-cards/docs.streamlit.io/assets/52ebf67e42f1ca8d.woff
knowledge-cards/docs.streamlit.io/assets/5550fe058f604650.woff
knowledge-cards/docs.streamlit.io/assets/6051e52a0cf6d52a.woff2
knowledge-cards/docs.streamlit.io/assets/620b913c403b6b39.woff2
knowledge-cards/docs.streamlit.io/assets/68d4643052cbdf37.woff
knowledge-cards/docs.streamlit.io/assets/763899a1b19746de.woff2
knowledge-cards/docs.streamlit.io/assets/8580e059a4aa0a65.woff
knowledge-cards/docs.streamlit.io/assets/868fa43c9ab9122c.woff
knowledge-cards/docs.streamlit.io/assets/93663f43f74afda9.eot
knowledge-cards/docs.streamlit.io/assets/9c5968fe378dfee8.svg
knowledge-cards/docs.streamlit.io/assets/9d8f04b2ffa3b1f7.woff
knowledge-cards/docs.streamlit.io/assets/9f57ca04b1b74887.gif
knowledge-cards/docs.streamlit.io/assets/LICENSE-Streamlit.txt
knowledge-cards/docs.streamlit.io/assets/NOTICES-Streamlit.txt
knowledge-cards/docs.streamlit.io/assets/a0db4bb30326ce18.woff2
knowledge-cards/docs.streamlit.io/assets/a4482066a0848c77.woff2
knowledge-cards/docs.streamlit.io/assets/a78a44a2e5cfa24b.woff
knowledge-cards/docs.streamlit.io/assets/ab4e71c3c5d8b253.woff
knowledge-cards/docs.streamlit.io/assets/ac79642470501ee5.woff2
knowledge-cards/docs.streamlit.io/assets/bbbbd7b32ae0a600.woff
knowledge-cards/docs.streamlit.io/assets/c19746e6469350ec.svg
knowledge-cards/docs.streamlit.io/assets/c51fa901985eb1f0.eot
knowledge-cards/docs.streamlit.io/assets/c60f05d86bee22b0.woff2
knowledge-cards/docs.streamlit.io/assets/dc798153cc30825c.woff2
knowledge-cards/docs.streamlit.io/assets/e75de2fac1cabf55.woff2
knowledge-cards/docs.streamlit.io/assets/ebefc6de5cbe05da.woff
knowledge-cards/docs.streamlit.io/assets/fb80a053e4b49e26.png
knowledge-cards/docs.streamlit.io/assets/ff6331989b5c5f61.woff
knowledge-cards/docs.streamlit.io/assets/official.css
knowledge-cards/docs.streamlit.io/cards.md
knowledge-cards/docs.streamlit.io/collection.json
knowledge-cards/docs.streamlit.io/index.html
knowledge-cards/docs.streamlit.io/page-10fe4049bc7c.html
knowledge-cards/docs.streamlit.io/page-4e76630f0871.html
knowledge-cards/docs.streamlit.io/page-7ab46dfd134d.html
knowledge-cards/docs.streamlit.io/page-aa0a8c3291e2.html
knowledge-cards/docs.streamlit.io/page-e7bd0266ac97.html
knowledge-cards/docs.streamlit.io/pending.html
tests/check_viewer.mjs
tests/test_cards.py
~~~

以后新增、删除或调整公开文件时，需要同步更新此清单，并重新检查实际文件内容。
