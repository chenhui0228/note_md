# python3进阶知识点

### python3数据类型
### 理解python *器
- 可迭代对象: 可直接作用于for循环的对象
	- list,tuple,dict,set,str
	- 生成器
- 迭代器： 可以被`next()`函数调用并不断返回下一个值的对象
	- 生成器
- 生成器： 使用`列表生成式`或者带`yield的function`
	- g = (x * x for x in range(10))
	
	```
	def fib(max):
		n, a, b = 0, 0, 1
		while n < max:
			yield b
			a, b = b, a+b
			n = n + 1
		return 'done'
	g = fib(6)
	```
		

###函数式编程 
- 高阶函数
	- 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数(还可以返回值为函数)

	```
	def add(x, y, f):
	    return f(x) + f(y)
	```
	- r = map(lambda x: x*x, [1, 2, 3])   	  # =>[1, 4, 9]
	- r = reduce(lambda x,y: x+y, [1, 2, 3])  # =>6
	- r = filter(lambda x: x and x.strip(), ['A', '', 'B', 'None'])   # =>['A', 'B']
	- sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)  # => ['about', 'bob', 'Credit', 'Zoo']
	- 闭包
		- 函数一里定义函数二，并且函数二里引用函数一的值并且做为函数一的返回值
- 匿名函数
	- lambda x: x*x
- 装饰器
	
	```
	def log(func):
	   def wrapper(*args, **kw):
	       print('call %s():' % func.__name__)
	       return func(*args, **kw)
    return wrapper
    @log   # => now = log(now)
    def now():
    	print('2017-11-17')
	```
- 偏函数
	- int2 = functools.partial(int, base=2)
	- int2('1000000') # => 64
### 弱引用
### 双下划线方法
- `__name`是`私有变量`(前两下划线)，只有内部可以访问，外部不可以访问。
- `__name__`是`特殊变量`,可以直接访问，但自己尽量别用这样的变量名。
- `_name`是`受保护变量`,可以访问，但import不进来。