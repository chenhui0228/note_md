# Linux用户管理介绍

### 概况
	Linux有三类用户，超级管理员(root)，系统账户(不能登录shell,如nginx)，普通用户(有登录功能)，可以使用`su -` or `sudo` 配合`/etc/sudoers`文件进行用户切换，其中用户登录的过程会经过`PAM(Pluggable Authentication Modules)`嵌入式用户验证模块。用户的配置有9个字段，都写入文件里，用户组的配置有5个，也是写入文件中。用户之间还可以利用 write, mesg, wall, mail等进行通信。
	
### 重要文件
- /etc/passwd
- /etc/shadow
- /etc/group
- /etc/gshadow
- /etc/default/useradd
- /etc/login.defs
- /etc/skel/*
- /etc/securetty
- /etc/nologin
- /etc/pam.d
- /etc/security/limits.conf

### 用户数据结构
- 用户
- 用户组

### 用户增删查改