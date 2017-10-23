# supervisor配置模板
<p>
<a href="http://supervisord.org">Supervisor</a> 是一个用Python实现的进程管理工具，可以很方便的用来启动、重启、关闭进程（不仅仅是Python进程）。除了对单个进程的控制，还可以同时启动、关闭多个进程，比如很不幸的服务器出问题导致所有应用程序都被杀死，此时可以用supervisor同时启动所有应用程序而不是一个一个地敲命令启动。非常方便。更多配置信息可以参考网址：<a href="http://supervisord.org/index.html">http://supervisord.org/index.html</a>
</p>
1. 安装supervisor
<pre>
pip install supervisor
</pre>
2. 生成配置文件
<pre>
# 如果有supervisord.conf文件，记得先备份
echo_supervisord_conf > /etc/supervisord.conf
# vim /etc/supervisord.conf G(到最后)
[include]
file=/etc/supervisor/conf.d/*.conf
</pre>
3. 启动
<pre>
supervisord -c /etc/supervisord.conf
</pre>
4. 添加监控进程
<pre>
# vim /etc/supervisor/con.d/schedule.conf
[program:schedule_all_p3]
command=/home/webapps/vpy3/bin/python3 schedule_all_p3.py
stderr_logfile=/var/log/supervisor/schedule_all_p3.log
stdout_logfile=/var/log/supervisor/schedule_all_p3.log
directory=/home/webapps/clawer_hefei/spiders
autostart=true
user=root
autorestart=true
;配置环境变量
environment=CHROME_DRIVER_ENV="1",MONGO_ENV="1",PASSWORD_SINA_COM="***"
</pre>
5. 重载
<pre>
supervisorctl reload
</pre>
6. 其它管理命令
<pre>
supervisorctl status # 查看监控进程状态
supervisorctl stop program_1  # 关闭某个进程
supervisorctl start program_1 # 启动某个进程
supervisorctl restart all  # 重启所有监控进程
supervisorctl reread # 读取有更新（增加）的配置文件，不会启动新添加的程序
supervisorctl update ＃ 重启配置文件修改过的程序
</pre>