# vim配置与插件

### auto-pairs
插入或者删除成对的括号，引号{'(':')', '[':']', '{':'}',"'":"'",'"':'"', '\`':'\`'}

### sourround & repeat
sourround快速给词加环绕符号,例如单引号/双引号/括号/成对标签等,repeat通过.操作重复刚才sourround的一次修改操作,关键字`cs`(change sourround),`ds`(delete sourround),`ys`(yield sourround)。如`cs"'`(更改环绕符”为'), `dst`(环绕符html标签), `ysiw"`(在单词外加环绕符”)























































<pre>
# 注意(括号, 左括号会加空格, 右括号不会)
# cs"', ds", ysiw", yss(, yss), ySS", veS",
cs"' => change sourround " to '  	# "Hello world!" -> 'Hello world!'
dst => delete sourround "         # <\a>Hello world!<\/a> -> Hello world! 
ysiw" => yield sourround iw(一个单词里) "  # Hello -> "Hello"
csw"  => up,   # Hello -> "Hello"
yss"  => yield sourround string "  # Hello world -> "Hello world"
yss), yss(  => up, no space   # Hello world -> (Hello world), ( Hello world )
ys$)  => yield sourround until line-end ) # 
ySS"  => up, 引号到上下两行
veS"  => ve(选择好一个单词), 添加“,效果与ysiw"类似
</pre>