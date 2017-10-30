# python模板程序整理

### python发送邮件装饰器
- 使用方法

```
import send_email

@send_email
def fun():
    return 1/0
if __name__ == "__main__":
    fun()
```
- 程序脚本

```
# coding: utf8

import os
import functools
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import traceback

def send_email(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        try:
            func(*args, **kw)
        except Exception as e:
            sender = 'forget_tian@sina.com'
            password = os.environ.get('PASSWORD_SINA_COM', '123456')
            all_receivers = ['haijunt@princetechs.com', 'zhiyuanh@princetechs.com']
            subject = '%s 爬虫运行出错了' % (func.__name__)
            words = traceback.format_exc()
            smtpserver = 'smtp.sina.com'

            for receiver in all_receivers:
                msg = MIMEText(words, 'plain', 'utf-8')
                msg['Subject'] = Header(subject, 'utf-8')
                msg['from'] = sender
                msg['to'] = receiver

                smtp = smtplib.SMTP()
                smtp.connect('smtp.sina.com')
                smtp.login(sender, password)
                smtp.sendmail(sender, receiver, msg.as_string())
            smtp.quit()
    return wrapper
```

### python从mongodb导出数据为csv格式(权限数据层为1)
- 运行方式

```
python mongo2csv.py
```
- 程序脚本

```
# coding:utf8
import pymongo
import traceback
import codecs

client = pymongo.MongoClient()
db = client['hefei_tyc']

# with codecs.open('result_utf8.csv', 'w', 'utf8') as f:
with codecs.open('result_gb18030.csv', 'w', 'gb18030') as f:
	maxs = 0
	title = []
	for item in db['hefei_tyc_data_again'].find():
		if (len(item.keys()) > maxs):
			maxs = len(item.keys())
			title = item.keys()
	title.pop(title.index('_id'))
	f.write(','.join(title))
	f.write('\n')

	for item in db['hefei_tyc_data_again'].find():
		body = []
		for key in title:
			body.append(item.get(key, 'unknown').replace(',', ';'))
		f.write(','.join(body))
		f.write('\n')
```

### python从csv数据导入mongodb
- 运行方式

```
python2 csv2mongo.py
```

- 程序脚本

```
# coding: utf8
import csv
import codecs
import pymongo
from pprint import pprint
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

client = pymongo.MongoClient()
db = client['hefei_tyc']

with codecs.open('result3_gb18030.csv', 'r', 'gb18030') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
    	result = dict(zip(headers, row))
    	db['test_csv2mongo_coll'].insert(result)
```

### ...