```
# 设置断点，并打印出调用栈
>>> import pdb
>>> print pdb.set_trace(); 
```
```
# 使用dis反汇编函数看两个方法的字节码
>>> from dis import dis
>>> dis('{1}')
>>> dis('set([1])')
```
```
# 使用timeit模块做速度测试
>>> import timeit
>>> ？
```

# 共享文件
python -m SimpleHTTPServer
python -m http.server

# 漂亮打印到终端与json
from pprint import pprint
cat file.json | python -m json.tools

# 定位性能分析
python -m cProfile my_script.py

# csv => json
python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file'))))"

# 列表辗平
itertools.chain.from_iterable

# 一行赋值
self.__dict__.update({k: v for k, v in locals().items()})
