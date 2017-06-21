# vim使用问题与解答

1. 如何在普通模式中向前向后删除一个字符？

2. 如何快速处理tab与空格的替换？

<pre>
	# in vimrc
	set ts=4
	set expandtab

	# in vim filename
	# Tab => 空格
	:set ts=4
	:set expandtab
	:%retab!

	# space => tab
	:set ts=4
	:set noexpandtab
	:%retab!
</pre>


3. 如何快速复制一部分文本到另外一个文本，替换两个文本
4. 如何忽略大小写进行查找,只查找特定单词

<pre>
set ignorecase
set noignorecase
set incsearch
/\<The\> # 默认都是行为单位，行内所有The单词
/The\> # 行内所有以The为结尾的单词
/the$ # 仅匹配一个在当前行结尾的the
/^the # 仅匹配一个在当前行开始的the
</pre>

5. 如何理解“移动”与“跳转”
<pre>
- jumps
每次执行这个命令会跳到本行之外，但也不包括'j','k'
.ex jumps:
- / ? n G
.ex moves:
- fx tx w e j k 
</pre>
