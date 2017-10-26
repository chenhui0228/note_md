# selenium+chromedriver爬取天眼查
	
网页数据，可见即可得。只是得到它的代价因为可见的代价增加而增加。目前天眼查网站很多数据需要登录功能才能访问，还有的需要购买VIP服务才能够访问。但一些基本信息不登录也能够查得到，而且在较低的访问频率下，不会被封IP。本python3程序ex_tyc.py利用selenium+chromedriver驱动浏览器实现模拟登录功能，实现js执行(如下划到页面底部),实现基本信息的爬取并存储到mongodb数据库。并可在centos等无界面的服务上部署爬取。目前提供的为单机版本，分布式的以后分享。

### 输入与输出
- 目标： 爬取天眼查网站企业详细数据
- 输入： 企业名单
- 输出： json格式数据到mongodb数据库

### 环境要求
	- python3.5
	- google-chrome-stable or (chrome浏览器（本地）)
	- chromedriver (Version 2.32)
	- selenium (version: 2.53.6)
	- Xvfb  (虚拟桌面)
	- mongodb

### 安装环境
```
	# 1. 利用虚拟环境库安装python环境与使用到的python库
	pip install virtualenv
	virtualenv --python=python3 vpy3
	source vpy3/bin/activate
	pip3 install -r requirements.txt  # 内容在下面
```

```
	# 2. 在centos下安装Chrome浏览器
	cd /etc/yum.repos.d/
	vim google-chrome.repo  # 内容在下面
	yum -y install google-chrome-stable --nogpgcheck
```

```
	# 3. 在centos下安装虚拟桌面
	yum install -y Xvfb
```

```
	# 4. 安装mongodb数据库，并启动服务端
	yum -y install mongodb
	mongod
```

```
	# 5. 在centos下载Chrome浏览器驱动二进制程序chromedriver，并放到环境目录下。
	# 注意下载对应OS版本的chromedriver,下面是linux版本的,google搜索chromedriver下载即可
	wget https://chromedriver.storage.googleapis.com/2.32/chromedriver_linux64.zip
	unzip chromedriver_linux64.zip
	cp chromedriver /usr/local/bin/
```

```
	# 6. 这一步一定要做，升级系统软件与各依赖，不然有可能chromedriver在驱动Chrome时会出现错误。
	yum -y update
```

```
	# 7. 在centos等无界面上需要导入系统环境变量。在本机就不用导入
	# 如果不导入，确保本机有界面的浏览器，及本地有mongod服务是开启的
	export CHROME_DRIVER_ENV=1
	export MONGO_ENV
```

```
	# google-chrome.repo  content
	[google-chrome]
	name=google-chrome
	baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64
	enabled=1
	gpgcheck=1
	gpgkey=https://dl.google.com/linux/linux_signing_key.pub
```

```
	# requirements.txt content
	selenium
	bs4
	xvfbwrapper
	pymongo
```

### 开跑程序
```
	# 确保各python库已经安装好，并使用yum -y update命令升级各依赖
	# 如果需要使用登录功能，把注释打开即可
	python3 ex_tyc.py
```

```
# coding:utf8
# ex_tyc.py
# __author__ = u'码码要洗手'

import os
import time
import pymongo
import traceback
from pprint import pprint
from xvfbwrapper import Xvfb
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
try:
    from urllib import urlencode
except:
    from urllib.parse import urlencode


ent_fix = [
'鼎捷软件股份有限公司',
'百度网讯科技有限公司'
]


# class TianyanchaLogin(object):

#     def __init__(self):
#         try:
#             self.driver = None
#             dcap = dict(DesiredCapabilities.PHANTOMJS)
#             dcap["phantomjs.page.settings.userAgent"] = (
#                 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
#             )
#             self.driver = webdriver.Chrome(desired_capabilities=dcap)
#             self.driver.implicitly_wait(10)

#             self.driver.get('https://www.tianyancha.com/login')
#             time.sleep(8.0)
#             element = self.driver.find_element_by_xpath('//*[@id="web-content"]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input')
#             element.clear()
#             element.send_keys(u'your_username')
#             element = self.driver.find_element_by_xpath('//*[@id="web-content"]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/input')
#             element.clear()
#             element.send_keys(u'your_password')
#             element = self.driver.find_element_by_xpath('//*[@id="web-content"]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[5]')
#             element.click()
#             time.sleep(8.0)
#         except Exception:
#             print(traceback.format_exc())
#             if self.driver:
#                 self.driver.close()


class TianyanchaClawer(object):

    def __init__(self):

        self.driver = None
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
        )
        self.env = os.environ.get('CHROME_DRIVER_ENV')
        if self.env:
            self.vdisplay = Xvfb()
            self.vdisplay.start()
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-setuid-sandbox")
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        else:
            self.driver = webdriver.Chrome(desired_capabilities=self.dcap)

        # loginer = TianyanchaLogin()
        # self.driver = loginer.driver

        self.driver.implicitly_wait(10)

        self.mongo_env = os.environ.get('MONGO_ENV')
        if self.mongo_env:
            self.client = pymongo.MongoClient(host="mongodb://10.3.0.27", port=27017)
        else:
            self.client = pymongo.MongoClient()
        self.db = self.client['db_tyc']

    def run(self):
        for i, ent in enumerate(ent_fix):
            time.sleep(5.0)
            try:
                # 搜索公司
                data = {'key': ent}
                comp_link = u'https://www.tianyancha.com/search?' + urlencode(data)
                self.driver.get(comp_link)
                time.sleep(15)

                # 访问公司详细信息的网址
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                div = soup.find('div', attrs={'class': 'search_right_item'})
                if not div:
                    print(ent)
                    print(u'没有公司该公司的url!!!!!!!!!')
                    continue
                a = div.find('a')
                href = a['href']
                comp_link = href
                self.driver.get(comp_link)
                time.sleep(10.0)

                # 划动到最底边，让浏览器加载js脚本并执行
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                time.sleep(8)

                # 从页面提取结构化信息
                result = self.parse_page(self.driver)
                result[u'公司名称'] = ent
                result['url'] = href
                result['order_num'] = str(i)
                pprint(result)

                # 插入到mongodb数据的集合中
                # self.db['db_tyc_collection_result'].insert(result)
                time.sleep(6.0)
            except Exception:
                print(traceback.format_exc())
                continue
        if self.driver:
            time.sleep(10.0)
            self.driver.close()

    def parse_page(self, driver):
        result = {}
        try:
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            # 解析 ’企业背景，企业发展，司法风险，经营风险，经营状况，知识产权‘信息
            divs = soup.find_all('div', attrs={"class": "nav_item_Box"})
            for div in divs:
                ch_divs = div.find_all('div', attrs={"class": 'company-nav-item-enable'})
                for ch_div in ch_divs:
                    text = ch_div.get_text().strip()
                    if ch_div.find('span'):
                        span_text = ch_div.find('span').get_text().strip()
                        result[text.replace(span_text, '')[:4]] = span_text
                    else:
                        result[text] = '0'
                ch_divs = div.find_all('div', attrs={"class": 'company-nav-item-disable'})
                for ch_div in ch_divs:
                    text = ch_div.get_text().strip()
                    result[text[:4]] = '0'

            # 解析 ’基本信息‘
            divs = soup.find_all('div', attrs={"class": "baseinfo-module-content-value"})
            ths = [u'注册资本', u'注册时间', u'企业状态']
            tds = [div.get_text().strip() if div.get_text() else None for div in divs]
            result.update(dict(zip(ths, tds)))

            # 解析 ’基本信息-查看详情‘信息
            div = soup.find('div', attrs={"class": 'base0910'})
            all_ths = []
            all_tds = []
            if div:
                trs = div.find_all('tr')
                for tr in trs:
                    ths = tr.find_all('td', attrs={'class': 'table-left'})
                    for th in ths:
                        text = th.get_text().strip()
                        if th.find('span'):
                            span_text = th.find('span').get_text().strip()
                            text = text.replace(span_text, '')
                        all_ths.append(text)
                    tds = tr.find_all('td', attrs={'class': False})
                    for td in tds:
                        text = td.get_text().strip()
                        all_tds.append(text)
                    feng = tr.find('td', attrs={'class': 'text-center'})
                    if feng and feng.find('img'):
                        all_ths.append(u'评分')
                        all_tds.append(feng.find('img')['alt'][2:])
            result.update(dict(zip(all_ths, all_tds)))

            # 解析 ’基本信息-天眼风险‘信息
            div = soup.find('div', attrs={"class": "tyfxBox"})
            if div:
                divs = div.find_all('div', attrs={"class": 'f18'})
                for i, item in enumerate(divs):
                    text = item.get_text().strip()
                    if i==0:
                        result[u'自身风险'] = item.find('span', attrs={"class": 'new-err'}).get_text().strip()
                    else:
                        result[u'周边风险'] = item.find('span', attrs={"class": 'new-err'}).get_text().strip()
                if u'自身风险' not in result.keys():
                    divs = div.find_all('div', attrs={"class": 'mr20'})
                    for i, item in enumerate(divs):
                        text = item.get_text().strip()
                        if i==0:
                            result[u'自身风险'] = item.find('span', attrs={"class": 'new-err'}).get_text().strip()
                        else:
                            result[u'周边风险'] = item.find('span', attrs={"class": 'new-err'}).get_text().strip()

        except Exception:
            print(traceback.format_exc())
        return result


if __name__ == "__main__":
    clawer = TianyanchaClawer()
    clawer.run()
```

```
# 爬取数据样例
{'order_num': '0',
 'url': 'https://www.tianyancha.com/company/7930073',
 '上市公告': '99+',
 '专利': '28',
 '严重违法': '0',
 '主要人员': '12',
 '产品信息': '0',
 '企业业务': '1',
 '企业关系': '',
 '企业年报': '4',
 '企业状态': '存续（在营、开业、在册）',
 '企业简介': '',
 '企业类型': '股份有限公司（中外合资、上市）',
 '作品著作': '0',
 '债券信息': '0',
 '公司名称': '鼎捷软件股份有限公司',
 '分支机构': '4',
 '分红情况': '8',
 '动产抵押': '0',
 '十大流通': '5',
 '十大股东': '5',
 '参股控股': '18',
 '发行相关': '',
 '变更记录': '20',
 '司法拍卖': '0',
 '周边风险': '24',
 '商标信息': '99+',
 '基本信息': '',
 '失信人': '0',
 '对外投资': '10',
 '工商注册号': '310000400286578',
 '开庭公告': '0',
 '微信公众': '3',
 '投资事件': '0',
 '抽查检查': '0',
 '招投标': '0',
 '招聘': '99+',
 '核准日期': '2001-12-26',
 '核心团队': '0',
 '欠税公告': '0',
 '法律诉讼': '26',
 '法院公告': '4',
 '注册地址': '上海市静安区江场路1377弄7号20层',
 '注册时间': '2001-12-26',
 '注册资本': '26096.9943万人民币',
 '登记机关': '上海市工商行政管理局',
 '税务评级': '4',
 '竞品信息': '10',
 '纳税人识别号': '310000734084709',
 '组织机构代码': '734084709',
 '经营异常': '0',
 '经营范围': '研究、开发和生产计算机软件系统、硬件及配套零部件、网络产品、多媒体产品、办公自动化设备、仪器仪表、电器及印刷照排设备；计算机系统集成和计算机应用系统的安装及维修，销售自产产品，并提供相关的技术转让和技术培训；从事上述同类产品的批发、佣金代理（拍卖除外）、进出口及相关技术咨询和配套服务。【依法须经批准的项目，经相关部门批准后方可开展经营活动】研究、开发和生产计算机软件系统、硬件及配套零部件、网络产品、多媒体产品、办公自动化设备、仪器仪表、电器及印刷照排设备；计算机系统集成和计算机应用系统的安装及维修，销售自产产品，并提供相关的技术转让和技术培训；从事上述同类产品的批发、佣金代理（拍卖除外）、进出口及相关技术咨询和配套服务。【依法须经批准的项目，经相关部门批准后方可开展经营活动...详细',
 '统一信用代码': '91310000734084709Q',
 '网站备案': '2',
 '股东信息': '22',
 '股本变动': '14',
 '股本结构': '7',
 '股权出质': '0',
 '股票行情': '',
 '自身风险': '15',
 '英文名称': 'Digiwin Software Co.,Ltd.',
 '营业期限': '2001-12-26至无固定期限',
 '融资历史': '1',
 '行业': '软件和信息技术服务业',
 '行政处罚': '0',
 '被执行人': '1',
 '评分': '98',
 '购地信息': '0',
 '资质证书': '2',
 '软件著作': '54',
 '进出口信': '1',
 '配股情况': '0',
 '高管信息': '12'}
```

- 我记得会实现分布式版本的！！！！！！！！！！！！！！