# centos安装配置phabricator

### 路线图
- 安装
	- LNMP
	- Phabricator源码下载与运行
- 配置
	- 启动配置
	- 基本配置
	- 设置用户登录认证方式
	- 设置邮件发送服务参数
	- 配置代码仓库访问方式
- Code Review
- 与GitHub集成
- 与Jenkins集成

### LNMP
- (L)更新centos机器
	- yum update
- (N)httpd服务安装（也可以使用Nginx)
	- yum install httpd -y
	- systemctl enable httpd.service
	- systemctl start httpd.service
- (M)mysql安装

	<pre>
	wget https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm
	md5sum mysql57-community-release-el7-9.noarch.rpm
	sudo rpm -ivh mysql57-community-release-el7-9.noarch.rpm
	sudo yum install -y mysql-server
	sudo systemctl start mysqld
	sudo systemctl status mysqld
	sudo grep 'temporary password' /var/log/mysqld.log  # 得到初始化临时密码
	sudo mysql_secure_installation # 设置新密码等
	mysql -u root -p  # 验证新密码是否能够登录
	</pre>

- (P)php与扩展安装
	- sudo yum install -y php php-mysql php-gd php-curl php-apc php-cli -y
- git安装
	- yum install -y git

### Phabricator源码下载与运行

<pre>
mkdir -p /var/www/html/myapp
cd /var/www/html/myapp

git clone https://github.com/phacility/libphutil.git
git clone https://github.com/phacility/arcanist.git
git clone https://github.com/phacility/phabricator.git
</pre>

### 启动配置
- vim /etc/httpd/conf/httpd.conf

<pre>
# 注意ServerAdmin your_domain填写为你的域名，没有域名则可以不管
<VirtualHost *:80>
ServerAdmin root@your_domain
ServerName your_domain
DocumentRoot /var/www/html/myapp/phabricator/webroot
RewriteEngine on
RewriteRule ^/rsrc/(.*)     -                       [L,QSA]
RewriteRule ^/favicon.ico   -                       [L,QSA]
RewriteRule ^(.*)$          /index.php?__path__=$1  [B,L,QSA]
<Directory "/var/www/html/myapp/phabricator/webroot">
Order allow,deny
Allow from all
</Directory>
</VirtualHost>
</pre>

<pre>
# your_mysqlb_root_password 字段尽量用引号'包住
cd phabricator
./bin/config set mysql.host localhost
./bin/config set mysql.user root
./bin/config set mysql.pass your_mysqlb_root_password
./bin/storage upgrade --user root --password your_mysqlb_root_password

systemctl restart mysqld

yum install -y php-mbstring
systemctl restart httpd
</pre>

### 基本配置
- web访问 http://your_ip_adress,或者域名。注册第一个用户（成功后将是管理员用户）,成功后将有问题需要解决(我这儿14个）
	- Disable PHP always_populate_raw_post_data
	- Small MySQL "max_allowed_packet"
	- MySQL ONLY_FULL_GROUP_BY Mode Set
	- MySQL May Run Slowly
	- Server Timezone Not Configured
	- Alternate File Domain Not Configured
	- Missing Repository Local Path
	- Install Pygments to Improve Syntax Highlighting
	- Large File Storage Not Configured
	- PHP post_max_size Not Configured
	- PHP Extension 'APC' Not Installed
	- Base URI Not Configured
	- No Authentication Providers Configured
	- Phabricator Daemons Are Not Running

<pre>
# Disable PHP always_populate_raw_post_data
# vim /etc/php.ini
always_populate_raw_post_data = -1

# Small MySQL "max_allowed_packet"
# vim /etc/my.cnf
max_allowed_packet=33554432

# MySQL ONLY_FULL_GROUP_BY Mode Set
# vim /etc/my.cnf
sql_mode=STRICT_ALL_TABLES

# MySQL May Run Slowly
# vim /etc/my.cnf
innodb_buffer_pool_size=1600M

# Server Timezone Not Configured
# vim /etc/php.ini
data.timezone = Asia/Shanghai

# Alternate File Domain Not Configured
# ... 可以不设置

# Missing Repository Local Path
mkdir -p /var/repo/
./bin/config set repository.default-local-path "/var/repo/"

# 	Install Pygments to Improve Syntax Highlighting
pip install Pygments
# 点击 pygments.enabled 在下拉框选择 Use Pygments

# Large File Storage Not Configured
# 设置使用Mysql做为存储
./bin/config set storage.mysql-engine.max-size 8388608
# vim /etc/php.ini
post_max_size=128MB
memory_limit=-1
max_input_vars=1024MB
upload_max_filesize=128MB

# PHP Extension 'APC' Not Installed
yum install php-pear php-devel httpd-devel pcre-devel gcc make
pecl install apc
# output pecl install apc
# Build process completed successfully
# Installing '/usr/include/php/ext/apc/apc_serializer.h'
# Installing '/usr/lib64/php/modules/apc.so'
# install ok: channel://pecl.php.net/APC-3.1.13
# configuration option "php_ini" is not set to php.ini location
# You should add "extension=apc.so" to php.ini
# vim /etc/php.d/apc.ini # 参考底下 参考文件apc.ini 文件内容
# 如果存在apcu.ini文件，请先移除

# Base URI Not Configured
# 按照网页提示操作配置 base.uri 的值默认为 http://your_ip_address

# No Auth Providers
# 点击链接 Auth Application 按要求配置 登录方式 与 邮验证

# Daemons Not Running
./bin/phd start
</pre>

### 邮件配置
- Config --> Core Settings --> Mail --> metamta.mail-dadpter (PhabricatorMailImplementationPHPMailerAdapter)
- Config --> Core Settings --> PHPMailer --> metamta.mail-adapter
	- phpmailer.smtp-host
	- phpmailer.smtp-port
	- phpmailer.smtp-protocol
	- phpmailer.smtp-user
	- phpmailer.smtp-password
	- phpmailer.smtp-encoding 

<pre>
./bin/config set phpmailer.smtp-host 'smtp.qq.com'
./bin/config set phpmailer.smtp-port 465
./bin/config set phpmailer.smtp-protocol SSL
./bin/config set phpmailer.smtp-user '1467220845@qq.com'
./bin/config set phpmailer.smtp-password 'your_email_password'
</pre>

### 代码仓库访问方式SSH配置
- www-user
- daemon-user
- vcs-user

<pre>
./bin/config set phd.user root
./bin/phd restart
./bin/config set diffusion.ssh-user vcsuser
</pre>

	- 设置用户登录认证方式
	- 设置邮件发送服务参数
	- 配置代码仓库访问方式:SSH/HTTP


### 参考文件
- /etc/php.d/apc.ini 文件

<pre>
; Enable apc extension module
extension = apc.so

; Options for the APC module version >= 3.1.3
; See http://www.php.net/manual/en/apc.configuration.php

; This can be set to 0 to disable APC.
apc.enabled=1
; The number of shared memory segments to allocate for the compiler cache.
apc.shm_segments=1
; The size of each shared memory segment, with M/G suffix
apc.shm_size=64M
; A "hint" about the number of distinct source files that will be included or
; requested on your web server. Set to zero or omit if you are not sure;
apc.num_files_hint=1024
; Just like num_files_hint, a "hint" about the number of distinct user cache
; variables to store.  Set to zero or omit if you are not sure;
apc.user_entries_hint=4096
; The number of seconds a cache entry is allowed to idle in a slot in case this
; cache entry slot is needed by another entry.
apc.ttl=7200
; use the SAPI request start time for TTL
apc.use_request_time=1
; The number of seconds a user cache entry is allowed to idle in a slot in case
; this cache entry slot is needed by another entry.
apc.user_ttl=7200
; The number of seconds that a cache entry may remain on the garbage-collection list.
apc.gc_ttl=3600
; On by default, but can be set to off and used in conjunction with positive
; apc.filters so that files are only cached if matched by a positive filter.
apc.cache_by_default=1
; A comma-separated list of POSIX extended regular expressions.
apc.filters
; The mktemp-style file_mask to pass to the mmap module
apc.mmap_file_mask=/tmp/apc.XXXXXX
; This file_update_protection setting puts a delay on caching brand new files.
apc.file_update_protection=2
; Setting this enables APC for the CLI version of PHP (Mostly for testing and debugging).
apc.enable_cli=0
; Prevents large files from being cached
apc.max_file_size=1M
; Whether to stat the main script file and the fullpath includes.
apc.stat=0
; Vertification with ctime will avoid problems caused by programs such as svn or rsync by making
; sure inodes have not changed since the last stat. APC will normally only check mtime.
apc.stat_ctime=0
; Whether to canonicalize paths in stat=0 mode or fall back to stat behaviour
apc.canonicalize=0
; With write_lock enabled, only one process at a time will try to compile an
; uncached script while the other processes will run uncached
apc.write_lock=1
apc.slam_defense=0
; Logs any scripts that were automatically excluded from being cached due to early/late binding issues.
apc.report_autofilter=0
; RFC1867 File Upload Progress hook handler
apc.rfc1867=0
apc.rfc1867_prefix =upload_
apc.rfc1867_name=APC_UPLOAD_PROGRESS
apc.rfc1867_freq=0
apc.rfc1867_ttl=3600
; Optimize include_once and require_once calls and avoid the expensive system calls used.
apc.include_once_override=0
apc.lazy_classes=0
apc.lazy_functions=0
; Enables APC handling of signals, such as SIGSEGV, that write core files when signaled.
; APC will attempt to unmap the shared memory segment in order to exclude it from the core file
apc.coredump_unmap=0
; Records a md5 hash of files.
apc.file_md5=0
; not documented
apc.preload_path
</pre>