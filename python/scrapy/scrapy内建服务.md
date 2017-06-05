# Scrapy内建服务
## Logging
- 日志与python的内建loggings模块一致
- 日志级别
	- logging.CRITICAL
	- logging.ERROR
	- logging.WARNING
	- logging.INFO
	- logging.DEBUG
- 如何使用

	```python
	import scrapy
	
	class MySpider(scrapy.Spider):
		name = 'myspider'
		start_urls = ['http://scrapinghub.com']
			
		def parse(self, response):
		   self.logger.info('Parse function called on %s', response.url) 
	```
	```python
	```
## Stats Collection
## Sending e-mail
## Telnet Console
## Web Service