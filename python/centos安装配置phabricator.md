# centos安装配置phabricator

### 路线图
- 安装
- 配置
- Code Review
- 与GitHub集成
- 与Jenkins集成

### LNMP环境的安装
- `yum -y install nginx`
- `service nginx start`

- yum install httpd -y
- systemctl enable httpd.service
- systemctl start httpd.service

---

- wget https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm
- md5sum mysql57-community-release-el7-9.noarch.rpm
- sudo rpm -ivh mysql57-community-release-el7-9.noarch.rpm
- sudo yum install -y mysql-server
- sudo systemctl start mysqld
- sudo systemctl status mysqld
- sudo grep 'temporary password' /var/log/mysqld.log
- sudo mysql_secure_installation
- mysql -u root -p

---

- sudo yum install -y php php-mysql php-gd php-curl php-apc php-cli -y
- yum install git

### 配置

- mkdir /var/www/html/myapp
- cd /var/www/html/myapp

- git clone https://github.com/phacility/libphutil.git
- git clone https://github.com/phacility/arcanist.git
- git clone https://github.com/phacility/phabricator.git

- vim /etc/httpd/conf/httpd.conf

<pre>
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

- cd phabricator
- ./bin/config set mysql.host localhost
- ./bin/config set mysql.user root
- ./bin/config set mysql.pass your_mariadb_root_password
- ./bin/storage upgrade --user root --password your_mariadb_root_password

- systemctl restart mysqld

- yum install php-mbstring
- systemctl restart httpd