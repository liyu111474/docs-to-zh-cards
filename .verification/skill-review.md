# 本地技能验证记录

日期：2026-10-17。目标：项目内的 docs-to-zh-cards；本轮不更新用户技能目录，不初始化 Git 或上传 GitHub。

## 官方初始化与文件

使用官方 skill-creator/scripts/init_skill.py 在 .verification/official-init/ 创建同名新骨架，完成 SKILL.md 和 agents/openai.yaml 后合并回项目。没有对已有技能目录执行初始化覆盖。保留原有模板、数据格式说明及两个必要的 Python 文件，未添加生产脚本。

## 不同文章类型

使用项目中已有的完整原文快照与译文重新生成并复核；本轮没有把旧摘要当作全文，也没有新增已翻译页面计数。

| 类型 | 实际样本 | 正文块 | 原样代码块 | 检查重点与结果 |
| --- | --- | ---: | ---: | --- |
| 文档首页 | Streamlit 首页 | 16 | 0 | 保留简介、栏目和三色入口；1 张图片本地加载成功 |
| 操作指南 | Streamlit 命令行安装 | 35 | 12 | 步骤与命令保持顺序；在线演示保留入口 |
| 概念说明 | Streamlit 基础概念 | 92 | 18 | 段落、层级与示例保留；修复嵌套结构校验漏洞 |
| 实践教程 | Streamlit 创建应用 | 75 | 20 | 从开头到结尾核对；缓存说明的版本差异在补充卡中注明 |
| API 参考 | st.write 与 st.button | 21 | 7 | 签名、3 个表格及参数说明保留；10 个动态演示提供明确链接 |
| 其他站点教程 | Python 非正式入门 | 9 | 42 | 包含嵌套章节、REPL 示例与脚注；代码与源快照一致 |

样本共 248 个正文块、99 个原样代码块。官方来源分别为 [Streamlit 文档](https://docs.streamlit.io/) 与 [Python 教程](https://docs.python.org/3/tutorial/introduction.html)，各页原文链接、读取时间及版本保存在对应 collection.json 中。

## 根据测试改进

先新增回归测试，证明旧校验允许嵌套列表脱离原父节点；首次运行 11 项测试，其中此项失败。随后把结构比较改为包含父子层级，全部 11 项通过。SKILL.md 同时补充列表嵌套、表格行列、提示所属小节和人工连贯通读要求。结构一致不等于译文语义完整。

## 验证结果

- python -m unittest discover -s tests -p test_cards.py：11 项通过；包括无效输入保留产物、断点继续、脚本注入拒绝、代码缩进与空行保留。
- 官方 quick_validate.py docs-to-zh-cards：Skill is valid!；另核对界面简介长度、默认提示中的技能名及自动匹配配置。
- node tests/check_viewer.mjs：7 个实际页面通过正文块顺序及代码原文比对；Streamlit 桌面与 390px 手机布局无横向溢出，Python 手机布局通过。
- 关闭补充讲解、搜索导航后，官方译文正文不变；首页没有远程静态资源请求；没有浏览器运行异常。结果保存于 viewer-checks-full.json。

这里只验证了示例代码的原样保留，没有执行 Streamlit 或 Python 官方示例。剩余待译页仍保持待译状态。
