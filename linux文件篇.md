# linux文件篇

## linux文件目录结构

```
# 遵守FHS(Filesystem Hierarchy Standard)
/		与开机系统有关
/usr		与软件安装或者执行有关
/var		与系统运行有关

/bin		系统执行文件目录
/etc		系统主要配置文件
/lib		系统函数库
/sbin		超级用户设置系统环境目录
/dev		设备，接口
/boot		开机使用到的文件
/opt		三方软件目录
/media		可删除设备挂载目录
/mnt		可删除设备挂载目录
/srv		网络服务目录
/tmp		临时文件

/proc		虚拟文件系统
/sys		虚拟文件系统	
```

## 文件属性

```
-rw-r--r--  1 haijunt haijunt  8261 4月   2 22:35 .vimrc

文件类型	[-dlbcsp][普通文件 目录文件 链接 块设备 字符设备 接字 管道]
文件拥有者权限	[-rwx][无权限 读 写 执行]
文件用户组权限	[-rwx][无权限 读 写 执行]
文件其它用户权限	[-rwx][无权限 读 写 执行]
文件连接数	[number] [当前被几个用户连接]
文件所有者	[haijunt][]
文件所属用户组	[haijunt][]
文件最后修改时间	[time]
文件名称	[.vimrc]
```

## 文件权限

```
值	数值	文件权限	目录权限
r	4	文件可读取	文件可用ls查看
w	2	文件可写入	可更改目录结构(new del mv ch)
x	1	文件可执行	文件可用cd进入
```