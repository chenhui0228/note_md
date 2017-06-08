# shell基础
### Bash功能
- 命令记忆与补全
- 别名，通配符，程序脚本支持
- 作业控制

### 精华
- 变量设置与使用
- bash操作环境
- 数据流重定向
- 管道

### 注意点
- 命名规范
- 赋值两头不能在空格
- 单引号会保存原有特性，而双引号会输出$等变量值
- 特殊字符可以用`\`进行转义

### 变量类型
- 系统变量： MAIL,PATH,HOME,SHELL
- 自定义变量： a
- 环境变量： export a

### 数据类型

- 字符串
- 数组

### 运算符

- 算术运算符
	- \+ - * / % = (加 减 乘 除 余 赋值)
	- == != (相等 不等)
- 关系运算符
	- -eq -ne (等于 不等于?)
	- -gt -lt (大于 小于?)
	- -ge -le (大于或等于 小于或等于?)
- 逻辑运算符
	- ! (非(取反))
	- -a && (与)
	- -o || (或)
- 字符串运算符
	- = != (字符串内容相等 不相等?)
	- -z -n (字符串长度是否为0 是否不为0?)
- 文件测试运算符
	- -b -c -f -p (块设备 字符设备 普通 管道文件？)
	- -r -w -x (可读 写 执行？)
	- -u -g -k (有SGID SUID SBIT位?)
	- -s -e (内容为空 文件存在？)
	- -d (目录？)
	
### 特殊词
- echo
- unset
- readonly
- function
- $var, $\{var\}, \`command\`, ${command}
	
### 流程控制

- if, else-if, else, for, while, until, case, continue, break

```
for var in item1 item2 ... intemN
do
	command1
	if [ $a == $b ]
	then
		continue
	elseif [ $a -gt $b ]
	then
		break
	else
		break
	fi
	...
	commandN
done

while condition
do
	case value in
	node1)
		command1
		...
		commandN
		;;
	node2)
		command1
		...
		commandN
	;;
	node3)
		continue
	;;
	node4)
		break
	;;
	esac
done

until condition
do
	command
done

```

### 函数
- 函数定义与声明

```
	# function可不声明，如果不返回数值，则默认返回最后语句执行结果值

[ function ] funname [()]
{
	action;
	[return int;]
}
```

- 函数传参与处理
	- $n if n<10 else ${n} (第n个参数)
	- $# (有多少个参数)
	- $*, $@ (一个参数以单一字符串显示所有参数，多个参数且所有参数都加引号)
	- $$, $! (当前运行进程ID号，后台运行的最后一个进程ID号)
	- $-
	- $?