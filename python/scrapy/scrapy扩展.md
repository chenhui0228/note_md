# Scrapy 扩展
## 架构预览
![](https://docs.scrapy.org/en/latest/_images/scrapy_architecture_02.png)

1. engine从某个spider里得到初始请求(start_url:requests)
2. engine将初始请求全部给scheduler,并向scheduler请求下个请求(request对象)
3. scheduler进行调度并返回一个请求(request对象)给engine
4. engine将请求(request对象)传给Downloader.(中间可以通过多个下载中间件 see process_request())
5. Downloader选择合适的处理器进行网络访问，并将响应(response对象)(中间可以通过多个下载中间件 see process_response())返回给engine
6. engine将响应(response对象)传给spider，并由对应设置好的回调解析函数(parse)进行解析(中间可以通过多个抓取中间件(see process_spider_input())
7. spider将解析的结果Item对象或者Request对象(中间可以通过多个抓取中间件(see process_spider_output())返回给engine
8. engine将spider产生的(yield语句)Item对象(dict对象也行)传给Item Pipelines,将spider产生的请求(request对象)传给Scheduler，并向Scheduler请求下个请求(request对象)
9. 重复(从步骤1开始，而不是从3开始)，直到Scheduler给不出请求(request对象)

- Scrapy Engine

	engine控制了整个数据流过程，并且当特定的事件发生时会触发另一个事件的开始
- Scheduler

	Scheduler从engine获取requests，并入队进行调度，当engine有需要时及时供给
- Downloader

	Downloader(下载器)去抓取网页并将响应传递给engine
- Spiders

	爬虫其实是特定的类，你得定义某些变量(start_url)实现某些方法(parse),并对响应进行解析，以便提取出响应体中有用的结构化的数据，或者新的request，以便补充requests
- Item Pipeline

	数据管道是对结构化的数据进行加工，清洗或者入库等操作
- Downloader middlewares

	下载中间件位于Engine与Downloader中间，可以对request,response进行加工，如设置用户代理，IP代理，过滤某些request,response.
- Spider middlewares

	抓取中间件位于Engine与Spiders中间，可以加工response,item,requests.如过滤添加删除某些item,requests,处理spider异常，如发生错误时调用邮件通知，发送某个特别信号。


## 下载中间件
- 如何自定义下载中间件(按要求写好类，并在配置文件里标注)


	```python
	# myproject/middlewares.py
	
	class CustomDownloaderMiddleware:
		
		def process_request(request, spider):
			return None or Request() or Response()
			raise IgnoreRequest
			
		def process_response(request, response, spider):
			return Response() or Request()
			raise IgnoreRequest
			
		def process_exception(request, exception, spider):
			return None or Response() or Request()	
	```
	```python
	# setting.py
	
	DOWNLOADER_MIDDLEWARES = {
	    'myproject.middlewares.CustomDownloaderMiddleware': 543,
	    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
	}
	```
- 框架自带的下载中间件(可以通过setting.py进行设置打开或者关闭某些中间件)
	- CookiesMiddleware
	- DefaultHeadersMiddleware
	- DownloadTimeoutMiddleware
	- HttpAuthMiddleware
	- HttpCacheMiddleware
	- HttpCompressionMiddleware
	- HttpProxyMiddleware
	- RedirectMiddleware
	- MetaRefreshMiddleware
	- RetryMiddleware
	- RobotsTxtMiddleware
	- DownloaderStats
	- UserAgentMiddleware
	- AjaxCrawlMiddleware

	
## 抓取中间件
- 如何自定义下载中间件(按要求写好类，并在配置文件里标注)
	
	```python
	# myproject/middlewares.py
	class CustomSpiderMiddleware:
	
		def process_spider_input(response, spider):
			return None
			raise exception
			
		def process_spider_output(response, result, spider):
			yield Item()
			yield Request()
			
		def process_spider_exception(response, exception, spider):
			yield Response()
			yield Item()
			
		def process_start_requests(start_requests, spider):
			yield requests
			
	```
	```python
	# setting.py
	
	SPIDER_MIDDLEWARES = {
    	'myproject.middlewares.CustomSpiderMiddleware': 543,
    	'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': None,
	}
	```
- 框架自带的抓取中间件
	- DepthMiddleware
	- HttpErrorMiddleware
	- OffsiteMiddleware
	- RefererMiddleware
	- UrlLengthMiddleware

## 扩展
- 自定义扩展

	```python
	# myproject/myextensions.py
	
	import logging
	from scrapy import signals
	from scrapy.exceptions import NotConfigured
	
	logger = logging.getLogger(__name__)
	
	class SpiderOpenCloseLogging(object):
	
	    def __init__(self, item_count):
	        self.item_count = item_count
	        self.items_scraped = 0
	
	    @classmethod
	    def from_crawler(cls, crawler):
	        # first check if the extension should be enabled and raise
	        # NotConfigured otherwise
	        if not crawler.settings.getbool('MYEXT_ENABLED'):
	            raise NotConfigured
	
	        # get the number of items from settings
	        item_count = crawler.settings.getint('MYEXT_ITEMCOUNT', 1000)
	
	        # instantiate the extension object
	        ext = cls(item_count)
	
	        # connect the extension object to signals
	        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
	        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
	        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)
	
	        # return the extension object
	        return ext
	
	    def spider_opened(self, spider):
	        logger.info("opened spider %s", spider.name)
	
	    def spider_closed(self, spider):
	        logger.info("closed spider %s", spider.name)
	
	    def item_scraped(self, item, spider):
	        self.items_scraped += 1
	        if self.items_scraped % self.item_count == 0:
	            logger.info("scraped %d items", self.items_scraped)
	```
	```python
	# setting.py
	
	EXTENSIONS = {
		'myproject.myextensions.SpiderOpenCloseLogging': 500,
	  	'scrapy.extensions.corestats.CoreStats': 500,
	   	'scrapy.extensions.telnet.TelnetConsole': 500,
	}
	```

- 框架自带的扩展
	- scrapy.extensions.logstats.LogStats
	- scrapy.extensions.corestats.CoreStats
	- scrapy.extensions.telnet.TelnetConsole
	- scrapy.extensions.memusage.MemoryUsage (not work in windows)
	- scrapy.extensions.memdebug.MemoryDebugger
	- scrapy.extensions.closespider.CloseSpider
	- scrapy.extensions.statsmailer.StatsMailer
	- scrapy.extensions.debug.StackTraceDump (only work in POSIX,ie. not windows)
	- scrapy.extensions.debug.Debugger (only work in POSIX,ie. not windows)
	
## 核心api
- Crawler API
	- scrapy.crawler.Crawler(spidercls, settings)
		- settings
		- signals
		- stats
		- extensions
		- engine
		- spider
		- crawl(*args, **kwargs)
	- scrapy.crawler.CrawlerRunner(settings=None)
		- crawlers
		- create_crawler(crawler_or_spidercls)
		- join()
		- stop()
	- scrapy.crawler.CrawlerProcess(settings=None)
		- crawlers
		- create_crawler(crawler_or_spidercls)
		- join()
		- start(stop_after_crawl=True)
		- stop()
- Settings API
	- SETTINGS_PRORITIES
	- get_settings_priority(priority)
	- scrapy.settings.Settings(values=None, priority='project')
	- scrapy.settings.BaseSettings(value=None, priority='project')
		- copy()
		- copy_to_dict()
		- freeze()
		- frozencopy()
		- get(name, default=None)
		- getbool(name, default=False)
		- getdict(name, default=None)
		- getfloat(name, default=0.0)
		- getint(name, default=0)
		- getlist(name, default=None)
		- getpriority(name)
		- getwithbase(name)
		- maxpriority()
		- set(name, value, priority='project')
		- setmodule(module, priority='project')
		- update(value, priority='project')

- SpiderLoader API
	- scrapy.loader.SpiderLoader
		- from_settings(settings)
		- load(spider_name)
		- list()
		- find_by_request(request)
		
- Signals API
	- scrapy.signalmanager.SignalManager(sender=_Anonymous)
		- connect(receiver, signal, **kwargs)
		- disconnect(receiver, signal, **kwargs)
		- disconnect_all(signal, **kwargs)
		- send_catch_log(signal, **kwargs)
		- send_catch_log_deferred(signal, **kwargs)

- Stats Collector API
	- scrapy.statscollectors.StatsCollector
		- get_value(key, default=None)
		- get_stats()
		- set_value(key, value)
		- set_stats(stats)
		- inc_value(key, count=1, start=0)
		- max_value(key, value)
		- min_value(key, value)
		- clear_stats()
		- open_spider(spider)
		- close_spider(spider)
			
			
## 信号
- ie.

	```python
	from scrapy import signals
	from scrapy import Spider
	
	
	class DmozSpider(Spider):
	    name = "dmoz"
	    allowed_domains = ["dmoz.org"]
	    start_urls = [
	        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
	        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
	    ]
	
	
	    @classmethod
	    def from_crawler(cls, crawler, *args, **kwargs):
	        spider = super(DmozSpider, cls).from_crawler(crawler, *args, **kwargs)
	        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
	        return spider
	
	
	    def spider_closed(self, spider):
	        spider.logger.info('Spider closed: %s', spider.name)
	
	
	    def parse(self, response):
	        pass
	```
	
- 内建信号参考
	- scrapy.signals.engine_started()
	- scrapy.signals.engine_stopped()
	- scrapy.signals.item_scraped(item, response, spider)
	- scrapy.signals.item_dropped(item, response, exception, spider)
	- scrapy.signals.spider_closed(spider, reason)
	- scrapy.signals.spider_opened(spider)
	- scrapy.signals.spider_idle(spider)
	- scrapy.signals.spider_error(failure, response, spider)
	- scrapy.signals.request_scheduled(request, spider)
	- scrapy.signals.request_dropped(request, spider)
	- scrapy.signals.response_received(response, request, spider)
	- scrapy.response_downloaded(response, request, spider)
	