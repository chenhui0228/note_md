# vim脚本语言
### help
- :help vim-script-intro

### 变量

<pre>
# 变量类型一旦分配后，就会保持不变并在运行时严格遵守：
let name = "Damian"

let height = 165

let interests = [ 'Cinema', 'Literature', 'World Domination', 101 ]

let phone     = { 'cell':5551017346, 'home':5558038728, 'work':'?' }
</pre>
- let b:name # 缓冲区局部变量
- let w:name # 窗口的局部变量
- let g:name # 全局变量，也作用于函数中
- let v:name # vim预定义变量
- let s:name # 局部变量
- unlet s:count # 删除变量
- exists() # 检查一个变量是否被定义过
- let s:count = 1 
- let name = "petter"

### 表达式
- $NAME	# 环境变量
- &name	# 选项(变量的值)
- @r	# 寄存器
- a +-\*/% b
- (a) ? (b): (c)
- if {condition} {statements} else {statements}  elseif {conditions} {statemenst} endif
- a == b a!=b a>b a>=b a<b a<=b 
- a =~ pattern a !~ pattern # a字符串满足模式匹配
- :exe 'let optval = &' . optname # 执行冒号命令，.表是连接两个字符串
- :call search("Date: ", "W")

### 函数
- :help function
- :help function-list


### 列表与字典
- let alist=['aap', 'mies', 'noot']
- call add(alist, 'foo') alist + ['foo', 'bar'] call extend(alist, ['two', 'three'])
- let adict = {'one': 'een', 'two': 'twee'}
- adict['one'] adict.one keys(adict)

### 映射
- map # 定义一个仅对缓冲区有效的局部映射
- mapleader 
- noremap # 仅映射脚本以SID开始的映射
- noremenu

