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