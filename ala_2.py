# coding:utf8

import pymongo
import re
import requests
from collections import Counter
from bs4 import BeautifulSoup

cur = pymongo.MongoClient()
db = cur.beihai_leader

positions = [u'书记', u'总书记', u'董事长', u'省长', u'市长', u'厅长', u'主席', u'常委']
leader = {
    '李延强': '市长',
    '习近平': '国家主席总书记',
    '蔡中平': '书记',
    # '谢庆华': '董事长',
    '陈勋': '北海市副市长',
    '王乃学': '商务厅厅长',
    '温卡华': '政协副主席',
    '柳金红': '总工会书记',
    '王可': '市委书记',
    '林青山': '市长',
    '陈武': '自治区主席',
    '玉明海': '北海市副市长',
    # '芮晓武': 'xxx',
    '王小东': '北海市委书记',
    '纪伟昕': 'xxx',
    # '索耀宗': 'xxx',
    # '陈万馨': 'xx厅长',
    '余远牧': '主席团主席',
    '刘红洲': '党委书记',
    '郝伟生': '纪委书记',
    '李蔚': '政协主席',
    '赵乐秦': '市委书记',
    '李厅波': '人社厅厅长',
    '彭清华': '党委书记',
    # '赵增': 'xxx',
    '陈维': '常务副主席',
    # '李贤谋': 'xxx尾市副市长',
    # '胡春华': '广东省市长',
    # '吴玉斌': 'xx副主席',
    '石昆': '副市长',
    '市委书记': '何辛幸',
    '梁丁丁': '党委书记',
    '陈维': '副市长',
    '刘新国': '管委会书记',
    '李宁波': '人社厅厅长',
    '马新风': '工会主席',
    '曾子祥': '副市长',
    # '陈刚': 'xxx主席',
    '李昌华': '副厅长',
    # '蒋巨峰': 'xx省长',
    '刘宏武': '副市长',
    # '汪洋': '广东省委书记',
    '马继宪': '商务厅副厅长',
    '周家斌': '市长',
    # '王正伟': 'xx主席',
    # '谢迺': 'xx科技厅厅长',
    # '蓝天立': 'xx治区副主席',
    '孙来燕': '监事会主席',
    '郭声琨': 'xx书记',
    '马飚': 'xxx区政府主席',
    '王兆国': '工会主席',
    '李长春': '政治局常委',
    '刘树森': '厅长',
    '刘奇葆': '四川省委书记',
    '莫亦翔': '市委副书记',
    '吴炜率': '常务副市长',
    '曹坤华': '商务厅副厅长',
    '石东龙': '市委副书记',
    '李广存': '副市长',
    '毛艳琼': '政府副市长',
    '李纪恒': '云南省省长',
    '张晓钦': 'xx自治区副主席',
    '刘君': '政协副主席',
    # '肖文荪': 'xx市长',
    '李源潮': '国家副主席',
    '孙大光': '左崇市市长',
    '董君舒': '纪委原书记',
    '陈玉玉': '工会主席',
    '韦朝晖': '商务厅副长',
    '车延风': '政协主席',
    '莫桦': '副市长',
    '金文': '副厅长',
    '车荣福': '书记',
    '贾庆林': '政协主席',
    '连友农': '市长',
    '杨道喜': '政府副主席',
    # '罗保铭': '省长',
    '李志刚': '市长',
    '王乐泉': '法委副书记',
    '李金早': '常务副主席',
    '林念修': '政府副主席',
    '陈际瓦': '党委副书记',
}

def get_png_address(url=None):
    if url:
        resp = requests.get(url)
        if resp.status_code == 200:
            # soup = BeautifulSoup(resp.content, 'html.parser')
            m = re.search(r'.*imageString = \"(.*.jpg\");', resp.text)
            if m:
                print(m.group(1))
                return m.group(1)
            else:
                return ''
        else:
            return ''
    else:
        return ''



leads = list(leader.keys())
c = Counter()
count = 0
lead_count = 0
for item in db.leader_speak.find():
    title = item.get('a_title')
    summary = item.get('summary')
    times = item.get('time')
    url = item.get('a_href')
    content = item.get('content')
    for lead in leads:
        if lead in title:
            lead_count += 1
            print(title)
            people = lead
            position = leader.get(lead)
            png_address = 'http://www.cecbh.com' + get_png_address(url)

            a_dict = {}
            a_dict['people'] = people
            a_dict['position'] = position
            a_dict['theme'] = summary
            a_dict['summary'] = summary
            a_dict['content'] = content
            a_dict['png_address'] = png_address

            db.leader_speak_filter.insert(a_dict)


    # for position in positions:
    #     m = re.search(r'，(.*)(%s)(.*)，' % (position,), content)
    #     if m:
    #         count += 1
    #         # c['%s' % (m.group(2),)] += 1
    #         # c['%s' % (m.group(1)[-6:],)] += 1
    #         # c['%s' % (m.group(3)[:6],)] += 1
    #         print('%s:%s:%s' % (m.group(1)[-6:], m.group(2), m.group(3)[:6]))

# print('total: %s' % (db.leader_speak.find().count(), ))
# print('key_count: %s' % (count,))
# print('lead_count: %s' % (lead_count,))
# for k, v in c.items():
#     print(k, v)



