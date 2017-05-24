# 利用Squid实现代理IP服务
## 目标
- 爬虫设置Squid指定的统一代理，如 http://ip:port 就可以进行爬取操作

## 实现方法与步骤
- 用scrapy爬取代理IP
- 用多线程requests过滤高质有效代理IP
- 按cache_peer格式配置squid
- 各类爬虫指定squid的服务ip:port，进行爬取

## 具体细节
- 用scrapy爬取代理IP
	- 参考 [scrap_IP](http://www.haijunt.com) github项目
	
- 用多线程requests过滤高质有效代理IP
	- pass
	
- 按cache_peer格式配置squid

- 各类爬虫指定squid的服务ip:port，进行爬取
	- pass