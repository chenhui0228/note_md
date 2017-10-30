# Scrapy使用总结
### 进行调研与调试
```
scrapy fetch --nolog http://www.example.com/some/page.html
scrapy parse --spider=myspider -c parse_item -d 2 <item_url>
scrapy shell 'http://quotes.toscrape.com'
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x102e39a90>
[s]   item       {}
[s]   request    <GET https://www.guazi.com/hf/buy>
[s]   response   <203 https://www.guazi.com/hf/buy>
[s]   settings   <scrapy.settings.Settings object at 0x102e39890>
[s]   spider     <DefaultSpider 'default' at 0x103b1a690>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser

response.css('div.quote').extract_first()
response.xpath('xpath').extract_first()
```

### 工程跑程序
```
$ scrapy startproject tutorial
$ cd tutorial
$ scrapy generator example example.com

import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield scrapy.Request(url='https://baidu.com', callback=self.parse)
            yield response.follow(next_page, self.parse)
            
$ scrapy crawl list
$ scrapy crawl quotes
```

### 单脚本跑程序
```
$ scrapy runspider my_spider.py

# singlespider.py
import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider(scrapy.Spider):
    # Your spider definition
    ...

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MySpider)
process.crawl(MySpider2)
process.start() # the script will block here until the crawling is finished
$ python singlespider.py

# or
# test_runner.py
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
$ python test_runner.py

```
### 分布式爬取
```
# scrapy_redis_text.py
import datetime
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy_redis.spiders import RedisSpider
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from bs4 import BeautifulSoup

class HefeiSpider(RedisSpider):
    name = 'mfw'
    allowed_domains = ['mafengwo.cn']
    host = 'http://www.mafengwo.cn'
    redis_key = 'mfw:start_urls'

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'SCHEDULER': "scrapy_redis.scheduler.Scheduler",
        #确保所有的爬虫通过Redis去重
        'DUPEFILTER_CLASS': "scrapy_redis.dupefilter.RFPDupeFilter",
        #最大空闲时间防止分布式爬虫因为等待而关闭
        'SCHEDULER_IDLE_BEFORE_CLOSE' :10,
        # 调度状态持久化，清理redis缓存
        'SCHEDULER_PERSIST': False,
        #将清除的项目在redis进行处理
        'ITEM_PIPELINES': {
            'scrapy_redis.pipelines.RedisPipeline': 301
            # 'MongoPipeline' : 301
        },
        'DOWNLOAD_DELAY' : 2.4,
        #指定连接到redis时使用的端口和地址（可选）
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': 6379,
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

        def start_requests(self):
	        yield scrapy.FormRequest(
	            url='http://www.mafengwo.cn/ajax/router.php',
	            formdata={},
	            callback=self.parse
        		)

    def parse(self, response):
        pass


if __name__ == '__main__':
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    runner = CrawlerRunner()
    d = runner.crawl(HefeiSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run() # the script will block here until the crawling is finished
$ python scrapy_redis_text.py

```
### 避免空爬
```
raise CloseSpider

# 针对scrapy-redis分布式版本在 scrapy-redis/spider的next_requests加入：
if found == 0:
    self.crawler.engine.close_spider('queue is empty, the spider close')
```
### 如何设定缓存机制
```
SCHEDULER_PERSIST = True
# 延迟1秒下载
DOWNLOAD_DELAY = 1
```
### 保存数据到JSON/CSV/XML file
```
scrapy crawl myspider -o itmes.json -a tag=humor
```