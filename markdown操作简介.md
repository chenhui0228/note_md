# Markdown 操作简介

### 标题
- 使用 # ## ... ######
### 引用
- `> 这是一段引用`

### 列表
- 有序列表用 1.
- 无序列表用 -. *. +.

### 链接与图片
- 使用链接 `[haijunt](http://www.haijunt.com)`
- 使用链接(参考式)
```
[an example] [id]
[id]: http://example.com/ "Option Title Here"
```
- 使用图片 `![]http://www.haijunt.com/xx.png`
- 使用图片(参考式)
```
![Alt text][id]
[id]: url/to/imgae "Optional title attribute"
```
- 使用图片(html)
```
<a href="http://example.com/" width=20 height=30>http://example.com/</a>
```

### 段落
- 使用空四格 或者 tab符

### 分隔线
`--- or *** or ___`

### 粗体与斜体
- `**这是粗体**` **粗体**
- `*这是斜体*` *斜体*

### 代码
- \`one line code\` `one line code`
- 多行代码用 \```xx\```
```
>>> print 'helle world'
hello world
```

### 表格
```
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
```