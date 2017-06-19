# vim进阶

### 技巧
- "点范式": 用一键移动，另一键执行
- "操作": = 操作符+动作命令
	- 字符命令形式 [{count}=1}]{operator}
	- 动作命令形式 [{count}=1]{operator}{motion}
	- 行命令形式 {operator}{operator}


### 问题
- 如何快速将一个单词替换成另外一个单词
- 如何快速移动到想到达的位置

### vim名词解析
- 缓冲区列表
<pre>
- vim *.txt
- :ls # 查看所有的缓冲区列表的文件名
- (:bnext, :bprev, :bfirst, :blast, :buffer N, :buffer filename, :bdelete N1 N2, :n,m bdelete)
- :bnext!  # 可以设置hhindden忽略!的书写，而直接用下面的命令保存，重新覆盖或者退出
- (:bwrite, :edit!)
- (:quit!, :qall!, :wall)
</pre>

- 参数列表
<pre>
- vim *.txt, vim
- :cd dirname # 进入另外一个目录做为工作目录
- (:args args *.txt, :args **/*.txt, args `cat .chapters`) # 查看当前参数列表，将一些文件设置新的分组, 以递归到下层目录的形式，以shell命令的输出形式
- (:next, :prev)
- :argdo # 在当前的参数列表组里为每个文件执行命令
</pre>

- 窗口管理
<pre>
- (ctrl+w+s, ctrl+w+v, :sp filename, :vsp filename)
- (ctrl+w+w, ctrl+w+hjkl)
- (ctrl+w+=, ctrl+w+_, ctrl+w+|, num+ctrl+w_, num+ctrl+w+|) # 设置所有窗口等高宽，最高，最宽，高num, 宽num列
- (:clo, :only) # 关闭活动窗口，只保留活动窗口，关闭其他所有窗口
</pre>

- 标签页(可以容纳一系列窗口的容器)
<pre>
- :tabedit filename # 打开文件到缓冲区并加入新的标签页
- :tabs	# 查看有多少标签页
- :lcd {path}
- ctrl+w+T # 把当前窗口移到新标签页中
- ({N}gt, {N}gT, :tabnext, :tabprevious, :tabnext {N})
- :tabmove {N} # 重排标签页，移到最后 if N is None else 移到N
- (:tabonly, :tabclose) # 关闭标签页
</pre>

- 文件打开与保存
<pre>
- :edit filename
- :edit %Tab	# 当前文件路径
- :edit %:h	# 当前目录路径,可以设置映射项		
- :find filenameTab # 打开打到的文件到缓冲区,需要设置 :set path+=app/**确保在该目录下去find
- :!make -p %:h, :write	# 假如edit的filename并不存在，可以使用shell命令先创建，再保存
- :w !sudo tee % > /dev/null # 可以参考:w !{cmd}, :r !{cmd}等相关命令
</pre>

- 打开文件管理器
<pre>
- :edit ., :e.	# 打开文件管理器，并显示当前工作目录
- :Explore, :E	# 打开文件管理器，并显示活动缓冲区所在的目录
- :Sexplore	# 水平切分窗口打开文件管理器
- :Vexplore	# 垂直切分窗口打开文件管理器
</pre>

- 命令行窗口
<pre>
- q:
- q/
</pre>

### 操作符

<pre>
- c d y g~ gu gU > < = ! p, ctrl+a, ctrl+x
</pre>

### 动作命令
<pre>
- h j k l 0 ^ $ gj gk g0 g^ g$
- w W b B e E ge g
- fFtT ; ,
- / ? # 查找d{motion}

### 文本对象
<pre>
- iw aw iW aW is as ip ap #范围文本对象 单词 串 句子 段落
- i/a ) ] } ' " `>t # 分隔符对象


### 快速跳转
<pre>
- m{letter} m{upper}
- 'letter `letter
- \`letter
- '' '. '^ '[ '] '< '> # 跳转之前 修改 插入 修改复制开始 修改复制结束 高亮开始 高亮结束
- %   # 配置matchit插件更好用
- :jumps ( ) { } H M L gf ctrl+] # 跳转到上句开头 下名开头 上段开头 下段开头 屏幕上方 中间 下方 光标下文件名 函数定义处(需要配置suffixesadd,path)
- :changes g; g, gi   # 查看修改列表 跳转到上次修改 回来 跳转到上次插入的行列
- ctrl+o ctrl+i # 往前跑 往后跳
</pre>
</pre>

### 普通模式
<pre>
- :h vimtutor
- f{char}/t{char} ; ,
- F{char}/T{char} ; ,
- n N
- &
- %s/content/copy/g
- *, cw, n, ., *nn
- daw, ciw
- ctrl+a ctrl+x
</pre>

### 插入模式

<pre>
- `c C s S i I a A o O r R gr gR`
- ctrl+h ctrl+w ctrl+u
- Esc ctrl+[
- ctrl+o
- ctrl+r+0
- ctrl+r + ctrl+p + 0
- ctrl+r + =
- ctrl+v ctrl+k+char1+char2
</pre>


### 可视模式

<pre>
- 'v V ctrl+v'
- ctrl+g
- gv
- Esc ctrl+[
- o
</pre>

### 命令行模式

<pre>
- `: \ ?`
- :edit
- :write
- :tabnew
- :split :vsplit
- :prev :next
- :bprev :bnext
- :copy :t :co
- :yank :put
- :move :m
- :join
- :delete
- :normal
- :substitute
- :global/{pattern}/[cmd]
- :print
- ctrl+w ctrl+u ctrl+v ctrl+k
- ctrl+r+0
- ctrl+r + ctrl+w
- :%s//ctrl+r + ctrl+w/g
- :shell
- :! {cmd}
- :read !{cmd}
- :write !{cmd}
- :[range] !{filter}
- :2,$! sort -t ',', -k2
- q: q/ ctrl+f
- ., %, $, '<, '>, +n
</pre>
### 插入普通模式
### 插入待决模式


### 寄存器
<pre>
- :reg "{register}"
- "_  # 黑洞寄存器
- "_  # 无名寄存器(d,x,s,c,y默认)
- "0  # 专有寄存器(y操作除了存入默认的，还会存入专有)"
- "{letter} # 有名寄存器，以替换形式
- "{upper}  # 有名寄存器，以追加形式
- "+  # 系统剪切板
- "*  # 选择专用寄存器(需要:version +xterm_clipboard支持)
- "= "% "# ". ": "/ # 表达式 当前文件名 轮换文件名 上次插入文本 上次EX命令 上次查找模式
</pre>

### 宏
<pre>
- q{register} where? from_where? go_where?(0 n gg G u b e j i a) q
- :reg {register}
- q{upper} ... q # 追加宏的命令
- [number]@{register} @@  # 重复执行多次 重复一次上次 
- :normal @{register} # 并行执行多次
- :put a # 将寄存器的宏命令粘贴到文本
- "add `0 "ay$ dd` #推荐使用第二种方式，不会有换行符的干扰
- :let @a=subsitute(@a, '\~', 'vU', \g') # 另外用编程方式更改宏
</pre>

### 查找进阶
<pre>
- \v \V # 更你python perl的正则  原义匹配忽略.*+的特殊含义但不包括/?\
- <> # 限定边界符 /\v<the>
- \zs \ze #从哪个匹配开始 结束，只高亮后面匹配
- () %(|) # 分组 不分组
- \_s #空白符或者换行符
- \w \W #字母 数字 _ 单词类字符  取反
- \\e 重复上次查找并到结尾
</pre>

### quickfix列表
<pre>
- mM
- :vimgrep
- :grep
- :make
- \`M
</pre>
