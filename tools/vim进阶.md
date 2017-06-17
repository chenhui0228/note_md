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
vim *.txt
:ls # 查看所有的缓冲区列表的文件名
(:bnext, :bprev, :bfirst, :blast, :buffer N, :buffer filename, :bdelete N1 N2, :n,m bdelete)
:bnext!  # 可以设置hhindden忽略!的书写，而直接用下面的命令保存，重新覆盖或者退出
(:bwrite, :edit!)
(:quit!, :qall!, :wall)
</pre>

- 参数列表
<pre>
vim *.txt, vim
(:args args *.txt, :args **/*.txt, args `cat .chapters`) # 查看当前参数列表，将一些文件设置新的分组, 以递归到下层目录的形式，以shell命令的输出形式
(:next, :prev)
:argdo # 在当前的参数列表组里为每个文件执行命令
</pre>

- 窗口管理
<pre>
(ctrl+w+s, ctrl+w+v, :sp filename, :vsp filename)
(ctrl+w+w, ctrl+w+hjkl)
(ctrl+w+=, ctrl+w+_, ctrl+w+|, num+ctrl+w_, num+ctrl+w+|) # 设置所有窗口等高宽，最高，最宽，高num, 宽num列
(:clo, :only) # 关闭活动窗口，只保留活动窗口，关闭其他所有窗口
</pre>

- 标签页(可以容纳一系列窗口的容器)
<pre>
:tabedit filename # 打开文件到缓冲区并加入新的标签页
:tabs	# 查看有多少标签页
:lcd {path}
ctrl+w+T # 把当前窗口移到新标签页中
({N}gt, {N}gT, :tabnext, :tabprevious, :tabnext {N})
:tabmove {N} # 重排标签页，移到最后 if N is None else 移到N
(:tabonly, :tabclose) # 关闭标签页
</pre>

- 文件打开与保存
<pre>
:edit filename
:edit %Tab	# 当前文件路径
:edit %:h	# 当前目录路径,可以设置映射项		
:find filenameTab # 打开打到的文件到缓冲区,需要设置 :set path+=app/**确保在该目录下去find
:!make -p %:h, :write	# 假如edit的filename并不存在，可以使用shell命令先创建，再保存
:w !sudo tee % > /dev/null # 可以参考:w !{cmd}, :r !{cmd}等相关命令
</pre>

- 打开文件管理器
<pre>
:edit ., :e.	# 打开文件管理器，并显示当前工作目录
:Explore, :E	# 打开文件管理器，并显示活动缓冲区所在的目录
:Sexplore	# 水平切分窗口打开文件管理器
:Vexplore	# 垂直切分窗口打开文件管理器
</pre>



### 窗口
- 编辑区
- 状态行
- 缓冲区
- 命令窗口
- 多窗口

### 操作符

<pre>
- c d y g~ gu gU > < = ! p, ctrl+a, ctrl+x
</pre>

### 动作命令
<pre>
- h j k l 0 ^ $ gj gk g0 g^ g$
- w W b B e E ge g
- fFtT ; ,
</pre>

### 文本对象
<pre>
- iw aw iW aW is iS as aS ip ap i/a ) ] } ' " `>t
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
