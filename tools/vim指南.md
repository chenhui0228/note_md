# vim指南

## vim功能
### 多窗口，多文件管理与编辑
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
### 快速移动
### 查找与替换
### 配置支持
- hhidden

### 插件支持
- unimpaired.vim	# 使用"[", "]"做相关命令的前缀

	


