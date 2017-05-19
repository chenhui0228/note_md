# Scrapy探究

## 安装
- ubuntu python2
	1. sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
	2. pip install scrapy
- ubuntu python3
	1. sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
	2. sudo apt-get install python3 python3-dev
	3. pip install scrapy

## 目录结构
<pre>
tutorial/
    scrapy.cfg            # deploy configuration file
    tutorial/             # project's Python module, you'll import your code from here
        __init__.py
        items.py          # project items definition file
        pipelines.py      # project pipelines file
        settings.py       # project settings file
        spiders/          # a directory where you'll later put your spiders
            __init__.py
</pre>

## 命令行工具
- scrapy tool (command)
	- Global commands：
		- scrapy `--help`
		- scrapy `<command> -h`
		- scrapy `startproject` project_name [project_dir]
		- scrapy `genspider` [-t template] mydomain mydomain.com
		- scrapy `settings` [options]
		- scrapy `runspider` <spider_file.py>
		- scrapy `shell` [url] [options]
		- scrapy `fetch` <url>
		- scrapy `view` <url>
		- scrapy `version` [-v]

	- Project-only commands: 
		- scrapy `crawl` <spider>
		- scrapy `check` [-l] <spider>
		- scrapy `list`
		- scrapy `edit` <spider>
		- scrapy `parse` <url> [options]
		- scrapy `bench`


## 爬虫分类
- Spiders
- CrawlSpider
- XMLFeedSpider
- CSVFeedSpider
- SitemapSpider

## 选择器
- selector
- xpath

## 提取结构化数据
- Item
- Item Loaders

## 调试
- scrapy shell <content>

## 数据过滤与流向
- Item Pipeline
- Feed exports

## 请求与响应数据结构
- Requests
- Responses

## 链接器
- Link Extractors

## Settings

## 异常

## 日志

## 状态收集
- stats collection

## 发送邮件
- sending e-mail

## Telnet Console
## Web服务

## 常见问题总结
- 解析使用BeautifulSoup
- scrapy支持python2.7 or python3.3+
- 使用http代理
- 如何提取item时跨网页
- 登录页面
- 爬取设置深度优先还是广度优先
- 内存泄漏检测
- use Basic HTTP Authentication
- 下载页面本地化
- 不创建工程下运行爬虫
- 如何布署爬虫
- 如何导出成json,csv
- 调试就使用scrapy shell
- 解析 big XML/CSV 数据
- 如何使用 CookiesMiddleware
- How can I see the cookies being sent and received from Scrapy
- 如何让爬虫自己关闭(CloseSpider)
- 如何防止爬虫被禁
	- 轮流使用 user agent
	- 禁用 cookies
	- DOWNLOAD_DELAY >= 2
	- 使用 Google cache 去获取页面
	- 使用IP代理， <a href='http://scrapoxy.io/'>scrapoxy</a>,<a href='http://proxymesh.com/'>ProxyMesh</a>,<a href=''>Tor</a>,squid.
	- 使用分布式 downloader, <a href=''>Crawlera</a>
- 如何给爬虫传递参数
- Removing namespaces.
- How to realize distributed system
	- scrapy-redis
	- redispy
- How to deploy spiders
	- scrapyd
	- scrapy cloud

## 爬虫合约
## 普通运行爬虫项目
- scrapy.crawler.CrawlerProcess
	<pre>
		import scrapy
		from scrapy.crawler import CrawlerProcess
		class MySpider(scrapy.Spider):
    		# Your spider definition
    		...
		process = CrawlerProcess({
    		'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
		})
		process.crawl(MySpider)
		process.start() # the script will block here until the crawling is finished
	</pre>
	
	<pre>
		from scrapy.crawler import CrawlerProcess
		from scrapy.utils.project import get_project_settings
		process = CrawlerProcess(get_project_settings())
		# 'followall' is the name of one of the spiders of the project.
		process.crawl('followall', domain='scrapinghub.com')
		process.start() # the script will block here until the crawling is finished
	</pre>
	
	<pre>
		import scrapy
		from scrapy.crawler import CrawlerProcess
		class MySpider1(scrapy.Spider):
		    # Your first spider definition
		    ...
		class MySpider2(scrapy.Spider):
		    # Your second spider definition
		    ...
		process = CrawlerProcess()
		process.crawl(MySpider1)
		process.crawl(MySpider2)
		process.start() # the script will block here until all crawling jobs are finished
	</pre>
	
- scrapy.crawler.CrawlerRunner
	<pre>
		from twisted.internet import reactor
		import scrapy
		from scrapy.crawler import CrawlerRunner
		from scrapy.utils.log import configure_logging
		class MySpider(scrapy.Spider):
		    # Your spider definition
		    ...
		configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
		runner = CrawlerRunner()
		d = runner.crawl(MySpider)
		d.addBoth(lambda _: reactor.stop())
		reactor.run() # the script will block here until the crawling is finished
	</pre>
	
	<pre>
		import scrapy
		from twisted.internet import reactor
		from scrapy.crawler import CrawlerRunner
		from scrapy.utils.log import configure_logging
		class MySpider1(scrapy.Spider):
		    # Your first spider definition
		    ...
		class MySpider2(scrapy.Spider):
		    # Your second spider definition
		    ...
		configure_logging()
		runner = CrawlerRunner()
		runner.crawl(MySpider1)
		runner.crawl(MySpider2)
		d = runner.join()
		d.addBoth(lambda _: reactor.stop())
		reactor.run() # the script will block here until all crawling jobs are finished
	</pre>
	
	</pre>
		from twisted.internet import reactor, defer
		from scrapy.crawler import CrawlerRunner
		from scrapy.utils.log import configure_logging
		class MySpider1(scrapy.Spider):
		    # Your first spider definition
		    ...
		class MySpider2(scrapy.Spider):
		    # Your second spider definition
		    ...
		configure_logging()
		runner = CrawlerRunner()
		@defer.inlineCallbacks
		def crawl():
		    yield runner.crawl(MySpider1)
		    yield runner.crawl(MySpider2)
		    reactor.stop()
		crawl()
		reactor.run() # the script will block here until the last crawl call is finished
	</pre>


## Difficulty
- Twisted
- Item Loaders
- Web Service 