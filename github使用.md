# github使用
- 注册账户以及创建仓库
	- [https://github.com](https://github.com)
	- create a New Repository
- git安装与配置
	- 安装
	<pre>
		sudo apt-get install git
	</pre>
		
	- 添加公钥到github并测试
	<pre>
		ssh-keygen -t rsa -C 'your_email@youremail.com'
		ssh -T git@github.com  # 检测是否能连接上github
	</pre>
		
	- 设置user.name和user.email
	<pre>
		git config --global user.name 'your name'
		git config --global user.email 'your_email@youremail.com'
	</pre>
	
	- 上传仓库远端或者克隆仓库到本地
	<pre>
		git remote add origin git@github.com:yourName/yourRepo.git # 上传
		git clone https://github.com/username:what.git
	</pre>