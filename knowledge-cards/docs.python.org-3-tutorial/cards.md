# Python 中文文档

2026-10-17 读取 Python 官方教程的入门介绍页，用于验证其他文档站点。仅整理这一个页面，不代表 Python 全站目录或全部内容。


---

## Python 入门介绍

原文：[打开原文](<https://docs.python.org/3/tutorial/introduction.html>)



# 3. Python 非正式入门



在下面的示例中，通过有无提示符（[&gt;&gt;&gt;](<https://docs.python.org/3/glossary.html#term-0>)和[…](<https://docs.python.org/3/glossary.html#term-...>)）来区分输入与输出。重现示例时，只需输入提示符之后的内容；不以提示符开头的行，是解释器输出。请注意，示例中次级提示符独占一行时，表示需要输入一个空行，以结束多行命令。



可以使用“Copy”（复制）按钮：鼠标悬停或点击代码示例时，按钮会显示在右上角。它会去掉提示符并省略输出，便于把输入代码复制到解释器中。



本手册中的许多示例，包括在交互提示符下输入的示例，都带有注释。Python 注释以井号 `#` 开始，直到当前物理行结束。注释可以位于行首，也可以跟在空白或代码后面，但字符串字面量内部不算注释。字符串里的井号只是普通字符。注释用于解释代码，不会被 Python 执行，输入示例时可以省略。



下面是一些示例：



```
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

```



## 3.1. 把 Python 当作计算器




先试几个简单的 Python 命令。启动解释器，等待主提示符 `>>>` 出现，通常很快就会看到。




### 3.1.1. 数字




解释器就像一个简单的计算器：输入表达式，它就会输出计算结果。表达式的语法很直接，可以使用运算符 `+`, `-`, `*`和`/` 进行算术运算，并使用括号（`()`）分组。例如：




```
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating-point number
1.6

```




整数，例如 `2`, `4`, `20`，其类型为 [`int`](<https://docs.python.org/3/builtins/functions.html#int>)；带有小数部分的数，例如 `5.0`, `1.6`，其类型为 [`float`](<https://docs.python.org/3/builtins/functions.html#float>)。本教程后面会继续介绍数值类型。




除法（`/`）总是返回浮点数。若要进行[向下取整除法](<https://docs.python.org/3/glossary.html#term-floor-division>)并得到整数结果，可以使用 `//` 运算符；计算余数则使用 `%`:




```
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # floored quotient * divisor + remainder
17

```




在 Python 中，可以使用 `**` 运算符计算幂 [\[1\]](<https://docs.python.org/3/tutorial/introduction.html#id3>):




```
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128

```




等号（`=`）用于给变量赋值。赋值之后，在出现下一个交互提示符之前，不会显示计算结果：




```
>>> width = 20
>>> height = 5 * 9
>>> width * height
900

```




如果变量尚未“定义”（即尚未赋值），尝试使用它就会报错：




```
>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined

```




Python 完整支持浮点运算。对于混合类型的操作数，运算时会把整数操作数转换为浮点数：




```
>>> 4 * 3.75 - 1
14.0

```




在交互模式中，上一次输出的表达式结果会赋给变量 `_`。因此，把 Python 当作桌面计算器时，继续计算会更方便。例如：




```
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06

```




用户应将这个变量视为只读。不要显式给它赋值，否则会创建一个同名的独立局部变量，遮蔽这个具有特殊行为的内置变量。




除了 [`int`](<https://docs.python.org/3/builtins/functions.html#int>)和[`float`](<https://docs.python.org/3/builtins/functions.html#float>)，Python 也支持其他数值类型，例如 [`Decimal`](<https://docs.python.org/3/library/decimal.html#decimal.Decimal>)和[`Fraction`](<https://docs.python.org/3/library/fractions.html#fractions.Fraction>)。Python 还内置支持[复数](<https://docs.python.org/3/builtins/stdtypes.html#typesnumeric>)，用 `j` 或 `J` 后缀表示虚部，例如 `3+5j`).




### 3.1.2. 文本




Python 不仅可以处理数字，还可以处理文本。文本使用 [`str`](<https://docs.python.org/3/builtins/stdtypes.html#str>) 类型表示，也称为“字符串”，它可以包含字符“`!`”、单词“`rabbit`”、名字“`Paris`”、句子“`Got your back.`”等。“`Yay! :)`”也属于文本。它们可以放在单引号（`'...'`）或双引号（`"..."`）中，效果相同 [\[2\]](<https://docs.python.org/3/tutorial/introduction.html#id4>).




```
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> "Paris rabbit got your back :)! Yay!"  # double quotes
'Paris rabbit got your back :)! Yay!'
>>> '1975'  # digits and numerals enclosed in quotes are also strings
'1975'

```




要在文本中包含引号，需要在前面加上 `\` 对它进行“转义”；也可以改用另一种引号：




```
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'

```




在 Python 交互环境中，字符串的定义形式与输出形式可能不同。[`print()`](<https://docs.python.org/3/builtins/functions.html#print>) 函数会去掉外层引号，并正确输出转义字符和特殊字符，从而得到更容易阅读的结果：




```
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), special characters are included in the string
'First line.\nSecond line.'
>>> print(s)  # with print(), special characters are interpreted, so \n produces new line
First line.
Second line.

```




如果不希望以 `\` 开头的字符被解释为特殊字符，可以使用*原始字符串*：在第一个引号前加上 `r` 即可。




```
>>> print('C:\this\name')  # here \t means tab, \n means newline
C:      his
ame
>>> print(r'C:\this\name')  # note the r before the quote
C:\this\name

```




原始字符串有一个细节需要注意：它不能以奇数个 `\` 字符结尾。更多信息及处理方法，请参阅[常见问题中的相关条目](<https://docs.python.org/3/faq/programming.html#faq-programming-raw-string-backslash>)。




字符串字面量可以跨越多行。一种写法是使用三引号：`"""..."""` 或 `'''...'''`。换行符会自动包含在字符串中；不过，可以在行尾加上 `\` 来避免包含换行符。下面的示例不会包含开头的换行：




```
>>> print("""\
... Usage: thingy [OPTIONS]
...      -h                        Display this usage message
...      -H hostname               Hostname to connect to
... """)
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to

>>>

```




字符串可以通过 `+` 运算符连接，也可以通过以下运算符重复：`*`:




```
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'

```




两个或多个相邻的*字符串字面量*，即由引号包围的文本，会自动连接起来。




```
>>> 'Py' 'thon'
'Python'

```




需要将长字符串拆开书写时，这个功能尤其有用：




```
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'

```




不过，它只适用于两个字面量，不适用于变量或表达式：




```
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
           ^^^^^^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
               ^^^^^
SyntaxError: invalid syntax

```




如果需要连接变量，或连接变量和字面量，请使用 `+`:




```
>>> prefix + 'thon'
'Python'

```




字符串支持*索引*（下标），第一个字符的索引为 0。Python 没有单独的字符类型，一个字符就是长度为 1 的字符串：




```
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'

```




索引也可以是负数，表示从右侧开始计数：




```
>>> word[-1]  # last character
'n'
>>> word[-2]  # second-last character
'o'
>>> word[-6]
'P'

```




注意，因为 -0 与 0 相同，所以负索引从 -1 开始。




除了索引，也支持*切片*。索引用于获取单个字符，而*切片*可以获取子字符串：




```
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'

```




切片索引具有实用的默认值：省略起点时，默认从 0 开始；省略终点时，默认到字符串长度对应的位置结束。




```
>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]   # characters from position 4 (included) to the end
'on'
>>> word[-2:]  # characters from the second-last (included) to the end
'on'

```




注意，切片始终包含起点，不包含终点。这样就能保证 `s[:i] + s[i:]` 总是等于 `s`:




```
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'

```




记忆切片的一种方法，是将索引理解为指向字符*之间*的位置：第一个字符左侧边界编号为 0。那么，一个长度为 *n* 的字符串，最后一个字符右侧边界的编号就是 *n*。例如：




```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

```




第一排数字表示字符串中从 0 到 6 的边界位置，第二排表示对应的负索引。从 *i* 到 *j* 的切片，包含标为 *i*和*j* 的两条边界之间的所有字符。




对于非负索引，只要两个索引都在范围内，切片长度就是它们的差。例如，`word[1:3]` 的长度为 2。




尝试使用过大的索引，会导致错误：




```
>>> word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

```




不过，切片能够妥善处理超出范围的索引：




```
>>> word[4:42]
'on'
>>> word[42:]
''

```




Python 字符串不能被修改，因为它们是[不可变的](<https://docs.python.org/3/glossary.html#term-immutable>)。因此，给字符串的某个索引位置赋值会报错：




```
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

```




如果需要不同的字符串，应当创建一个新字符串：




```
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'

```




内置函数 [`len()`](<https://docs.python.org/3/builtins/functions.html#len>) 返回字符串长度：




```
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34

```




另请参阅




[文本序列类型——str](<https://docs.python.org/3/builtins/stdtypes.html#textseq>)



字符串属于*序列类型*，支持这类类型共有的常见操作。





[字符串方法](<https://docs.python.org/3/builtins/stdtypes.html#string-methods>)



字符串提供了大量用于基本转换和查找的方法。





[f 字符串](<https://docs.python.org/3/reference/lexical_analysis.html#f-strings>)



在字符串字面量中嵌入表达式。





[格式化字符串语法](<https://docs.python.org/3/library/string.html#formatstrings>)



关于使用下列方法进行字符串格式化的信息：[`str.format()`](<https://docs.python.org/3/builtins/stdtypes.html#str.format>).





[printf 风格的字符串格式化](<https://docs.python.org/3/builtins/stdtypes.html#old-string-formatting>)



字符串位于 `%` 运算符左侧时所使用的旧式格式化操作，详见此处。




### 3.1.3. 列表




Python 有多种*复合*数据类型，用来将其他值组合起来。其中最通用的是*列表*：把用逗号分隔的值（元素）放在方括号中即可。列表可以包含不同类型的元素，但通常其中的元素都具有相同类型。




```
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]

```




和字符串及其他内置[序列](<https://docs.python.org/3/glossary.html#term-sequence>)类型一样，列表也可以使用索引和切片：




```
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]

```




列表也支持连接等操作：




```
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

```




字符串是[不可变的](<https://docs.python.org/3/glossary.html#term-immutable>)，而列表属于[可变](<https://docs.python.org/3/glossary.html#term-mutable>)类型，也就是说，可以修改它的内容：




```
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]

```




也可以使用 [`list.append()`](<https://docs.python.org/3/builtins/stdtypes.html#list.append>) *方法*在列表末尾添加新元素。稍后还会进一步介绍方法。




```
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]

```




Python 中的简单赋值永远不会复制数据。把列表赋给变量时，变量引用的是*现有列表*。通过某个变量对列表所做的修改，也会被其他引用同一列表的变量看到：




```
>>> rgb = ["Red", "Green", "Blue"]
>>> rgba = rgb
>>> id(rgb) == id(rgba)  # they reference the same object
True
>>> rgba.append("Alph")
>>> rgb
["Red", "Green", "Blue", "Alph"]

```




所有切片操作都会返回包含指定元素的新列表。因此，下面的切片会返回列表的[浅复制](<https://docs.python.org/3/library/copy.html#shallow-vs-deep-copy>)：




```
>>> correct_rgba = rgba[:]
>>> correct_rgba[-1] = "Alpha"
>>> correct_rgba
["Red", "Green", "Blue", "Alpha"]
>>> rgba
["Red", "Green", "Blue", "Alph"]

```




也可以给切片赋值，甚至由此改变列表长度，或将列表彻底清空：




```
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]

```




内置函数 [`len()`](<https://docs.python.org/3/builtins/functions.html#len>) 同样适用于列表：




```
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4

```




列表可以嵌套，也就是创建包含其他列表的列表。例如：




```
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'

```



> **AI 补充讲解：用 Python 做计算**
>
> 整数（int）与浮点数（float）可以直接参与算术运算。普通除法 / 与整除 // 的结果含义不同。
>
> 什么时候用：先熟悉表达式，再写数据处理代码时。
> 1. 用 print 显示运算结果。
> 2. 观察 /、// 和 % 分别得到商、向下取整的商与余数。
> 注意：// 是向下取整，不能简单理解为所有情况下都截掉小数。



## 3.2. 迈出编程的第一步




当然，Python 不只能完成简单加法，还可以处理更复杂的任务。例如，可以编写如下代码，生成[斐波那契数列](<https://en.wikipedia.org/wiki/Fibonacci_sequence>)的开头一段：




```
>>> # Fibonacci series:
>>> # the sum of two elements defines the next
>>> a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8

```




这个示例引入了几个新特性。




- 第一行包含*多重赋值*：变量 `a`和`b` 同时分别得到新值 0 和 1。最后一行再次使用这一方式，展示了一个规则：任何赋值发生之前，右侧的表达式都会先完成求值；这些表达式按从左到右的顺序求值。
- [`while`](<https://docs.python.org/3/reference/compound_stmts.html#while>) 循环会在条件（这里是 `a < 10`）为真时持续执行。与 C 一样，在 Python 中，任何非零整数都为真，零为假。条件也可以是字符串、列表或任意序列：长度非零时为真，空序列为假。本示例使用简单的比较作为判断。标准比较运算符的写法与 C 一样：`<`（小于）、`>`（大于）、`==`（等于）、`<=`（小于或等于）、`>=`（大于或等于）以及 `!=`（不等于）。
- *循环体*需要使用*缩进*：缩进是 Python 对语句进行分组的方式。在交互提示符下，每一行缩进都需要输入制表符或空格。实际工作中，较复杂的 Python 程序通常在文本编辑器中编写，常见编辑器都支持自动缩进。在交互模式中输入复合语句后，需要再输入一个空行表示结束，因为解析器无法判断你是否已经写完最后一行。注意，同一个基本代码块中的各行必须使用相同的缩进量。
- [`print()`](<https://docs.python.org/3/builtins/functions.html#print>) 函数会输出传入的参数值。与直接输入表达式不同，它在处理多个参数、浮点数和字符串时有专门的显示行为：打印字符串时不带引号，各项之间插入空格，因此可以方便地格式化输出，例如：
  
  
  
  
  ```
  >>> i = 256*256
  >>> print('The value of i is', i)
  The value of i is 65536
  
  ```
  
  
  
  
  关键字参数 *end* 可以取消输出后的换行，或把结尾替换成其他字符串：
  
  
  
  
  ```
  >>> a, b = 0, 1
  >>> while a < 1000:
  ...     print(a, end=',')
  ...     a, b = b, a+b
  ...
  0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
  
  ```




脚注




\[[1](<https://docs.python.org/3/tutorial/introduction.html#id1>)\]


因为 `**` 的优先级高于 `-`, `-3**2`，所以会被解释为 `-(3**2)`，得到的结果是 `-9`。如果希望得到 `9`，可以使用 `(-3)**2`.




\[[2](<https://docs.python.org/3/tutorial/introduction.html#id2>)\]


与其他语言不同，`\n` 等特殊字符放在单引号（`'...'`）和双引号（`"..."`）中时，含义相同。两者唯一的区别是：在单引号内部，不需要转义 `"`，但必须转义 `\'`；双引号内部则相反。



> **AI 补充讲解：while：条件成立时重复执行**
>
> while 会反复检查条件，并执行缩进的代码块。循环体中需要更新相关变量，让循环最终有机会结束。
>
> 什么时候用：需要按条件重复处理，而不是只执行一次时。
> 1. 先给变量设置初始值。
> 2. 编写 while 条件，并缩进循环体。
> 3. 在循环体中更新变量。
> 注意：同一代码块的缩进需要保持一致。



## 中英术语对照

- integer：整数
- float：浮点数
- string：字符串
- list：列表
- slice：切片
- while loop：while 循环
