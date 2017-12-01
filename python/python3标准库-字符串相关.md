# python3标准库-字符串相关

字符串的处理主要有str,string,textwrap,difflib,re 等模块。字符串是Python中最常用的数据类型。自身集成了很多方法，在此之外，还有string模块主要提供format方法对字符串进行格式化，在python3里也是一种很现代化并且官方推荐使用的方法.另外对Template模板进行了介绍与使用案例。而对于文本需要使用textwrap模块，还包括功能更加强大的TextWrapper类。difflib主要用于字符串与文本的比较分析，使用时可以参考官方文档。re正则因为内容比较多，打算另成一篇。

- str
- string
- textwrap
- difflib
- re

## str

字符串对象可以进行 替换、删除、截取、复制、连接、比较、查找、包含、大小写转换、分割 等操作，略过...

字符串内建函数

<pre>
str(123) # 将其它类型强转为字符串类型
capitalize() # 将字符串的第一个字符转换为大写
center(width, fillchar) # 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
count(str, beg=0, end=len(string)) # 出现的次数
startswith(suffix, beg=0, end=len(string)) # 是否以suffix开始
endswith(suffix, beg=0, end=len(string)) # 是否以suffix结束
expandtabs(tabsize=8)	# 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8
find(str, beg=0, end=len(string)) # 检测 str 是否包含在字符串中，如果指定范围 beg 和 end,没有则返回-1
rfind(str, beg=0, end=len(string))  # 类似于 find()函数，不过是从右边开始查找.
index(str, beg=0, end=len(string)) # 跟find()方法一样，只不过如果str不在字符串中会报一个异常.
rindex(str, beg=0, end=len(string))
isalnum() # 所有字符都是字母或数字则返 回 True,否则返回 False
isalpha() # 所有字符都是字母则返回 True, 否则返回 False
isdigit() # 字符串只包含数字则返回 True 否则返回 False..
isdecimal() # 是否只包含十进制字符，如果是返回 true，否则返回 false。
islower()  # # 所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
isnumeric() # 字符串中只包含数字字符，则返回 True，否则返回 False
isspace()  # 如果字符串中只包含空白，则返回 True，否则返回 False.
title()  # 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写
istitle() # 字符串是标题化的(见 title())则返回 True，否则返回 False
isupper() # 所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
','.join(seq)  # 以指定字符串`,`，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
len(string) # 返回字符串长度
ljust(width[, fillchar]) # 返回一个原字符串左对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
rjust(width[, fillchar]) # 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
lower() # 转换字符串中所有大写字符为小写
upper() # 转换字符串中的小写字母为大写
swapcase() # 大小写互换
lstrip([seq])
rstrip([seq]) 
strip([seq]) # 去年左右两边seq字符，默认去空格
maketrans() # 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
max(str)
min(str) # 返回字符串 str 中最小的字母。
replace(old, new [,max]) # 把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
split(str="", num=string.count(str)) # 返回按str分隔的列表
splitlines(keepends) # 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
translate(table, deletechars="") # 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
zfill(width)  # 返回长度为 width 的字符串，原字符串右对齐，前面填充0
</pre>

## string

### 字符串常量与首字母大写函数

<pre>
string.ascii_litters	# =>'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_lowrcase	# =>'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase	# =>'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.digits				# =>'0123456789'
string.hexdigits			# =>'0123456789abcdefABCDEF'
string.octdigits			# =>'01234567'
string.punctuation		# =>'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
string.printable			# =>'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
string.whitespace		# =>' \t\n\r\x0b\x0c'

# string.capwords(s, sep=None)
string.capwords('The quick brown fox jumped over the lazy dog.') # =>The Quick Brown Fox Jumped Over The Lazy Dog.
</pre>

### class `string.Formatter`格式化字符串方法

- format(format_string, \*args, \*\*wargs) # 常用就这一个函数
- vformat(format_string, args, kwargs)
- parse(format_string)
- get_field(field_name, args, kwargs)
- get_value(key, args, kwargs)
- check_unused_args(used_args, args, kwargs)
- format_field(value, format_spec)
- convert_field(value, conversion)

#### 按位置访问参数

<pre>
>>> '{0}, {1}, {2}'.format('a', 'b', 'c')
'a, b, c'
>>> '{}, {}, {}'.format('a', 'b', 'c')  # 3.1+ only
'a, b, c'
>>> '{2}, {1}, {0}'.format('a', 'b', 'c')
'c, b, a'
>>> '{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence
'c, b, a'
>>> '{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated
'abracadabra'
</pre>

#### 按名称访问参数

<pre>
>>> 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
'Coordinates: 37.24N, -115.81W'
>>> coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
>>> 'Coordinates: {latitude}, {longitude}'.format(**coord)
'Coordinates: 37.24N, -115.81W'
</pre>

#### 对齐文本并指定宽度

<pre>
>>> '{:<30}'.format('left aligned')
'left aligned                  '
>>> '{:>30}'.format('right aligned')
'                 right aligned'
>>> '{:^30}'.format('centered')
'           centered           '
>>> '{:*^30}'.format('centered')  # use '*' as a fill char
'***********centered***********'
</pre>

#### 替换 %+f，%-f 和 % f 并指定符号

<pre>
>>> '{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
'+3.140000; -3.140000'
>>> '{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers
' 3.140000; -3.140000'
>>> '{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}'
'3.140000; -3.140000'
</pre>

#### 使用逗号作为千位分隔符:

<pre>
>>> '{:,}'.format(1234567890)
'1,234,567,890'
</pre>

#### 表示百分比

<pre>
>>> points = 19
>>> total = 22
>>> 'Correct answers: {:.2%}'.format(points/total)
'Correct answers: 86.36%'
</pre>

#### 使用特定于类型的格式

<pre>
>>> import datetime
>>> d = datetime.datetime(2010, 7, 4, 12, 15, 58)
>>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
'2010-07-04 12:15:58'
</pre>

### class `string.Template`模板字符串

- substitute(mapping, \*\*kwargs)
- safe_substitute(mapping, \*\*kwargs)
- template

<pre>
>>> from string import Template
>>> s = Template('$who likes $what')
>>> s.substitute(who='I', what='mmyxs')
'I likes mmyxs'
>>> d = dict(who='I')
>>> Template('Give $who $100').substitute(d)
Traceback (most recent call last):
...
ValueError: Invalid placeholder in string: line 1, col 11
>>> Template('$who likes $what').substitute(d)
Traceback (most recent call last):
...
KeyError: 'what'
>>> Template('$who likes $what').safe_substitute(d)
'I likes $what'
</pre>

---

## textwrap

### textwrap模块

只是包装或填充一个或两个文本字符串，方便的功能应该是足够好；否则，您应该使用 TextWrapper 的实例来提高效率。

`textwrap.wrap(text, width=70, \*\*kwargs)` 将单个段落包含在 text （字符串）中，因此每行最多 width 个字符长。返回输出行的列表，没有最后的换行符。

<pre>
sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''
</pre>

`textwrap.fill(text, width=70, \*\*kwargs)` 将单个段落包装在 text 中，并返回包含包装段落的单个字符串。

<pre>
print(textwrap.fill(sample_text, width=50))
=============================================
     The textwrap module can be used to format
text for output in     situations where pretty-
printing is desired.  It offers     programmatic
functionality similar to the paragraph wrapping
or filling features found in many text editors.
</pre>

`textwrap.shorten(text, width, **kwargs)` 折叠和截断给定的 text 以适合给定的 width。

<pre>
>>> textwrap.shorten("Hello  world!", width=12)
'Hello world!'
>>> textwrap.shorten("Hello  world!", width=11)
'Hello [...]'
>>> textwrap.shorten("Hello world", width=10, placeholder="...")
'Hello...'
</pre>


`textwrap.dedent(text)` 从 text 中的每一行删除任何共同的前导空白。

<pre>
dedented_text = textwrap.dedent(sample_text)
print('Dedented:')
print(dedented_text)
==========================
Dedented:

The textwrap module can be used to format text for output in
situations where pretty-printing is desired.  It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
</pre>


`textwrap.indent(text, prefix, predicate=None)` 将 prefix 添加到 text 中选定行的开头。

<pre>
>>> s = 'hello\n\n \nworld'
>>> indent(s, '  ')
'  hello\n\n \n  world'
>>> print(indent(s, '+ ', lambda line: True))
+ hello
+
+
+ world
</pre>

### class `textwrap.TextWrapper`
- 参考`官方文档` 或者https://www.rddoc.com/doc/Python/3.6.0/zh/library/textwrap/#module-textwrap

## difflib —计算增量的帮助者

更多详细内容请参考`官方文档` 或者 https://www.rddoc.com/doc/Python/3.6.0/zh/library/difflib/#module-difflib

- class `difflib.SequenceMatcher`这是用于比较任何类型的序列对的灵活类，只要序列元素是 hashable。
- class `difflib.Differ` 这是一个类，用于比较文本行的序列，并产生人类可读的差异或增量。 Differ使用 SequenceMatcher 来比较线的序列，并且比较类似（近匹配）线内的字符序列。
- class `difflib.HtmlDiff` 此类可用于创建一个并排显示的HTML表（或包含表的完整HTML文件），逐行比较文本与行间变化和行内变化亮点。该表可以在完全或上下文差分模式下生成。
- `difflib.context_diff(a, b, fromfile='', tofile='', fromfiledate='', tofiledate='', n=3, lineterm='\n')` 比较 a 和 b （字符串列表）；在上下文差异格式中返回增量（生成增量线的 generator）。
- `difflib.get_close_matches(word, possibilities, n=3, cutoff=0.6)`返回最好的“足够好”匹配的列表。 word 是需要紧密匹配的序列（通常是字符串），possibilities 是与 word 匹配的序列列表（通常是字符串列表）。
- `difflib.ndiff(a, b, linejunk=None, charjunk=IS_CHARACTER_JUNK)`比较 a 和 b （字符串列表）；返回 Differ 样式增量（生成增量线的 generator）。
- `difflib.restore(sequence, which)` 返回生成增量的两个序列之一。
- `difflib.unified_diff(a, b, fromfile='', tofile='', fromfiledate='', tofiledate='', n=3, lineterm='\n')` 比较 a 和 b （字符串列表）；以统一差异格式返回增量（生成增量线的 generator）。
- `difflib.diff_bytes(dfunc, a, b, fromfile=b'', tofile=b'', fromfiledate=b'', tofiledate=b'', n=3, lineterm=b'\n')` 使用 dfunc 比较 a 和 b （字节对象列表）；以 dfunc 返回的格式产生一系列delta线（也是字节）。 
- `difflib.IS_LINE_JUNK(line)` 对于可忽略的行返回true。如果 line 为空或包含单个 '#'，则线 line 可忽略，否则不可忽略。在旧版本中用作 ndiff() 中参数 linejunk 的默认值。
- `difflib.IS_CHARACTER_JUNK(ch)`对可忽略的字符返回true。如果 ch 是空格或制表符，则字符 ch 可忽略，否则不可忽略。用作 ndiff() 中参数 charjunk 的默认值。

## re

re模块的内容将另起一篇文档
