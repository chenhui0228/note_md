# Bash基础

### 学习线路
- Bash启动->Bash功能->Bash变量->Bash命令与数据流->管道

### 重点
- Bash变量
- 数据流重定向
- 管道

### Bash启动

- 系统环境

<pre>
	/etc/profile	系统整体的设置
	/etc/inputrc	Bash热键定义,被profile调用
	/etc/profile.d/*.sh	规定Bash操作接口的颜色，别名等，被调用
	/etc/sysconfig/i18n	配置默认语系
</pre>

- 自定义环境配置

<pre>
	# 如何配置欢迎信息
	/etc/issue	本地连接Bash
	/etc/issue.net	telnet连接Bash
	/etc/motd	用户登录后的信息
	# 环境配置文件
	～/.bash_profile	
	～/.bashrc	被.bash_profile调用
	/etc/bashrc	整体配置，如根据UID配置umask,PS1
	～/.bash_login	如果没有.bash_profile,则执行，有，则被调用
	～/.profile	如果没有.bash_login,则执行，有，则被上调用
	# 使配置生效
	- `source` or `.`
	# 其他
	/etc/man.config	规定man去哪里寻找路径
	～/.bash_history	历史命令记录
	～/.bash_logout	注销bash后执行什么操作
</pre>

- 终端机的环境设置
	- stty
	- set

### Bash功能
- 命令记忆与补全
	- history
	- !!
	- !number
	- !command
- 别名，通配符，程序脚本支持
	- alias
	- \* ? [] [-] [^]
	- \# \ | ; ～ $ & ! / >,>> <,<< \`` "" '' () {}
	- ; && ||
- 作业控制
	- jobs
	- fg
	- bg

### Bash变量
- 环境变量(全局)
	- LANG(locale -a), PS1, MAIL, PATH, SHELL, HOME, RANDOM, $$(shell PID), $?(回传值 上次运行命令的返回值 0 1) ...
- 自定义变量(局部)
	- a='a' a="b" #''对$保持原义	# 字符串
	- declare -i sum=100+300	# 整型
	- var[1]="2"	# 数组
	
- 变量设置
	- env	# 查看所有环境变量
	- set	# 查看所有环境变量及自定义变量
	- echo ${a} $PATH ${MAIL}is	# 输出与变量有关
	- $(ls -al) \`uname -a`	# 输出与命令有关
	- export	# 将变量升级为环境变量
	- read [-pt] var	# 用户输入
	- declare [-pfixr +-] var  #显示变量属性，只显示函数，数值，升级为shell变量，设置为只读，加减某个属性
- 命令的查询顺序
	- 相对或者绝对路径》alias》builtin》$PATH
	
- 变量操作(删除，替代，替换)
	- ${变量#关键字}	从头开始，删除最短
	- ${变量##关键字}	从头开始，删除最长
	- ${变量%关键字}	尾，最短
	- ${变量%%关键字}	尾，最长	
	- ${变量/旧/新}		仅替换第一个
	- ${变量//旧/新}	全部替换
	---
	- var=${str-expr}	变量str未设置，var=expr
	- var=${str:-expr}	变量str未设置或者空，var=expr
	- var=${str+expr}	变量str有设置，var=expr
	- var=${str:+expr}	变量str有设置或者空，var=expr
	- var=${str=expr}	str也跟着一起变
	- var=${str:=expr}	。。。
	- var=${str?expr}	变量str未设置，则有错误输出
	- var=${str:?expr}	变量str未设置或为空，则有错误输出
	
### 数据流重定向
- 标准输入(stdin)	0	<,<<
- 标准输出(stdout)	1	>,>>
- 标准错误输出(stderr)	2	2>,2>>
- 黑洞	/dev/null

### 管道
- 管道只处理standard output,对standard erroutput 会忽略
- 管道必须接收前一个命令的数据成为standard output继续处理
- 很多命令并不支持管道命令,如 ls
- 常用管道命令有 cut, grep, sort, wc, uniq, tee, tr, col, join, paste, expand, split, xargs

### ?
- 是否可以用命令查看某个命令是否支持管道?
- 变量的数据结构？
