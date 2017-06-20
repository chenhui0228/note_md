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
