# Scrapy Study

## How to Install
- ubuntu python2
	1. sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
	2. pip install scrapy
- ubuntu python3
	1. sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
	2. sudo apt-get install python3 python3-dev
	3. pip install scrapy

## Feature
- Single
- The kind of spiders
	- Spiders
	- CrawlSpider
	- XMLFeedSpider
	- CSVFeedSpider
	- SitemapSpider
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

## How to realize distributed system
- scrapy-redis
- redispy

## How to deploy spiders
- scrapyd
- scrapy cloud

## Difficulty
- Twitter
- Item Loaders
- Web Service 