# python3标准库-collections
<p>collections是Python内建的一个集合模块，提供了许多有用的集合类。相对于python本身的tuple,list,dict提供了namedtuple, deque, defaultdict,counter,OrderedDict,ChainMap等轻量及并且好用的数据结构。参考官方文档及搜索好的资料整理而得，以便知道有这个好用的库，并且能够拿来就用。</p>
## collections
- collections.Counter
- collections.defaultdict
- collections.OrderedDict
- collections.namedtuple
- collections.ChainMap
- collections.deque
- collections.UserDict
- collections.UserList
- collections.UserString

### Counter
<p>对象实例化接受‘可迭代对象’或者‘字典’或者‘字典形式传参’；方法包括’取前几数量的字典（most_common([n])）‘，’所有的键值(keys()，values()，items()）‘，’所有value为正数的键（elements()）‘，’以相加的方式相加或者更新（d.update(e),d.substract(e)）‘，；并可以强制转化为’列表‘，’集合‘，’字典‘；进行+=运算时与update,substract一致，但只保持为正值的，进行&|运算时与集合的交集合集一致，但也只保持为正值的；+-操作对每个值做正负操作后，只保留为正值的</p>
- elements()
- most_common([n])
- subtract([iterable-or-mapping])
- fromkeys(iterable)  # This class method is not implemented for Counter objects.
- update([iterable-or-mapping])

<pre>
cnt = Counter()
for word in ['red', 'blue']:
	cnt[word] += 1
print(cnt)
cnt.keys()
cnt.most_common(1)  # 第一数量的字典 =======================================
c = Counter('gallahad')  # 实例化方法
c = Counter({'red': 4, 'blue': 2})  # 实例化方法
c = Counter(cats=4, dogs=8)   # 实例化方法
c = Counter(['eggs', 'ham'])  # 实例化方法==================================
c = Counter(a=4, b=2, c=0, d=-2)
sorted(c.elements()) # =>['a', 'a', 'a', 'a', 'b', 'b']
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)  # =>Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
c = Counter({'a': 2, 'b': -4})
c.update({'c': 3})  # =>Counter({'a': 2, 'b': -4, 'c': 3})
c.update({'b': 3})  # =>Counter({'a': 2, 'b': -1, 'c': 3}) 以相加的方式更新
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs====================
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c + d                       # 创建新的Counter,相同键值的相加，不同的都赋值到新的Counter对象,并只保持着value为正值的
c - d                       # 相减，并只保持着value为正值的
c & d                       # 先交集，并所有value只为交集里最小的。并只保持着value为正值的
c | d                       # 先合集，并所有value只为合集里最大的。并只保持着value为正值的======================
c = Counter(a=2, b=-4)
+c  # =>Counter({'a': 2})
-c  # =>Counter({'b': 4})
</pre>

### defaultdict
<p>对字典设置默认值，默认值以函数的形式传入</p>
<pre>
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)  # or d = defaultdict([]) or set, int
for k, v in s:
	d[k].append(v)
# ==================================================================
def constant_factory(value):
	return lambda: value
d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
print('%(name)s %(action)s to %(object)s' % d)  # =>'John ran to <missing>'
</pre>

### OrderedDict
- move_to_end(last=True)
- popitem(last=True)

<p>dict是Python利用Hash实现的，并且会自动扩容，所以无序。但是使用OrderedDict会根据放入元素的先后顺序进行排序。并且可以利用sorted及key传函数名参数创建一个排序字典。</p>
<pre>
d = OrderedDict.fromkeys('abcde') # =>OrderedDict([('a', None), ('b', None), ('c', None), ('d', None), ('e', None)])
d.move_to_end('b')  # =>
print(''.join(d.keys()))  # =>'acdeb'  # last=True,则将最后一个移到最右边
d.move_to_end('b', last=False)
print(''.join(d.keys()))  # => 'bacde'  # last=False,则将最后一个移到最左边
d.popitem()  # =>('d', None), last=True,弹出最右边一个
d.popitem(last=False)  # =》('e', None), last=False,弹出最左边一个
# ==================================================================
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
OrderedDict(sorted(d.items(), key=lambda t: t[0]))  # =>OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
OrderedDict(sorted(d.items(), key=lambda t: t[1]))  # =>OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))  # =>OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])
</pre>

### namedtuple
<p>命名元组，非常轻量及的元组,可结合csv，sqlite3使用</p>
- \_make(iterable)
- \_asdict()
- \_replace(**kwargs)
- \_source
- \_fields

<pre>
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)     # =>Point(x=11, y=22)
p[0] + p[1]             # =>33  or p.x + p.y
x, y = p                # 解包
print(x, y)				 # =>(11, 22)
# 直接对csv,sqlite3返回结果进行命名元组创建=======================================
EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    print(emp.name, emp.title)
import sqlite3
conn = sqlite3.connect('/companydata')
cursor = conn.cursor()
cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.name, emp.title)
# =================================================
t = [11, 22]
p = Point._make(t)  	# => Point(x=11, y=22)
d = {'x': 11, 'y': 22}
p = Point(**d)			# => Point(x=11, y=22)
p_x = getattr(p, 'x')	# => 11
p1 = p._asdict()			# => OrderedDict([('x', 11), ('y', 22)])
p2 = p._replace(x=33)	# => Point(x=33, y=22), p不变
p3 = p._fields			# => ('x', 'y') p3为元组
Color = namedtuple('Color', 'red green blue')
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
p4 = Pixel(11, 22, 128, 255, 0)  # =>Pixel(x=11, y=22, red=128, green=255, blue=0)            
</pre>

### ChainMap
<p>它用来将多个map串联到一起。这比新建一个map再将其他map用update加进来快得多。通过ChainMap可以来模拟嵌套的情景，而且多用于模板之中。</p>
- maps
- new_child(m=None)
- parents

<pre>
from collections import ChainMap
m1 = {'color': 'red', 'user': 'guest', 'age': 11}
m2 = {'name': 'drfish', 'age': '18'}
chainMap = ChainMap(m1, m2)
print(chainMap.items()) # =>ItemsView(ChainMap({'color': 'red', 'user': 'guest', 'age': 11}, {'name': 'drfish', 'age': '18'}))
# 获取ChainMap中的元素 ======================================
print(chainMap.get('name'))  # =>drfish
print(chainMap.get('age'))   # => 11, 从第一个开始查询，找到就结束，没有找到就None
print(chainMap.get('not'))   # =>None
# 新增map==================================================
m3 = {'data': '1-6'}
chainMap = chainMap.new_child(m3)
print(chainMap.items())  # =>ItemsView(ChainMap({'data': '1-6'}, {'user': 'guest', 'color': 'red'}, {'age': '18', 'name': 'drfish'})) 出现在前头
# 属性=====parents属性返回除去第一个map后的ChainMap实例========
print(chainMap.parents) # =>ChainMap({'user': 'guest', 'color': 'red'}, {'age': '18', 'name': 'drfish'})
print(chainMap.parents.parents)  # =>ChainMap({'age': '18', 'name': 'drfish'})
print(chainMap.parents.parents.parents)  # =>ChainMap({})
chainMap.maps   # =>[{'data': '1-6'},{'color': 'red', 'user': 'guest'},{'age': '18', 'name': 'drfish'}]
</pre>

### deque
<p>Deque是双向列表数据结构，适合快速在容器两端插入和删除数据。它在容器两端操作的时间复杂度为 O(1),相比list（O(n)）要快很多。但与list又有差不多的api。Deque的缺点就是remove还有判断获取索引的时候，速度有些慢，因为他需要执行多遍deque相关联的数据块。不像list那样，一遍就行。 </p>
- append(x)
- appendleft(x)
- clear()
- copy()
- count(x)
- extend(iterable)
- extendleft(iterable)
- index(x[,start[, stop]])
- insert(i, x)
- pop()
- popleft()
- remove(value)
- reverse()
- rotate(n)
- maxlen
	
<pre>
from collections import deque
d = deque('ghi')
for elem in d:                  
	print(elem.upper())  # =>'G H I'
d.append('j')
d.appendleft('f')   # =>deque(['f', 'g', 'h', 'i', 'j'])
d.pop()				# =>'j'
d.popleft()         # =>'f'
list(d)                          # =>['g', 'h', 'i']
d[0]                             # =>'g'
list(reversed(d))                # =>['i', 'h', 'g']
'h' in d                         # =>True
d.extend('jkl')                  # =>deque(['g', 'h', 'i', 'j', 'k', 'l'])
d.rotate(1)                      # 右移一位，=>deque(['l', 'g', 'h', 'i', 'j', 'k'])
d.rotate(-1)                     # 左移一位, =>deque(['g', 'h', 'i', 'j', 'k', 'l'])
d.clear()                        # empty the deque
>>> d.extendleft('abc')          # 一个一个元素添加的，所以 =>deque(['c', 'b', 'a'])
</pre>

### UserDict
### UserList
### UserString


- operator
	- attrgetter
	- itemgetter
- heapq
- sorted
- min
- max
- itertools
	- groupdy
- compress