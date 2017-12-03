# python3标准库-re

python-re模块，效率比str自带的方法低，但是功能强大。可以直接调用来实现正则匹配进行“查找”，“替换”，“分组”，“匹配”等。正则表达式模式被编译成一系列的字节码，然后由用C编写的匹配引擎执行。使用它最好的方式是使用”原字符r",并且需要对所有特殊字符进行分类方便记忆，可以参考文章的"元字符分类“，比如分组字符，特殊控制字符等。并且注意使用过程的”几条潜规则“，比如'\'字符进行转义，‘[]’字符的作用。及“贪婪”与“非贪婪”模式做区别，默认是使用“贪婪”模式的。再掌握常用的函数方法加上不断的实践，肯定能够对“正则处理”有较深的认识。

### 元字符分类
- 一般字符： `.` `\` `[]`
- 空白字符： `\b\r\n\f\s`
- 预定义单字符： `\d\D\s\S\w\W`
- 锚字符： `^` `$` `\b\B` `\A\Z`
- 重复字符： `*` `+` `?` `{m}` `{n,}` `{n,m}` `{,m}`
- 分组字符： `|` `()` `(?P<name>` `\number` `(?P=name)`
- 不分组字符： `(?:...)` `(?iLmsux)` `(?#...)` `(?=...)` `(?!...)` `(?<=...)` `(?<!...)` `(?(id/name)yes-pattern|no-pattern)`
- 特殊控制： re.M, re.I, re.G, ?

### 模块函数
- re.compile(pattern, flags=0)
- re.search(pattern, string, flags=0)
- re.match(pattern, string, flags=0)
- re.fullmatch(pattern, string, flags=0)
- re.split(pattern, string, maxsplit=0, flags=0)
- re.findall(pattern, string, flags=0)
- re.finditer(pattern, string, flags=0)
- re.sub(pattern, repl, string, count=0, flags=0)
- re.subn(pattern, repl, string, count=0, flags=0)
- re.escape(string)
- re.purge()
- re.A, re.ASCII, re.DEBUG, re.I, re.IGNORECASE, re.L, re.LOCALE, re.M, re.MULTILTNE, re.S, re.DOTALL, re.X, re.VERBOSE

### 编译后的正则表达式对象also
- regex.search(string[, pos[, endpos]])...

### 匹配对象
- m.expand(template)
- m.group([group1, ...])
- m.\_\_getitem\_\_(g)
- m.groups(default=None)
- m.groupdict(default=None)
- m.start([group])
- m.end([group])
- m.span([group])
- m.pos
- m.endpos
- m.lastindex
- m.lastgroup
- m.re
- m.string

### 几条规则
- 推荐使用原生字符串(如：r'\d' <==> '\\d' )
- '|' 的优先级很低，(?:...)一般使用于 '|' 或者接数量词,要匹配字面 '|'，请使用 \|，或将其放在字符类中，如在 [|] 中。
- +,`*`,?默认使用贪婪模式(尽可能多匹配),可使用+?,`*?`,??, {m,n}?使用非贪婪模式
- '\' 可以转义特殊字符（允许您匹配 `* . ? + $ ^ [ ] ( ) { } | \ / -` 等字符）
- () 匹配括号内的任何正则表达式，并指示组的开始和结束；可以在执行匹配之后检索组的内容，并且可以稍后在字符串中与下面描述的 \number 特殊序列匹配。要匹配字面值 '(' 或 ')'，请使用 \( 或 \)，或将它们包含在字符类中：[(] [)]。
- [] 用于表示一组字符。在一组

<pre>
	[amk] 将匹配 'a'，'m' 或 'k'。
	[a-z] 将匹配任何小写ASCII字母，[0-5][0-9] 将匹配从 00 到 59 的所有两位数字，并且 [0-9A-Fa-f] 将匹配任何十六进制数字。
	[a\-z]）或者如果它被放置为第一个或最后一个字符（例如 [a-]），则它将匹配文字 '-'。
	[(+*)] 将匹配任何字面字符 '('，'+'，'*' 或 ')'。特殊字符在集合中失去其特殊含义
	[^5] 将匹配除 '5' 之外的任何字符，
	[^^] 将匹配除 '^' 之外的任何字符。如果它不是集合中的第一个字符，^ 没有特殊的意义。
	[()[\]{}] 和 []()[{}] 都将匹配括号。要匹配字符串 ']' 在集合内，在它前面加一个反斜杠，或将它放在集合的开头。
</pre>

---
- re.match() 仅在字符串开头检查匹配，而 re.search() 在字符串中检查匹配的任何位置

### 说明及示例

#### 一般字符

|语法|说明|表达式实例|完整匹配的字符串|
|:-:|:-:|:-:|:-:|
|.|除换行符\n以外的任意字符|r'a.c'|"abc"|
|'\'|改变原字符的意义|r'a\\.c'|"a.c"|
|[...]|单个分类字符集|r"[a-z]"|"b"|

#### 空白字符与预定义字符

|语法|说明|表达式实例|完整匹配的字符串|
|:-:|:-:|:-:|:-:|
|\s|匹配空白字符(space,\t,\r,\n,\f,\v)|r"abc\sde"|"abc de"|
|\S|匹配非空白字符[^\s]|r"a\Sb"|"abb"|
|\d|匹配[0-9]|r'a\dc'|"a1c"|
|\D|非数字|r'a\Dc'|"abc"|
|\w|数字、字母，下划线_|r'a\wc'|"abc"|
|\W|[^\w]|r'a\Wc'|"a c"|

#### 锚字符

|语法|说明|表达式实例|完整匹配的字符串|
|:-:|:-:|:-:|:-:|
|^ or \\A|匹配字符串开头| r'^abc' or r'\Aabc'| 'abc'|
|\$ or \\Z|切尔西字符串结尾| r"abc\$" or r"abc\Z"| 'abc'|

#### 重复字符

|语法|说明|表达式实例|完整匹配的字符串|
|:-:|:-:|:-:|:-:|
|\*|匹配前个字符0次或者无数次|r'ab\*'| "a","ab","abb"|
|+| 匹配前个字符1次或者无数次|r'ab+'| "ab", "abb"|
|?| 匹配前个字符0次或者1次|r'ab?'|"a", "ab"|
|{m}| 匹配前个字符m次| r'ab{2}c'|"abbc"|
|{n,m}| 匹配前个字符n~m次| r'ab{2,4}c' | 'abbc', 'abbbc', 'abbbbc'|
|\*?,+?,??,{n,m}?| 非贪婪 | - | - |

#### 分组字符

|语法|说明|表达式实例|完整匹配的字符串|
|:-:|:-:|:-:|:-:|
|'|'| 匹配左边或者右边 | r"abc|def" | "abc" "def"|
|(...)| 构造一个分组，可用group(1)索引 | r"(abc){2}" | "abcabc" |
|`(?P<name>...)`| 构造一个分组，并创建一别名,可用group(别名)索引 | `r"(?P<name>abc){2}"` | "abcabc"|
|`\number`| 引用编号为number的分组 | r"(\d)abc\1" | "1abc1" "5abc5"|
|`(?p=name)`| 引用分组为name的分组 | `r(?P<id>\d)abc(?p=id)` | "1abc1" "4abc4"|

#### 捕获字符（不分组）

|语法|说明|表达式实例|完整匹配的字符串|
|:-:|:-:|:-:|:-:|
|(?:...)| (...)的不分组，用于使用'\|'或者后接数量词 | r'(?:abc){2}' or r'abc(?:de\|gk)' | "abcabc" or "abcde", "abcgk"|
|(?iLmsux)|用于开头，可选多个| r"(?i)abc" | "aBC"|
|(?#...)| 仅仅是注释 | r"abc(?#comment)123" | 'abc123'|
|(?=...)| 后向肯定符 | r"a(?=\d)" | 'a3' 匹配 'a' |
|(?!...)| 后向否定符 | r"a(?!\d)" | 'ab' 匹配 'a' |
|(?<=...) | 前向肯定符 | r"(?<=\d)a" | '3a' 匹配 'a' |
|(?<!...) | 前向否定符 | r"(?<!\d)a" | 'ba' 匹配 'a' |
|(?(id/name)yes-pattern\|no-pattern| 如果编号为id或者别名为name的组匹配到字符，则需要匹配yes-pattern,否则需要匹配no-pattern \|no-pattern可以省略| r"(\d)abc(?(1)\d\|abc)" | "1abc2", "abcabc" | 


### 用例与说明

<pre>
re.A == re.ASCII  # 使 \w，\W，\b，\B，\d，\D，\s 和 \S 执行纯ASCII匹配，而不是完全Unicode匹配。这仅对Unicode模式有意义，对于字节模式将被忽略。

re.DEBUG  # 显示有关编译表达式的调试信息。

re.I == re.IGNORECASE  # 执行不区分大小写的匹配；表达式像 [A-Z] 也将匹配小写字母。这不受当前语言环境的影响，并如预期的那样工作于Unicode字符。

re.M == re.MULTILINE  # 当指定时，模式字符 '^' 在字符串的开头和每行的开始处（紧跟每个换行符之后）匹配；并且模式字符 '$' 在字符串的末尾和每行的末尾（紧接在每个换行符之前）匹配。默认情况下，'^' 仅在字符串的开头匹配，'$' 仅在字符串的结尾，紧接在字符串结尾的换行符（如果有）之前。

re.S ==  re.DOTALL  # 使 '.' 特殊字符匹配任何字符，包括换行符；没有这个标志，'.' 会匹配任何 except 换行符。

re.X == re.VERBOSE  # 此标志允许您编写看起来更好，更可读的正则表达式，允许您在视觉上分离模式的逻辑节并添加注释。模式中的空格被忽略，除非在字符类中或前面有一个未转义的反斜杠。当一行包含一个不在字符类中的 #，并且没有未转义的反斜杠时，将忽略从最左边的 # 到该行末尾的所有字符。

re.L == re.LOCALE # 根据当前区域设置 \w，\W，\b，\B，\s 和 \S。不鼓励使用此标志
</pre>

`prog = re.complie(pattern)` 将正则表达式模式编译为正则表达式对象

`re.search(pattern, string, flags=0)` 扫描通过 string 寻找正则表达式 pattern 产生匹配的第一个位置，并返回相应的 匹配对象。如果字符串中没有位置匹配模式，则返回 None

`re.match(pattern, string, flags=0)`如果 string 开头的零个或多个字符与正则表达式 pattern 匹配，则返回相应的 匹配对象。如果字符串与模式不匹配，返回 None；

`re.fullmatch(pattern, string, flags=0)`如果整个 string 匹配正则表达式 pattern，则返回相应的 匹配对象。如果字符串与模式不匹配，返回 None；

`re.split(pattern, string, maxsplit=0, flags=0)`通过 pattern 的发生拆分 string。

<pre>
# 如果在 pattern 中使用捕获括号，则模式中所有组的文本也将作为结果列表的一部分返回。如果 maxsplit 非零，则最多发生 maxsplit 分裂，并且返回字符串的其余部分作为列表的最后一个元素。
>>> re.split('\W+', 'Words, words, words.')
['Words', 'words', 'words', '']
>>> re.split('(\W+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']
>>> re.split('\W+', 'Words, words, words.', 1)
['Words', 'words, words.']
>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']

# 如果在分隔符中有捕获组，并且它在字符串的开头匹配，则结果将以空字符串开始。同样适用于字符串的结尾
>>> re.split('(\W+)', '...words, words...')
['', '...', 'words', ', ', 'words', '...', '']
</pre>

`re.findall(pattern, string, flags=0)`返回 string 中 pattern 的所有非重叠匹配，作为字符串列表。 string 从左到右扫描，匹配以找到的顺序返回。如果模式中存在一个或多个组，请返回组列表；如果模式具有多个组，这将是元组的列表。结果中包含空匹配

<pre>
>>> text = "He was carefully disguised but captured quickly by police."
>>> re.findall(r"\w+ly", text)
['carefully', 'quickly']
</pre>

`re.finditer(pattern, string, flags=0)` 返回 iterator 在 string 中的RE pattern 的所有非重叠匹配上产生 匹配对象。 string 从左到右扫描，匹配按找到的顺序返回。

<pre>
>>> text = "He was carefully disguised but captured quickly by police."
>>> for m in re.finditer(r"\w+ly", text):
...     print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
07-16: carefully
40-47: quickly
</pre>

`re.sub(pattern, repl, string, count=0, flags=0)`返回通过用替换 repl 替换 string 中 pattern 的最左侧不重叠出现而获得的字符串。如果未找到模式，则 string 将不更改地返回。

<pre>
>>> re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
...        r'static PyObject*\npy_\1(void)\n{',
...        'def myfunc():')
'static PyObject*\npy_myfunc(void)\n{'

# 如果 repl 是一个函数，则对于 pattern 的每个非重叠发生都调用它。该函数接受单个匹配对象参数，并返回替换字符串。
>>> def dashrepl(matchobj):
...     if matchobj.group(0) == '-': return ' '
...     else: return '-'
>>> re.sub('-{1,2}', dashrepl, 'pro----gram-files')
'pro--gram files'
>>> re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
'Baked Beans & Spam'
</pre>

`re.subn(pattern, repl, string, count=0, flags=0)`执行与 sub() 相同的操作，但返回一个元组 (new_string, number_of_subs_made)。

`re.escape(string)`除了ASCII字母，数字和 '_' 之外，模式中除去所有字符。如果您想匹配任何可能有正则表达式元字符的文字字符串，这将非常有用。

`re.purge()`清除正则表达式高速缓存。

---

`match.expand(template)`返回通过对模板字符串 template 执行反斜杠替换获得的字符串，如 sub() 方法所做。

`match.group([group1, ...])`返回匹配的一个或多个子组。如果有一个参数，结果是单个字符串；如果有多个参数，则结果是每个参数具有一个项的元组。

<pre>
>>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
>>> m.group(0)       # The entire match
'Isaac Newton'
>>> m.group(1)       # The first parenthesized subgroup.
'Isaac'
>>> m.group(2)       # The second parenthesized subgroup.
'Newton'
>>> m.group(1, 2)    # Multiple arguments give us a tuple.
('Isaac', 'Newton')

>>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
>>> m.group('first_name')
'Malcolm'
>>> m.group('last_name')
'Reynolds'
# 命名组也可以通过索引来引用：
>>> m.group(1)
'Malcolm'
>>> m.group(2)
'Reynolds'
</pre>

`match.__getitem__(g)` python3.6新功能，这与 m.group(g) 相同。这使得更容易从匹配中访问单个组

<pre>
>>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
>>> m[0]       # The entire match
'Isaac Newton'
>>> m[1]       # The first parenthesized subgroup.
'Isaac'
>>> m[2]       # The second parenthesized subgroup.
'Newton'
</pre>

`match.groups(default=None)`返回包含匹配的所有子组的元组，从1到模式中的许多组。 default 参数用于未参与匹配的组；它默认为 None。

<pre>
>>> m = re.match(r"(\d+)\.(\d+)", "24.1632")
>>> m.groups()
('24', '1632')

>>> m = re.match(r"(\d+)\.?(\d+)?", "24")
>>> m.groups()      # Second group defaults to None.
('24', None)
>>> m.groups('0')   # Now, the second group defaults to '0'.
('24', '0')
</pre>

`match.groupdict(default=None)`返回包含匹配的所有 named 子组的字典，由子组名称键入。 default 参数用于未参与匹配的组；它默认为 None。

<pre>
>>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
>>> m.groupdict()
{'first_name': 'Malcolm', 'last_name': 'Reynolds'}
</pre>

`match.start([group])`, `match.end([group])`返回由 group 匹配的子串的开始和结束的索引； group 默认为零（表示整个匹配的子字符串）。如果 group 存在但返回 -1 但没有贡献匹配。

<pre>
>>> email = "tony@tiremove_thisger.net"
>>> m = re.search("remove_this", email)
>>> email[:m.start()] + email[m.end():]
'tony@tiger.net'
</pre>

`match.span([group])`对于匹配 m，返回元组 (m.start(group), m.end(group))

`match.pos`将 pos 的值传递给 regex对象 的 search() 或 match() 方法。这是RE引擎开始寻找匹配的字符串的索引。

`match.endpos`将 endpos 的值传递给 regex对象 的 search() 或 match() 方法。这是进入字符串的索引，超过该字符串RE引擎将不会去。

`match.lastindex`最后匹配捕获组的整数索引，如果没有匹配的组，则为 None。

`match.lastgroup`最后匹配的捕获组的名称，如果该组没有名称，或者如果没有匹配任何组，则为 None。

`match.re`match() 或 search() 方法生成此匹配实例的正则表达式对象。

`match.string`字符串传递给 match() 或 search()。