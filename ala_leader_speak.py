# coding:utf8

import pymongo
import re
from collections import Counter

cur = pymongo.MongoClient()
db = cur.beihai_leader

positions = [u'书记', u'总书记', u'董事长', u'省长', u'市长', u'厅长', u'主席', u'常委']
leader = {
    '李延强': '市长',
    '习近平': '总书记',
    '蔡中平': '书记',
    '谢庆华': '董事长',
    '陈勋': '市长',
    '王乃学': '厅长',
    '温卡华': '政协副主席',
    '柳金红': '总工会书记',
}
c = Counter()
count = 0
for item in db.leader_speak.find():
    title = item.get('a_title')
    content = item.get('content')
    for position in positions:
        m = re.search(r'，(.*)(%s)(.*)，' % (position,), content)
        if m:
            count += 1
            c['%s' % (m.group(2),)] += 1
            c['%s' % (m.group(1)[-3:],)] += 1
            c['%s' % (m.group(3)[:3],)] += 1
            print ('%s:%s:%s' %(m.group(1)[-3:], m.group(2), m.group(3)[:3]))

print('total: %s' % (db.leader_speak.find().count(), ))
print('key_count: %s' %(count,))
for k, v in c.items():
    print(k, v)
