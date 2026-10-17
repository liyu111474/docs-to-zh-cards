# Streamlit 中文文档

2026-10-17 完整读取官方 llms.txt，并展开知识库的常见问题、安装依赖与部署问题目录，补入官网首页，去重收录 385 个当前文档页面。排除外站、历史更新记录及预发布功能。正文按批次读取，下方计数反映实际进度。站点地图子文件两次下载均因 HTTP 响应不完整而未能完成校验，因此本目录代表已发现页面，不保证索引外没有遗漏。 已译页面按原文顺序逐段保留正文；旧摘要不计入全文翻译进度。


---

## Streamlit 文档

原文：[打开原文](<https://docs.streamlit.io/>)



# Streamlit 文档



[Streamlit](<https://www.streamlit.io>) 是一个开源 Python 框架，数据科学家和 AI／机器学习工程师只需几行代码，就能构建动态数据应用。几分钟内即可构建并部署功能强大的数据应用。现在开始吧！







[

#### 设置与安装



准备好环境，开始使用 Streamlit。

](<https://docs.streamlit.io/get-started/installation>)



[

#### API 参考



了解各项 API，阅读具体函数和功能的实用说明。

](<https://docs.streamlit.io/develop/api-reference>)



[

#### 应用示例库



体验用户创建的优秀应用，示例精选自社区论坛和 Twitter。

](<https://streamlit.io/gallery>)



## 如何使用本文档



[*↗*](<https://docs.streamlit.io/get-started>)

[入门](<https://docs.streamlit.io/get-started>)使用 Streamlit！设置开发环境，学习基础概念，然后开始编写代码！



[*▤*](<https://docs.streamlit.io/develop>)

[开发](<https://docs.streamlit.io/develop>)你的 Streamlit 应用！API 参考通过示例解释每个 Streamlit 函数。阅读概念指南，深入了解各项功能；也可以跟着分步教程动手实践。



[*☁*](<https://docs.streamlit.io/deploy>)

[部署](<https://docs.streamlit.io/deploy>)你的 Streamlit 应用！Streamlit Community Cloud 是免费部署和分享 Streamlit 应用的平台。Streamlit in Snowflake 是企业级解决方案，可将数据与应用统一放在同一个全球系统中。探索适合你的各种选择！



[*▣*](<https://docs.streamlit.io/knowledge-base>)

[知识库](<https://docs.streamlit.io/knowledge-base>)提供自助查阅的技巧、经验和文章，解答创建及部署 Streamlit 应用时遇到的问题。



> **AI 补充讲解：从哪里开始阅读？**
>
> 先读“入门”准备环境，再按需要查阅开发、API 和部署内容。正文保持官网顺序，这些浅紫色卡片只是辅助理解。
>
> 什么时候用：第一次阅读这套文档时。
> 1. 按左侧目录进入章节。
> 2. 遇到术语时查阅补充讲解；也可以关闭上方“显示补充讲解”，连续阅读译文。



## 最新功能



[

#### 侧边抽屉对话框



将 `position="left"` 或 `position="right"` 设置在 `st.dialog` 上，即可将其作为全高侧边抽屉打开。

](<https://docs.streamlit.io/develop/api-reference/execution-flow/st.dialog?utm_source=streamlit>)[

#### 元素的替代文本



使用 `alt` 参数，为图片、媒体、图表、地图和数据表提供屏幕阅读器可读取的名称。

](<https://docs.streamlit.io/develop/api-reference/media/st.image?utm_source=streamlit>)[

#### ECharts 图表



`st.echarts_chart` 使用 Streamlit 主题渲染 Apache ECharts 配置，可传入字典、JSON 字符串或 `pyecharts` 图表。

](<https://docs.streamlit.io/develop/api-reference/charts/st.echarts_chart?utm_source=streamlit>)[

#### 异步应用代码



在应用中直接使用 `async`/`await` 和常见的异步库。缓存装饰器也支持 `async def` 函数。

](<https://docs.streamlit.io/develop/concepts/design/multithreading?utm_source=streamlit>)[

#### 并行局部片段



将 `parallel=True` 设置在 `st.fragment`，可在整页重新运行时并发执行独立的局部片段。

](<https://docs.streamlit.io/develop/api-reference/execution-flow/st.fragment?utm_source=streamlit>)[

#### 后台刷新缓存



在后台更新过期的缓存值，同时让应用继续使用之前的值提供服务。

](<https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data?utm_source=streamlit>)



## 最新博客文章



[查看全部更新](<https://blog.streamlit.io/>)



## 加入社区



Streamlit 不仅是一种创建数据应用的方式，也是创作者交流应用、分享想法并互相帮助改进作品的社区。欢迎加入社区论坛。我们期待听到你的问题和想法，也愿意帮你排查程序中的错误——现在就来看看吧！

[访问论坛](<https://discuss.streamlit.io>)



![](<assets/fb80a053e4b49e26.png>)



## 其他媒体



- [
  
  
  
  
  
  ##### GitHub
  
  
  
  查看 Streamlit 源代码和问题跟踪列表。
  
  ](<https://github.com/streamlit>)
- [
  
  
  
  
  
  ##### YouTube
  
  
  
  观看 Streamlit 团队和社区制作的演示视频。
  
  ](<https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q>)
- [
  
  
  
  
  
  ##### Twitter
  
  
  
  在 Twitter 关注 @streamlit，了解最新消息。
  
  ](<https://twitter.com/streamlit>)
- [
  
  
  
  
  
  ##### LinkedIn
  
  
  
  在全球最大的职业社交网络上关注 @streamlit。
  
  ](<https://www.linkedin.com/company/streamlit>)
- [
  
  
  
  
  
  ##### 电子通讯
  
  
  
  订阅 Streamlit 的消息与动态。
  
  ](<https://info.snowflake.com/streamlit-newsletter-sign-up.html>)



---

## 通过命令行安装

原文：[打开原文](<https://docs.streamlit.io/get-started/installation/command-line>)



# 通过命令行安装 Streamlit



本页将带你使用 `venv` 创建环境，并通过 `pip` 安装 Streamlit。这些是我们推荐的工具；如果你熟悉其他工具，也可以选择自己喜欢的方式。最后，你将构建并运行一个简单的“Hello world”应用。如果更喜欢通过图形界面管理 Python 环境，可以了解如何[使用 Anaconda Distribution 安装 Streamlit](<https://docs.streamlit.io/get-started/installation/anaconda-distribution>).



## 前置条件



和使用其他编程工具一样，安装 Streamlit 前需要先准备好电脑。具体来说，你需要：



1. **Python**
  
  
  
  
  我们支持 [3.11 至 3.15 版本](<https://www.python.org/downloads/>).
2. **Python 环境管理器**（推荐）
  
  
  
  
  环境管理器会创建虚拟环境，让不同项目安装的 Python 软件包彼此隔离。
  
  
  
  
  我们推荐使用虚拟环境，因为安装或升级某个 Python 包，可能会意外影响另一个包。关于 Python 环境的详细介绍，请阅读[Python 虚拟环境入门](<https://realpython.com/python-virtual-environments-a-primer/>).
  
  
  
  
  本指南使用 `venv`，它随 Python 一起提供。
3. **Python 包管理器**
  
  
  
  
  包管理器负责安装各个 Python 软件包，包括 Streamlit。
  
  
  
  
  本指南使用 `pip`，它随 Python 一起提供。
4. **仅 macOS 需要：Xcode 命令行工具**
  
  
  
  
  请按照[这些说明](<https://mac.install.guide/commandlinetools/4.html>)下载 Xcode 命令行工具，让包管理器能够安装 Streamlit 的部分依赖。
5. **代码编辑器**
  
  
  
  
  我们喜欢的编辑器是 [VS Code](<https://code.visualstudio.com/download>)，本套教程也都使用它。



## 使用下列工具创建环境：`venv`



1. 打开终端，进入项目文件夹。
  
  
  
  
  终端
  
  
  
  ```bash
  cd myproject
  
  ```
2. 在终端中输入：
  
  
  
  
  终端
  
  
  
  ```bash
  python -m venv .venv
  
  ```
3. 项目中会出现一个名为“.venv”的文件夹，虚拟环境及其依赖将安装在该目录中。



> **AI 补充讲解：虚拟环境：给项目准备独立的工具箱**
>
> 虚拟环境（virtual environment）把项目所需的 Python 软件包放在单独目录里，便于隔离项目之间的依赖。Streamlit 官方安装教程使用 Python 自带的 venv。
>
> 什么时候用：准备在自己电脑上开始一个 Streamlit 项目时。
> 1. 先安装文档支持的 Python，打开项目文件夹中的终端。
> 2. 创建 .venv；Windows PowerShell 使用下方命令激活，然后再安装依赖。
> 注意：激活命令因操作系统和终端而异。macOS / Linux 使用 source .venv/bin/activate。



## 激活环境



4. 根据所用操作系统，在终端中使用以下相应命令激活环境。
  
  
  
  
  终端
  
  
  
  ```bash
  # Windows command prompt
  .venv\Scripts\activate.bat
  
  # Windows PowerShell
  .venv\Scripts\Activate.ps1
  
  # macOS and Linux
  source .venv/bin/activate
  
  ```
5. 激活后，命令提示符前会以括号显示环境名：“(.venv)”。



## 在环境中安装 Streamlit



6. 在已激活环境的终端中输入：
  
  
  
  
  终端
  
  
  
  ```bash
  pip install streamlit
  
  ```
7. 启动 Streamlit Hello 示例应用，检查安装是否成功：
  
  
  
  
  终端
  
  
  
  ```bash
  streamlit hello
  
  ```
  
  
  
  
  如果该命令无法使用，请尝试完整的模块调用形式：
  
  
  
  
  终端
  
  
  
  ```bash
  python -m streamlit hello
  
  ```
8. Streamlit Hello 应用应当会出现在浏览器的新标签页中！
  
  
  
  
  [交互式演示（打开在线页面）](<https://doc-mpa-hello.streamlit.app/~/+/?embed=true&embed_options=light_theme>)
  
  [使用 Streamlit 构建 🎈](<https://streamlit.io>)
  
  
  
  [全屏 *↗*](<https://doc-mpa-hello.streamlit.app/?utm_medium=oembed>)



*★*

#### 提示



如果你使用 AI 编程代理，可以安装 Streamlit 官方代理技能，让它遵循当前版本的 Streamlit API：



终端



```bash
streamlit skills

```



详情请参阅 [`streamlit skills`](<https://docs.streamlit.io/develop/api-reference/cli/skills>).



9. 完成后关闭终端。



## 创建并运行“Hello World”应用



10. 创建一个名为 `app.py` 的文件，放在项目文件夹中。



Python



```python
import streamlit as st

st.write("Hello world")

```



11. 每次需要使用这个新环境时，都要先进入项目文件夹（其中有 `.venv` 目录），然后运行激活命令：



终端



```bash
# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS and Linux
source .venv/bin/activate

```



12. 激活后，终端提示符开头会以括号显示环境名：“(.venv)”。
13. 运行 Streamlit 应用。



终端



```bash
streamlit run app.py

```



如果该命令无法使用，请尝试完整的模块调用形式：



终端



```bash
python -m streamlit run app.py

```



14. 若要停止 Streamlit 服务，请按 `Ctrl+C`，操作位置是在终端中。
15. 使用环境结束后，输入以下命令回到普通终端环境：



终端



```bash
deactivate

```



> **AI 补充讲解：把 app.py 运行成一个网页**
>
> Streamlit 应用从一个普通 Python 文件开始。使用 Streamlit 的运行命令启动它，网页就能显示文件中的界面内容。
>
> 什么时候用：想从官方演示转到自己的第一个页面时。
> 1. 在项目目录创建 app.py，填入下方 Python 代码。
> 2. 在已激活环境的终端执行 python -m streamlit run app.py。
> 3. 在浏览器查看输出；结束服务时回到终端按 Ctrl+C。
> 注意：以后重新打开终端，先进入项目目录并重新激活环境。结束使用环境可输入 deactivate。



## 下一步



阅读[基础概念](<https://docs.streamlit.io/get-started/fundamentals/main-concepts>)，了解 Streamlit 的数据流模型。



[*←*上一页：使用 Streamlit Playground](<https://docs.streamlit.io/get-started/installation/streamlit-playground>)[*→*下一页：通过 Anaconda Distribution 安装](<https://docs.streamlit.io/get-started/installation/anaconda-distribution>)



*?*

### 还有问题？



我们的[论坛](<https://discuss.streamlit.io>)中有丰富的实用信息，也有许多 Streamlit 专家。



---

## 基础概念

原文：[打开原文](<https://docs.streamlit.io/get-started/fundamentals/main-concepts>)



# Streamlit 基础概念



使用 Streamlit 很简单。先在普通的 Python 脚本中加入几个 Streamlit 命令，再用以下命令运行：`streamlit run`:



终端



```bash
streamlit run your_script.py [-- script args]

```



按上面的方式运行脚本后，本地 Streamlit 服务就会启动，应用会在默认浏览器的新标签页中打开。应用就是你的画布，可以在其中绘制图表、文本、交互组件、表格等内容。



页面具体展示什么，由你决定。例如，[`st.text`](<https://docs.streamlit.io/develop/api-reference/text/st.text>)可以向应用写入原始文本，而 [`st.line_chart`](<https://docs.streamlit.io/develop/api-reference/charts/st.line_chart>)顾名思义，会绘制折线图。请查阅[API 文档](<https://docs.streamlit.io/develop/api-reference>)，了解所有可用命令。



*●*

#### 说明



向脚本传递自定义参数时，参数必须放在两个连字符之后；否则，它们会被当作 Streamlit 自身的参数。



还可以把 Streamlit 当作 Python 模块运行。在配置 PyCharm 等 IDE 时，这种方式可能很有用：



终端



```bash
# Running
python -m streamlit run your_script.py

# is equivalent to:
streamlit run your_script.py

```



*★*

#### 提示



你也可以向 `streamlit run` 传入 URL！与 GitHub Gists 配合使用尤其方便。例如：



终端



```bash
streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py

```



## 开发流程



每次需要更新应用时，请保存源文件。Streamlit 会检测变化，并询问是否重新运行应用。选择屏幕右上方的“Always rerun”（始终重新运行），之后每次修改源码时就会自动更新应用。



这样就能形成快速的交互式开发循环：写代码、保存、实时试用，再继续写一些代码、保存、试用，直到对结果满意。编码与查看结果之间的紧密循环，是 Streamlit 简化开发体验的方式之一。



*★*

#### 提示



开发 Streamlit 应用时，推荐将编辑器和浏览器并排摆放，方便同时查看代码与应用。不妨试试看！



从 Streamlit 1.10.0 开始，应用不能从 Linux 发行版的根目录启动。如果这样运行，Streamlit 会抛出 `FileNotFoundError: [Errno 2] No such file or directory` 错误。更多信息请参阅 GitHub 问题 [\#5239](<https://github.com/streamlit/streamlit/issues/5239>).



如果使用 Streamlit 1.10.0 或更新版本，请将主脚本放在根目录以外的目录中。在 Docker 中，可以使用 `WORKDIR` 命令指定主脚本所在目录。示例请参阅[创建 Dockerfile](<https://docs.streamlit.io/deploy/tutorials/docker#create-a-dockerfile>).



## 数据流



Streamlit 的架构允许你像编写普通 Python 脚本一样编写应用。为了做到这一点，它采用了独特的数据流：屏幕上的内容每当需要更新，Streamlit 就会把整个 Python 脚本从上到下重新运行。



这种情况可能在以下两种情形中发生：



- 修改应用源代码时。
- 用户与应用中的交互组件发生交互时，例如拖动滑块、在输入框中输入文本，或点击按钮。



通过交互组件的 `on_change`（或 `on_click`）参数传入回调函数时，回调总会先于脚本的其余部分运行。回调 API 的详细说明，请参阅[会话状态 API 参考指南](<https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state#use-callbacks-to-update-session-state>).



为了让这一切快速、顺畅地完成，Streamlit 会在后台承担许多复杂工作。其中一个重要角色是 [`@st.cache_data`](<https://docs.streamlit.io/get-started/fundamentals/advanced-concepts#caching>) 装饰器，它使应用重新运行时能够跳过某些代价较高的计算。进阶概念中会更详细地介绍缓存。



> **AI 补充讲解：重新运行：为什么点一下，代码又执行了？**
>
> 默认的数据流可以理解为：交互组件（widget）的值变化时，Streamlit 会重新从上到下执行脚本，再按最新输入刷新界面。
>
> 什么时候用：页面上有滑块、输入框或按钮，需要理解更新顺序时。
> 1. 按从上到下的顺序组织代码。
> 2. 把组件返回的值交给后面的计算和显示语句。
> 3. 修改源码并保存后，可以按页面提示重新运行，开发时也可开启自动重新运行。
> 注意：这里解释默认整页运行方式；进阶的表单和局部重运行有各自规则。



## 展示数据与设置样式



Streamlit 提供多种方式展示表格、数组和数据表。[下面](<https://docs.streamlit.io/get-started/fundamentals/main-concepts#use-magic>)将介绍 *自动显示*和 [`st.write()`](<https://docs.streamlit.io/develop/api-reference/write-magic/st.write>)，它们能够输出文本、表格等多种内容。之后，我们再看看专门用于数据可视化的方法。



### 使用自动显示功能



即使不调用 Streamlit 的方法，也能向应用输出内容。Streamlit 支持“[自动显示命令](<https://docs.streamlit.io/develop/api-reference/write-magic/magic>)”，因此完全不必调用 [`st.write()`](<https://docs.streamlit.io/develop/api-reference/write-magic/st.write>)！试试下面的代码，就能看到效果：



Python



```python
"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

```



只要 Streamlit 看到某个变量或字面量独占一行，就会自动使用 [`st.write()`](<https://docs.streamlit.io/develop/api-reference/write-magic/st.write>) 将它显示在应用中。更多信息请参阅[自动显示命令](<https://docs.streamlit.io/develop/api-reference/write-magic/magic>).



### 显示数据表



与 [自动显示命令](<https://docs.streamlit.io/develop/api-reference/write-magic/magic>),
[`st.write()`](<https://docs.streamlit.io/develop/api-reference/write-magic/st.write>) 是 Streamlit 的“瑞士军刀”。你几乎可以向 [`st.write()`](<https://docs.streamlit.io/develop/api-reference/write-magic/st.write>) 传入任何内容：文本、数据、Matplotlib 图形、Altair 图表等等。不必担心，Streamlit 会判断并正确渲染。



Python



```python
import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

```



你也可以使用其他面向特定数据的函数，例如 [`st.dataframe()`](<https://docs.streamlit.io/develop/api-reference/data/st.dataframe>) 和 [`st.table()`](<https://docs.streamlit.io/develop/api-reference/data/st.table>)，来展示数据。下面我们了解这些功能分别适用于什么情况，以及如何为数据表添加颜色和样式。



你可能会问：“为什么不一直使用 `st.write()`？”原因有以下几个：



1. *自动显示*和 [`st.write()`](<https://docs.streamlit.io/develop/api-reference/write-magic/st.write>) 会检查传入的数据类型，并决定合适的渲染方式。但有时，你希望换一种方式展示。例如，不想把数据表显示成交互式表格，而是希望使用 `st.table(df)`.
2. 第二个原因是，其他方法会返回一个对象，你可以继续添加数据或替换数据，修改它的内容。
3. 最后，使用更具体的 Streamlit 方法时，还可以传入额外参数，自定义其行为。



例如，我们来创建一个数据表，并用 Pandas 的 `Styler` 对象修改其格式。本示例将用 NumPy 生成随机样本，再通过 [`st.dataframe()`](<https://docs.streamlit.io/develop/api-reference/data/st.dataframe>) 方法绘制交互式表格。



*●*

#### 说明



本示例用 NumPy 生成随机样本，但也可以使用 Pandas 数据表、NumPy 数组或普通 Python 数组。



Python



```python
import streamlit as st
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

```



接下来扩展第一个示例，使用 Pandas 的 `Styler` 对象突出显示交互式表格中的某些元素。



Python



```python
import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

```



Streamlit 也提供生成静态表格的方法：[`st.table()`](<https://docs.streamlit.io/develop/api-reference/data/st.table>).



Python



```python
import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

```



### 绘制图表与地图



Streamlit 支持多种常用的数据图表库，例如 [Matplotlib、Altair、deck.gl 等](<https://docs.streamlit.io/develop/api-reference#chart-elements>)。本节会向应用添加柱状图、折线图和地图。



### 绘制折线图



使用 [`st.line_chart()`](<https://docs.streamlit.io/develop/api-reference/charts/st.line_chart>) 就能轻松为应用添加折线图。我们用 NumPy 生成随机样本，再将其绘制出来。



Python



```python
import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

```



### 绘制地图



使用 [`st.map()`](<https://docs.streamlit.io/develop/api-reference/charts/st.map>) 可以在地图上显示数据点。下面用 NumPy 生成一些样本数据，并将它们绘制在旧金山的地图上。



Python



```python
import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

```



## 交互组件



准备好要探索的数据或模型后，就可以加入交互组件，例如 [`st.slider()`](<https://docs.streamlit.io/develop/api-reference/widgets/st.slider>),
[`st.button()`](<https://docs.streamlit.io/develop/api-reference/widgets/st.button>) 或 [`st.selectbox()`](<https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox>)。方法很直接：把交互组件当作变量使用。



Python



```python
import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

```



首次运行时，上面的应用应输出“0 squared is 0”。之后，每次用户操作交互组件时，Streamlit 都会从上到下重新运行脚本，并把组件当前状态赋给相应变量。



例如，用户把滑块移动到 `10` 时，Streamlit 会重新运行上面的代码，并将 `x` 设置为 `10`。因此，此时应当看到“10 squared is 100”。



如果为交互组件指定了唯一字符串 key，也可以通过 key 访问它：



Python



```python
import streamlit as st
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

```



每个设置了 key 的交互组件，都会自动加入会话状态。有关会话状态、它与组件状态的关系及其限制，请参阅[会话状态 API 参考指南](<https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state>).



### 使用复选框显示或隐藏数据



复选框的一种用途，是显示或隐藏应用中的某张图表或某个部分。[`st.checkbox()`](<https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox>) 接收一个参数作为组件标签。此示例通过复选框控制条件语句。



Python



```python
import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

```



### 使用下拉框选择选项



使用 [`st.selectbox`](<https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox>) 可以从一组值中选择。你可以直接写出想要的选项，也可以传入数组或数据表中的一列。



下面使用前面创建的 `df` 数据表。



Python



```python
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

```



> **AI 补充讲解：把用户输入当作 Python 变量**
>
> 滑块、复选框和下拉框会提供当前输入值。把返回值保存到变量，就能用平常的 Python 判断和计算控制页面。
>
> 什么时候用：需要选择筛选条件，或让用户决定是否显示一块内容时。
> 1. 选择合适的输入组件，设置清楚的标签。
> 2. 接住组件返回值，例如复选框返回的布尔值。
> 3. 在后面的 if 判断中使用它，控制显示内容。
> 注意：给组件设置 key 后，可以通过 st.session\_state 访问相关状态；这部分可继续阅读会话状态文档。



## 布局



使用 [`st.sidebar`](<https://docs.streamlit.io/develop/api-reference/layout/st.sidebar>)，可以轻松把交互组件放入左侧侧边栏。传给 [`st.sidebar`](<https://docs.streamlit.io/develop/api-reference/layout/st.sidebar>) 的每个元素都会固定在左侧，让用户在仍可使用控制项的同时，专注于应用的主要内容。



例如，要把下拉框和滑块放在侧边栏中，请使用 `st.sidebar.slider`和 `st.sidebar.selectbox`，代替 `st.slider` 和 `st.selectbox`:



Python



```python
import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

```



除了侧边栏，Streamlit 还有其他几种控制应用布局的方式。[`st.columns`](<https://docs.streamlit.io/develop/api-reference/layout/st.columns>) 可以把交互组件并排放置，而 [`st.expander`](<https://docs.streamlit.io/develop/api-reference/layout/st.expander>) 可以折叠大段内容，从而节省空间。



Python



```python
import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

```



*●*

#### 说明



`st.echo`和 `st.spinner` 目前尚不支持放在侧边栏或布局选项中。我们正在努力增加这些支持，敬请放心！



### 显示进度



给应用加入耗时计算时，可以使用 [`st.progress()`](<https://docs.streamlit.io/develop/api-reference/status/st.progress>) 实时显示状态。



先导入 time。我们将用 `time.sleep()` 方法模拟耗时计算：



Python



```python
import time

```



现在创建一个进度条：



Python



```python
import streamlit as st
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

```



[*←*上一页：基础知识](<https://docs.streamlit.io/get-started/fundamentals>)[*→*下一页：进阶概念](<https://docs.streamlit.io/get-started/fundamentals/advanced-concepts>)



*?*

### 还有问题？



我们的[论坛](<https://discuss.streamlit.io>)中有丰富的实用信息，也有许多 Streamlit 专家。



> **AI 补充讲解：布局：把控制项和内容摆到合适的位置**
>
> 侧边栏（sidebar）适合放筛选项；分栏（columns）可以把内容并排放置；折叠区（expander）适合收起暂时不需要的细节。
>
> 什么时候用：页面内容变多，需要让主要结果更容易阅读时。
> 1. 把常用控制项放进 st.sidebar。
> 2. 用 st.columns 创建并排区域。
> 3. 在相应的 with 区域里写界面代码。
> 注意：布局改变显示位置，仍然需要理解脚本的运行顺序。



---

## 创建第一个应用

原文：[打开原文](<https://docs.streamlit.io/get-started/tutorials/create-an-app>)



# 创建应用



读到这里，你可能已经[安装了 Streamlit](<https://docs.streamlit.io/get-started/installation>)，并阅读了[基础概念](<https://docs.streamlit.io/get-started/fundamentals/main-concepts>)和[进阶概念](<https://docs.streamlit.io/get-started/fundamentals/advanced-concepts>)。如果还没有，现在正适合先看一看。



学习 Streamlit 最简单的方法，就是亲自动手。阅读本指南时，请逐个试用这些方法。只要应用正在运行，每次向脚本添加新元素并保存后，Streamlit 界面就会询问是否重新运行应用、查看变化。这样就能形成快速的交互循环：编写代码、保存、查看输出，再继续编写和调整，直到对结果满意。我们的目标是用 Streamlit 为你的数据或模型创建交互式应用，并在此过程中用它检查、调试、完善和分享代码。



本指南将使用 Streamlit 的核心功能创建一个交互式应用，探索纽约市 Uber 上下车记录的公开数据集。完成后，你将掌握获取与缓存数据、绘制图表、在地图上标记信息，以及通过滑块等交互组件筛选结果的方法。



*★*

#### 提示



如果想直接跳到完整结果，[下方提供了完整脚本](<https://docs.streamlit.io/get-started/tutorials/create-an-app#lets-put-it-all-together>).



## 创建第一个应用



Streamlit 不仅是创建数据应用的工具，也是创作者交流应用、分享想法并互相帮助改进作品的社区。欢迎加入社区论坛。我们期待听到你的问题和想法，也愿意帮助排查程序中的错误——现在就来看看吧！



1. 第一步，创建一个新的 Python 脚本。我们把它命名为 `uber_pickups.py`.
2. 打开 `uber_pickups.py`，使用你喜欢的 IDE 或文本编辑器，加入以下代码：
  
  
  
  
  Python
  
  
  
  ```python
  import streamlit as st
  import pandas as pd
  import numpy as np
  
  ```
3. 好的应用都需要标题，我们来添加一个：
  
  
  
  
  Python
  
  
  
  ```python
  st.title('Uber pickups in NYC')
  
  ```
4. 现在可以从命令行运行 Streamlit：
  
  
  
  
  终端
  
  
  
  ```bash
  streamlit run uber_pickups.py
  
  ```
  
  
  
  
  运行 Streamlit 应用与运行其他 Python 脚本类似。每次需要查看应用时，都可以使用这个命令。
  
  
  
  
  *★*
  
  #### 提示
  
  
  
  你知道吗？也可以向 `streamlit run` 传入 URL！与 GitHub Gists 配合使用尤其方便。例如：
  
  
  
  终端
  
  
  
  ```bash
  streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
  
  ```
5. 和往常一样，应用应当会自动在浏览器的新标签页中打开。



## 获取数据



现在已经有了应用，接下来需要获取纽约市 Uber 上下车记录的数据集。



1. 先编写一个加载数据的函数。将以下代码加入脚本：
  
  
  
  
  Python
  
  
  
  ```python
  DATE_COLUMN = 'date/time'
  DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
           'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
  
  def load_data(nrows):
      data = pd.read_csv(DATA_URL, nrows=nrows)
      lowercase = lambda x: str(x).lower()
      data.rename(lowercase, axis='columns', inplace=True)
      data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
      return data
  
  ```
  
  
  
  
  你会发现，`load_data` 是一个普通函数：它下载数据，将其放入 Pandas 数据表，并把日期列从文本转换为日期时间类型。这个函数接收一个参数（`nrows`），用于指定加载到数据表中的行数。
2. 现在测试函数并查看输出。在函数下面添加以下代码：
  
  
  
  
  Python
  
  
  
  ```python
  # Create a text element and let the reader know the data is loading.
  data_load_state = st.text('Loading data...')
  # Load 10,000 rows of data into the dataframe.
  data = load_data(10000)
  # Notify the reader that the data was successfully loaded.
  data_load_state.text('Loading data...done!')
  
  ```
  
  
  
  
  应用右上角会出现一些按钮，询问是否重新运行应用。选择 **Always rerun（始终重新运行）**，之后每次保存都能自动看到变化。



好吧，效果似乎没有那么惊艳……



事实证明，下载数据并将 10,000 行记录加载进数据表需要不少时间，把日期列转换为日期时间类型也不快。你肯定不希望应用每次更新都重新加载数据——幸运的是，Streamlit 可以缓存数据。



## 轻松使用缓存



1. 尝试添加 `@st.cache_data`，将它放在 `load_data` 声明之前：
  
  
  
  
  Python
  
  
  
  ```python
  @st.cache_data
  def load_data(nrows):
  
  ```
2. 接着保存脚本，Streamlit 会自动重新运行应用。因为这是首次使用 `@st.cache_data` 运行脚本，所以暂时看不出变化。我们再稍微调整文件，让你看到缓存的作用。
3. 把这一行 `data_load_state.text('Loading data...done!')` 替换为：
  
  
  
  
  Python
  
  
  
  ```python
  data_load_state.text("Done! (using st.cache_data)")
  
  ```
4. 现在保存。看到了吗，新增的文字立即出现了！退后一步想想，这确实很了不起：后台发生了一些神奇的事情，而你只用了一行代码就启用了它。



### 它是如何工作的？



我们花几分钟讨论 `@st.cache_data` 的实际工作方式。



给函数添加 Streamlit 缓存注解后，每次调用该函数，Streamlit 都会检查两项内容：



1. 调用函数时使用的输入参数。
2. 函数内部的代码。



如果 Streamlit 第一次遇到这两项内容以这些确定的值、这种组合出现，就会执行函数，并把结果存入本地缓存。下次调用时，如果两项内容都没有变化，Streamlit 就知道可以完全跳过函数执行，直接从本地缓存读取输出并返回给调用方——就像魔法一样。



你可能会想：“等一下，这听起来好得让人难以置信。它究竟有什么限制？”



确实有几个限制：



1. Streamlit 只会检查当前工作目录内的变化。如果升级了某个 Python 库，只有该库安装在工作目录中，Streamlit 的缓存才会注意到这一变化。
2. 如果函数不是确定性的（例如输出依赖随机数），或者从外部获取随时间变化的数据（例如实时股票行情服务），缓存并不会自动知道这些变化。
3. 最后，应当避免修改由 `st.cache_data` 缓存的函数输出，因为缓存值是按引用保存的。



虽然需要注意这些限制，但在很多情况下，它们都不会成为问题。这时，缓存会带来非常显著的改善。



*★*

#### 提示



如果代码中有耗时计算，可以考虑调整其组织方式，以便尽可能使用 `@st.cache_data`。更多细节请阅读[缓存](<https://docs.streamlit.io/develop/concepts/architecture/caching>)专题。



了解了 Streamlit 缓存的工作方式后，我们继续处理 Uber 上车记录。



> **AI 补充讲解：缓存：相同的数据工作尽量复用**
>
> 缓存（cache）会保存函数结果。官方教程把 st.cache\_data 放在数据加载函数上，减少应用重新运行时重复下载和处理相同数据。
>
> 什么时候用：读文件、下载数据或计算较慢，且希望复用结果时。
> 1. 把需要复用结果的工作整理成函数。
> 2. 在函数上方添加 @st.cache\_data。
> 3. 在页面中像调用普通函数一样调用它。
> 注意：首次调用仍需要实际计算；外部数据更新不一定改变函数参数，不能把缓存理解为自动实时同步。
> 注意：更完整的缓存失效和刷新规则应继续阅读缓存专题。
> 注意：版本核对：本教程原文中“缓存值按引用保存”的说明已照原文翻译；当前官方缓存专题说明 st.cache\_data 会返回副本，按引用共享资源的是 st.cache\_resource。实际使用请以当前缓存专题为准。
> [相关官方说明](<https://docs.streamlit.io/develop/concepts/architecture/caching>)



## 查看原始数据



先查看原始数据通常是个好习惯。我们给应用添加一个小标题，并显示原始数据：



Python



```python
st.subheader('Raw data')
st.write(data)

```



在[基础概念](<https://docs.streamlit.io/get-started/fundamentals/main-concepts>)指南中，你已经了解到 [`st.write`](<https://docs.streamlit.io/develop/api-reference/write-magic/st.write>) 几乎可以渲染任何传入的内容。这里传入的是数据表，因此它会被渲染为交互式表格。



[`st.write`](<https://docs.streamlit.io/develop/api-reference/write-magic/st.write>) 会根据输入的数据类型，尽量选择合适的展示方式。如果结果不符合预期，可以改用更具体的命令，例如 [`st.dataframe`](<https://docs.streamlit.io/develop/api-reference/data/st.dataframe>)。完整列表请参阅[API 参考](<https://docs.streamlit.io/develop/api-reference>).



## 绘制直方图



查看数据集并了解其内容后，我们再进一步，绘制直方图，看看纽约市 Uber 上车最繁忙的时段。



1. 首先，在原始数据部分下方添加一个小标题：
  
  
  
  
  Python
  
  
  
  ```python
  st.subheader('Number of pickups by hour')
  
  ```
2. 用 NumPy 生成一个按小时分组的上车时间直方图：
  
  
  
  
  Python
  
  
  
  ```python
  hist_values = np.histogram(
      data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
  
  ```
3. 然后，使用 Streamlit 的 [`st.bar_chart()`](<https://docs.streamlit.io/develop/api-reference/charts/st.bar_chart>) 方法绘制该直方图。
  
  
  
  
  Python
  
  
  
  ```python
  st.bar_chart(hist_values)
  
  ```
4. 保存脚本，直方图应立即显示在应用中。简单查看后可以发现，最繁忙的时间是 17:00，也就是下午 5 点。



这张图使用了 Streamlit 原生的 `bar_chart()` 方法，不过 Streamlit 也支持 Altair、Bokeh、Plotly、Matplotlib 等更复杂的图表库。完整列表请参阅[支持的图表库](<https://docs.streamlit.io/develop/api-reference/charts>).



## 在地图上绘制数据



Uber 数据的直方图让我们找到了最繁忙的上车时段，但如果想知道这些上车点集中在城市的哪些地方呢？虽然也可以用柱状图展示，但除非十分熟悉城市的经纬度，否则不容易理解。为了展示上车点的空间分布，我们使用 Streamlit 的 [`st.map()`](<https://docs.streamlit.io/develop/api-reference/charts/st.map>) 函数，把数据叠加到纽约市地图上。



1. 给这一部分添加一个小标题：
  
  
  
  
  Python
  
  
  
  ```python
  st.subheader('Map of all pickups')
  
  ```
2. 使用 `st.map()` 函数绘制数据：
  
  
  
  
  Python
  
  
  
  ```python
  st.map(data)
  
  ```
3. 保存脚本。这张地图可以交互，试着拖动或缩放一下。



前面的直方图表明，Uber 最繁忙的上车时段是 17:00。接下来重新绘制地图，只显示 17:00 上车点的分布。



1. 找到以下代码片段：
  
  
  
  
  Python
  
  
  
  ```python
  st.subheader('Map of all pickups')
  st.map(data)
  
  ```
2. 将其替换为：
  
  
  
  
  Python
  
  
  
  ```python
  hour_to_filter = 17
  filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
  st.subheader(f'Map of all pickups at {hour_to_filter}:00')
  st.map(filtered_data)
  
  ```
3. 你应当能立即看到数据更新。



绘制这张地图时，我们使用了 Streamlit 内置的 [`st.map`](<https://docs.streamlit.io/develop/api-reference/charts/st.map>) 函数。如果希望可视化更复杂的地图数据，建议进一步了解 [`st.pydeck_chart`](<https://docs.streamlit.io/develop/api-reference/charts/st.pydeck_chart>).



## 使用滑块筛选结果



上一节绘制地图时，筛选数据所用的时间被直接写在脚本中。如果希望读者实时选择筛选条件呢？Streamlit 的交互组件可以做到。我们用 `st.slider()` 方法给应用添加一个滑块。



1. 找到 `hour_to_filter`，将其替换为下面的代码：
  
  
  
  
  Python
  
  
  
  ```python
  hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
  
  ```
2. 操作滑块，观察地图如何实时更新。



> **AI 补充讲解：交互筛选：滑块选择条件，再显示筛选结果**
>
> 官方数据应用把小时滑块的返回值用于筛选数据，再刷新地图。核心顺序是：读输入、筛选数据、展示结果。
>
> 什么时候用：希望读者自己选择时间、类别或范围，查看不同结果时。
> 1. 先准备带小时和数值的示例数据。
> 2. 用 st.slider 得到选中的小时。
> 3. 用这个值筛选数据，再把结果交给展示函数。
> 注意：这里用本地小表解释流程，原文进一步用经纬度数据和 st.map 展示位置。



## 使用按钮切换数据显示



滑块只是动态改变应用内容的一种方式。我们使用 [`st.checkbox`](<https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox>) 函数再添加一个复选框，用它显示或隐藏应用顶部的原始数据表。



1. 找到以下代码行：
  
  
  
  
  Python
  
  
  
  ```python
  st.subheader('Raw data')
  st.write(data)
  
  ```
2. 将它们替换为以下代码：
  
  
  
  
  Python
  
  
  
  ```python
  if st.checkbox('Show raw data'):
      st.subheader('Raw data')
      st.write(data)
  
  ```



相信你已经有了自己的想法。完成本教程后，可以查看 Streamlit 提供的全部交互组件，详见[API 参考](<https://docs.streamlit.io/develop/api-reference>).



## 把所有内容组合起来



到这里，你已经完成了整个流程！下面是交互式应用的完整脚本。



*★*

#### 提示



如果你直接跳到了这里，创建脚本后，运行 Streamlit 的命令是 `streamlit run [app name]`.



Python



```python
import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)

```



## 分享应用



构建好 Streamlit 应用后，就可以分享它了！要向大家展示，可以使用 **Streamlit Community Cloud** 免费部署、管理并分享应用。



只需三个简单步骤：



1. 把应用放入公开的 GitHub 仓库，并确保仓库中包含 requirements.txt！
2. 登录 [share.streamlit.io](<https://share.streamlit.io>)
3. 点击“Deploy an app”（部署应用），然后粘贴 GitHub URL。



完成！🎈 现在你有了公开部署的应用，可以分享给所有人。点击链接，进一步了解[如何使用 Streamlit Community Cloud](<https://docs.streamlit.io/deploy/streamlit-community-cloud>).



## 获取帮助



入门内容到这里就结束了，你可以开始构建自己的应用了！如果遇到困难，可以尝试以下方式：



- 访问我们的[社区论坛](<https://discuss.streamlit.io/>)并发布问题。
- 通过命令行获取快速帮助：`streamlit help`
- 查阅[知识库](<https://docs.streamlit.io/knowledge-base>)，其中有技巧、分步教程，以及解答创建和部署 Streamlit 应用相关问题的文章。
- 继续阅读文档！例如：
  
  - [概念指南](<https://docs.streamlit.io/develop/concepts>)介绍缓存、主题和应用状态等内容。
  - [API 参考](<https://docs.streamlit.io/develop/api-reference>)提供每个 Streamlit 命令的示例。



[*←*上一页：动手实践](<https://docs.streamlit.io/get-started/tutorials>)[*→*下一页：创建多页面应用](<https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app>)



*?*

### 还有问题？



我们的[论坛](<https://discuss.streamlit.io>)中有丰富的实用信息，也有许多 Streamlit 专家。



---

## st.write

原文：[打开原文](<https://docs.streamlit.io/develop/api-reference/write-magic/st.write>)



## st.write



在应用中展示传入的参数。




它是 Streamlit 命令中的“瑞士军刀”：传入不同内容，就会执行不同的展示操作。与其他 Streamlit 命令相比，st.write() 有几个独特之处：




- 可以一次传入多个参数，它们都会显示出来。
- 具体行为取决于输入的数据类型。



| 函数签名[\[源代码\]](<https://github.com/streamlit/streamlit/blob/1.66.0/lib/streamlit/elements/write.py#L307>) |  |
| --- | --- |
| st.write(\*args, unsafe\_allow\_html=False) |  |
| 参数 |  |
| \*args<br>（任意类型） | 要在应用中显示的一个或多个对象。<br><br><br><br><br>| 类型 | 处理方式 |<br>| --- | --- |<br>| str | 使用 st.markdown(). |<br>| 类似数据表的对象、dict 或 list | 使用 st.dataframe(). |<br>| Exception | 使用 st.exception(). |<br>| 函数、模块或类 | 使用 st.help(). |<br>| DeltaGenerator | 使用 st.help(). |<br>| Altair 图表 | 使用 st.altair\_chart(). |<br>| Graphviz 图形 | 使用 st.graphviz\_chart(). |<br>| Keras 模型 | 转换模型并使用 st.graphviz\_chart(). |<br>| Matplotlib 图形 | 使用 st.pyplot(). |<br>| Plotly 图形 | 使用 st.plotly\_chart(). |<br>| PIL.Image | 使用 st.image(). |<br>| 生成器或流，例如 openai.Stream) | 使用 st.write\_stream(). |<br>| SymPy 表达式 | 使用 st.latex(). |<br>| 带有以下方法的对象：.\_repr\_html() | 使用 st.html(). |<br>| 数据库游标 | 以表格形式显示 DB API 2.0 游标的结果。 |<br>| 其他任意对象 | 将 str(arg) 显示为行内代码。 | |
| 类型 | 处理方式 |
| str | 使用 st.markdown(). |
| 类似数据表的对象、dict 或 list | 使用 st.dataframe(). |
| Exception | 使用 st.exception(). |
| 函数、模块或类 | 使用 st.help(). |
| DeltaGenerator | 使用 st.help(). |
| Altair 图表 | 使用 st.altair\_chart(). |
| Graphviz 图形 | 使用 st.graphviz\_chart(). |
| Keras 模型 | 转换模型并使用 st.graphviz\_chart(). |
| Matplotlib 图形 | 使用 st.pyplot(). |
| Plotly 图形 | 使用 st.plotly\_chart(). |
| PIL.Image | 使用 st.image(). |
| 生成器或流，例如 openai.Stream) | 使用 st.write\_stream(). |
| SymPy 表达式 | 使用 st.latex(). |
| 带有以下方法的对象：.\_repr\_html() | 使用 st.html(). |
| 数据库游标 | 以表格形式显示 DB API 2.0 游标的结果。 |
| 其他任意对象 | 将 str(arg) 显示为行内代码。 |
| unsafe\_allow\_html<br>（布尔值） | 是否渲染 \*args 中的 HTML。此设置仅作用于字符串，或回退到 \_repr\_html\_() 的对象。如果设置为 False（默认），body 中的 HTML 标签会被转义，并作为原始文本显示。如果设置为 True，则 body 中的 HTML 表达式会被渲染。<br><br><br><br><br>给应用添加自定义 HTML 会影响安全性、样式和可维护性。不要使用 unsafe\_allow\_html 来重新构造界面或注入 CSS，应优先使用 Streamlit 原生功能和主题。如果需要不经过 Markdown 的 HTML 或 CSS，请使用 st.html. |



#### 示例



最基本的用法，是在输入为字符串时，绘制 Markdown 格式的文本：




```

import streamlit as st

st.write("Hello, *World!* :sunglasses:")

```




[交互式演示（打开在线页面）](<https://doc-write1.streamlit.app/~/+//?embed=true&&embed_options=light_theme&>)

[使用 Streamlit 构建 🎈](<https://streamlit.io>)



[全屏 *↗*](<https://doc-write1.streamlit.app//?utm_medium=oembed&>)



如前所述，st.write() 也接受数字、数据表、设置过样式的数据表和其他各种对象等数据形式：




```

import streamlit as st
import pandas as pd

st.write(1234)
st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)

```




[交互式演示（打开在线页面）](<https://doc-write2.streamlit.app/~/+//?embed=true&&embed_options=light_theme&>)

[使用 Streamlit 构建 🎈](<https://streamlit.io>)



[全屏 *↗*](<https://doc-write2.streamlit.app//?utm_medium=oembed&>)



最后，还可以传入多个参数，例如：




```

import streamlit as st

st.write("1 + 1 = ", 2)
st.write("Below is a DataFrame:", data_frame, "Above is a dataframe.")

```




[交互式演示（打开在线页面）](<https://doc-write3.streamlit.app/~/+//?embed=true&&embed_options=light_theme&>)

[使用 Streamlit 构建 🎈](<https://streamlit.io>)



[全屏 *↗*](<https://doc-write3.streamlit.app//?utm_medium=oembed&>)



还有一点：st.write 也接受图表对象！例如：




```

import altair as alt
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((200, 3)), columns=["a", "b", "c"])
chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(chart)

```




[交互式演示（打开在线页面）](<https://doc-vega-lite-chart.streamlit.app/~/+//?embed=true&&embed_options=light_theme&>)

[使用 Streamlit 构建 🎈](<https://streamlit.io>)



[全屏 *↗*](<https://doc-vega-lite-chart.streamlit.app//?utm_medium=oembed&>)



### 精选视频



了解 [`st.write`](<https://docs.streamlit.io/develop/api-reference/write-magic/st.write>) 和 [自动显示](<https://docs.streamlit.io/develop/api-reference/write-magic/magic>)命令的含义及使用方式。



[交互式演示（打开在线页面）](<https://www.youtube-nocookie.com/embed/wpDuY9I2fDg?playlist=wpDuY9I2fDg&rel=0&start=undefined&end=undefined&autoplay=undefined&loop=undefined&mute=0>)



*★*

#### 提示



希望 `st.write` 增加新功能，或者发现了错误？可以查看[尚未关闭的问题](<https://github.com/streamlit/streamlit/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22feature%3Ast.write%22%20sort%3Areactions-%2B1-desc>)，在你关心的问题的首条帖子上点击 👍。你的投票能帮助我们决定接下来优先处理哪些工作。



[*←*上一页：输出与自动显示](<https://docs.streamlit.io/develop/api-reference/write-magic>)[*→*下一页：st.write\_stream](<https://docs.streamlit.io/develop/api-reference/write-magic/st.write_stream>)



*?*

### 还有问题？



我们的[论坛](<https://discuss.streamlit.io>)中有丰富的实用信息，也有许多 Streamlit 专家。



> **AI 补充讲解：st.write：一个入口展示多种对象**
>
> st.write 会根据传入对象的类型选择展示方式：字符串按 Markdown 展示，数据表按表格展示，还能接收多种图表对象。
>
> 什么时候用：想先把文字、变量或分析结果展示出来时。
> 1. 先 import streamlit as st。
> 2. 把需要观察的值传给 st.write。
> 3. 可以传多个参数；想精确控制样式时，再查对应的专用显示函数。
> 注意：函数会按输入类型选择行为，并不是把所有对象都当普通字符串输出。



---

## st.button

原文：[打开原文](<https://docs.streamlit.io/develop/api-reference/widgets/st.button>)



## st.button



显示一个按钮交互组件。



| 函数签名[\[源代码\]](<https://github.com/streamlit/streamlit/blob/1.66.0/lib/streamlit/elements/widgets/button.py#L138>) |  |
| --- | --- |
| st.button(label, key=None, help=None, on\_click=None, args=None, kwargs=None, \*, type="secondary", icon=None, icon\_position="left", disabled=False, use\_container\_width=None, width="content", shortcut=None, wrap=None) |  |
| 参数 |  |
| label<br>（字符串） | 简短标签，用来向用户说明按钮的用途。标签可包含以下 GitHub 风格 Markdown：粗体、斜体、删除线、行内代码、链接和图片。图片会像图标一样显示，最大高度等于字体高度。<br><br><br><br><br>不支持的 Markdown 元素会被去除外层标记，仅保留其中的文本。标题、列表、引用等常见块级 Markdown 会被自动转义，并在标签中显示为原始文本。<br><br><br><br><br>关于 body 参数所支持的其他 Markdown 指令，请参阅 [st.markdown](<https://docs.streamlit.io/develop/api-reference/text/st.markdown>)。 |
| key<br>（字符串、整数或 None） | 可选的字符串或整数，用作该交互组件的唯一键。如果设置为 None（默认），系统会根据其他参数的值生成一个键。两个组件不能使用相同的键。指定 key 可以稳定组件身份，即使其他参数变化，也能在重新运行时保留状态。<br><br><br><br><br>设置 key 后，可通过 st.session\_state\[key\] 访问组件的值（只读）。更多细节请参阅[交互组件的行为](<https://docs.streamlit.io/develop/concepts/architecture/widget-behavior>).<br><br><br><br><br>此外，如果提供了 key，它还会成为一个带有以下前缀的 CSS 类名：st-key-. |
| help<br>（字符串或 None） | 鼠标悬停在按钮上时显示的提示文字。如果设置为 None（默认），则不显示提示。<br><br><br><br><br>提示文字可包含 GitHub 风格 Markdown，包括 body 参数描述的指令；该参数属于 st.markdown. |
| on\_click<br>（可调用对象） | 可选的回调函数，点击按钮时调用。 |
| args<br>（列表或元组） | 可选的列表或元组，用来向回调函数传递位置参数。 |
| kwargs<br>（字典） | 可选字典，用来向回调函数传递关键字参数。 |
| type<br>（"primary"、"secondary" 或 "tertiary"） | 可选字符串，用于指定按钮类型，可取以下值：<br><br><br><br><br>- "primary"：按钮背景采用应用主色，使其更加醒目。<br>- "secondary"（默认）：按钮背景与应用背景协调，提供普通程度的强调。<br>- "tertiary"：按钮显示为纯文本，没有边框或背景，视觉上更轻。 |
| icon<br>（字符串或 None） | 可选的表情或图标，显示在按钮标签旁。如果 icon 为 None（默认），则不显示图标。如果 icon 是字符串，可使用以下选项：<br><br><br><br><br>- 单个字符的表情。例如，可以设置 icon="🚨" 或 icon="🔥"。不支持表情短代码。<br>- Material Symbols 图标库中的圆角样式图标，格式为 ":material/icon\_name:"，其中“icon\_name”是采用下划线命名法的图标名称。<br>  <br>  <br>  <br>  <br>  例如，icon=":material/thumb\_up:" 会显示点赞图标。更多图标请查阅 [Material Symbols ](<https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded>)字体库。<br>- "spinner"：显示加载旋转指示器。 |
| icon\_position<br>（"left" 或 "right"） | 图标相对于按钮标签的位置，默认是 "left". |
| disabled<br>（布尔值） | 可选布尔值。设置为 True 时禁用按钮。默认值为 False. |
| use\_container\_width<br>（布尔值） | use\_container\_width 已弃用，将在未来版本中移除。对于 use\_container\_width=True，请使用 width="stretch"。对于 use\_container\_width=False，请使用 width="content".<br><br><br><br><br>是否扩展按钮宽度以填满父容器。如果 use\_container\_width 为 False（默认），Streamlit 会按内容调整按钮宽度。如果 use\_container\_width 为 True，按钮宽度会与父容器一致。<br><br><br><br><br>无论哪种情况，当按钮内容宽于父容器时，内容都会换行。 |
| width<br>（"content"、"stretch" 或整数） | 按钮宽度，可以使用以下值：<br><br><br><br><br>- "content"（默认）：按钮宽度与内容宽度一致，但不超过父容器宽度。<br>- "stretch"：按钮宽度与父容器宽度一致。<br>- 用整数指定像素宽度：按钮具有固定宽度。如果指定宽度大于父容器宽度，按钮会改为与父容器等宽。 |
| shortcut<br>（字符串或 None） | 可选的键盘快捷键，用于触发按钮。可使用以下字符串：<br><br><br><br><br>- 单个字母或数字键，例如 "K" 或 "4".<br>- 功能键，例如 "F11".<br>- 特殊键，例如 "Enter", "Esc" 或 "Tab".<br>- 上述按键与修饰键的组合。例如，可以使用 "Ctrl+K" 或 "Cmd+Shift+O".<br><br><br><br><br>重要<br><br><br><br><br>按键 "C" 和 "R" 为保留键，即使加上修饰键也不能使用。目前也不支持以下标点键："." 和 ","。某些组合键，例如 "Ctrl+T", "Ctrl+W", "Ctrl+PageUp",<br>"Ctrl+PageDown" 和 "F11"，由浏览器或操作系统保留，可能无法传递到 Streamlit。<br><br><br><br><br>支持的特殊键包括：Backspace、Delete、Down、End、Enter、Esc、Home、Left、PageDown、PageUp、Right、Space、Tab 和 Up。<br><br><br><br><br>支持的修饰键包括：Alt、Ctrl、Cmd、Meta、Mod、Option 和 Shift。<br><br><br><br><br>- Ctrl、Cmd、Meta 和 Mod 可互换使用，显示给用户时会匹配其所在平台。<br>- Option 和 Alt 可互换使用，显示给用户时会匹配其所在平台。 |
| wrap<br>（布尔值或 None） | 是否允许按钮标签换成多行，可以使用以下值：<br><br><br><br><br>- None（默认）：Streamlit 根据周围布局决定。在水平容器中，或直接位于一列中且未嵌套于其他容器时，按钮维持标准的单行高度，超长标签用省略号截断；其他布局中，标签会换行显示。<br>- True：如果标签太宽，就换成多行，按钮相应增高。<br>- False：按钮保持标准单行高度；标签太宽时用省略号截断。<br><br><br><br><br>单行标签被省略号截断，且未设置 help 时，鼠标悬停会显示完整标签。图标和键盘快捷键始终可见。 |
| 返回值 |  |
| （布尔值） | 如果按钮在应用上一次运行时被点击，则返回 True；否则返回 False。 |



#### 示例



**示例 1：自定义按钮类型**




```

import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")

```




[交互式演示（打开在线页面）](<https://doc-buton.streamlit.app/~/+//?embed=true&&embed_options=light_theme&>)

[使用 Streamlit 构建 🎈](<https://streamlit.io>)



[全屏 *↗*](<https://doc-buton.streamlit.app//?utm_medium=oembed&>)



**示例 2：给按钮添加图标**




虽然可以通过 Markdown 给按钮添加图标，但 icon 参数提供了更方便且一致的替代方式。




```

import streamlit as st

left, middle, right = st.columns(3)
if left.button("Plain button", width="stretch"):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", width="stretch"):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", width="stretch"):
    right.markdown("You clicked the Material button.")

```




[交互式演示（打开在线页面）](<https://doc-button-icons.streamlit.app/~/+//?embed=true&&embed_options=light_theme&>)

[使用 Streamlit 构建 🎈](<https://streamlit.io>)



[全屏 *↗*](<https://doc-button-icons.streamlit.app//?utm_medium=oembed&>)



**示例 3：使用键盘快捷键**




下面的示例展示如何通过快捷键触发按钮。如果使用 Ctrl、Cmd 或 Mod 等与平台相关的修饰键，它们会按等价方式解释，展示时也总会匹配用户平台。




```

import streamlit as st

with st.container(horizontal=True, horizontal_alignment="distribute"):
    "`A`" if st.button("A", shortcut="A") else "` `"
    "`S`" if st.button("S", shortcut="Ctrl+S") else "` `"
    "`D`" if st.button("D", shortcut="Cmd+Shift+D") else "` `"
    "`F`" if st.button("F", shortcut="Mod+Alt+Shift+F") else "` `"

```




[交互式演示（打开在线页面）](<https://doc-button-shortcuts.streamlit.app/~/+//?embed=true&&embed_options=light_theme&>)

[使用 Streamlit 构建 🎈](<https://streamlit.io>)



[全屏 *↗*](<https://doc-button-shortcuts.streamlit.app//?utm_medium=oembed&>)



### 进阶功能



虽然按钮是最简单的输入组件，但实际应用中，它常常与 [`st.session_state`](<https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state>) 密切关联。请进一步阅读我们的进阶指南：[按钮行为与示例](<https://docs.streamlit.io/develop/concepts/design/buttons>).



### 精选视频



观看视频，了解 Streamlit 核心函数之一——按钮——的使用方式！



[交互式演示（打开在线页面）](<https://www.youtube-nocookie.com/embed/JSeQSnGovSE?playlist=JSeQSnGovSE&rel=0&start=undefined&end=undefined&autoplay=undefined&loop=undefined&mute=0>)



下面的视频会更进一步，介绍如何组合使用[按钮](<https://docs.streamlit.io/develop/api-reference/widgets/st.button>), [复选框](<https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox>) 和 [单选按钮](<https://docs.streamlit.io/develop/api-reference/widgets/st.radio>)!



[交互式演示（打开在线页面）](<https://www.youtube-nocookie.com/embed/EnXJBsCIl_A?playlist=EnXJBsCIl_A&rel=0&start=undefined&end=undefined&autoplay=undefined&loop=undefined&mute=0>)



*★*

#### 提示



希望 `st.button` 增加新功能，或者发现了错误？可以查看[尚未关闭的问题](<https://github.com/streamlit/streamlit/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22feature%3Ast.button%22%20sort%3Areactions-%2B1-desc>)，在你关心的问题的首条帖子上点击 👍。你的投票能帮助我们决定接下来优先处理哪些工作。



[*←*上一页：输入组件](<https://docs.streamlit.io/develop/api-reference/widgets>)[*→*下一页：st.download\_button](<https://docs.streamlit.io/develop/api-reference/widgets/st.download_button>)



*?*

### 还有问题？



我们的[论坛](<https://discuss.streamlit.io>)中有丰富的实用信息，也有许多 Streamlit 专家。



> **AI 补充讲解：st.button：点击后触发一次操作**
>
> 按钮返回布尔值：在点击触发的那次运行中为 True，其他时候为 False。用 if 语句包住需要触发的操作，就能让它响应点击。
>
> 什么时候用：需要让用户主动执行一次计算、显示提示或开始某个操作时。
> 1. 创建按钮，并写清楚按钮标签。
> 2. 用 if st.button(...) 判断本次是否点击。
> 3. 把需要触发的代码缩进到判断中。
> 注意：按钮返回值不是永久开启的开关。需要持续保存状态时，再阅读会话状态专题。



## 中英术语对照

- virtual environment：虚拟环境
- widget：交互组件
- rerun：重新运行
- DataFrame：数据表
- cache：缓存
- Session State：会话状态
- callback：回调函数
- sidebar：侧边栏
- Markdown：轻量文本标记语法
