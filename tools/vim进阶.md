# vim进阶

### 问题
- 如何快速将一个单词替换成另外一个单词
- 如何快速移动到想到达的位置


### 模式
- 普通模式
- 插入模式
- 插入普通模式
- 命令模式
- 可视模式，选择模式

### 窗口
- 编辑区
- 状态行
- 缓冲区
- 命令窗口
- 多窗口

### 口决
- "点范式": 用一键移动，另一键执行
- "操作": = 操作符+动作命令

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

### 操作符

<pre>
- c d y g~ gu gU > < = !
</pre>

### 插入模式

<pre>
- ctrl+h ctrl+w ctrl+u
- Esc ctrl+[
- ctrl+o
- ctrl+r+0
- ctrl+r + ctrl+p + 0
- ctrl+r + =
- ctrl+v ctrl+k+char1+char2
- gr gR
</pre>


### 可视模式

<pre>
- ctrl+g
- v V ctrl+v
- gv
- Esc ctrl+[
- o
</pre>

### 命令行模式

<pre>
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
