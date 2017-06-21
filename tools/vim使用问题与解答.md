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

6. 如何正则匹配中文，及如何切换 贪婪与非贪婪模式
<pre>
/\v[^x00-xff] # 只有中文与英文是完全可以的 \v表示采用very magic模式
\v[\u4e00-\u9fa5]+

	<pre>
	vim	Perl	意义
	*	*	0个或多个(匹配优先)
	\+	+	1个或多个(匹配优先)
	\? 或 \=	?	0个或1个(匹配优先)，\?不能在 ? 命令（逆向查找）中使用
	\{n,m}	{n,m}	n个到m个(匹配优先)
	\{n,}	{n,}	最少n个(匹配优先)
	\{,m}	{,m}	最多m个(匹配优先)
	\{n}	{n}	恰好n个
	\{-n,m}	{n,m}?	n个到m个(忽略优先)
	\{-}	*?	0个或多个(忽略优先)
	\{-1,}	+?	1个或多个(忽略优先)
	\{-,1}	??	0个或1个(忽略优先)
	<pre>
</pre>

7. unbuntu及linux系统中设置系统剪切板共享
<pre>
sudo apt install vim-gnome
"+y dd  ctrl+v
ctrl+c "+p p

</pre>
