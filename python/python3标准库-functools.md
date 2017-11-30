# python3标准库-functools
functools是很简单但也很重要的模块，提供了常用高阶函数("一个可以接受函数作为参数或者以函数作为返回值的函数")并对可调用对象进行处理。有方法也有装饰器(标有@)

- functools.reduce(function, iterable[, initializer])
- functools.cmp_to_key(func)
- @functools.total_ordering
- functools.partial(func, \*args, \**keywords)
- functools.partialmethod(func, \*args, \**keywords)
- functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
- @functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
- @functools.lru_cache(maxsize=128, typed=False)
- @functools.singledispatch
- functools.WRAPPER_ASSIGNMENTS
- functools.WRAPPER_UPDATES

functools.reduce就是Python2内建库中的 reduce，但在python3只将map函数保留在了内建库中，reduce被发配边疆

<code>x = functools.reduce(lambda a,b: a+b, (1, 2, 3))  # =>x=6</code>

cmp_to_key用于将比较函数转换为key函数， sorted 和 list.sort 还提供了 cmp 参数来指定如何比较两个元素，但是在 Python 3 中该参数被去掉了。cmp_to_key 函数就是用来将老式的比较函数转化为 key 函数.这样就可以应用在接受 key 函数为参数的函数中，比如 sorted(), min(), max(), heapq.nlargest(), itertools.groupby()等等

<code>sorted(range(5), key=cmp_to_key(lambda x, y: y-x))      # =>[4, 3, 2, 1, 0]</code>

total_ordering用于简化比较函数的写法。如果你已经定义了 \_\_eq\_\_ 方法，以及 \_\_lt\_\_、\_\_le\_\_、\_\_gt\_\_ 或者 \_\_ge\_\_() 其中之一， 即可自动生成其它比较方法。

<pre>
@total_ordering
class Student:
    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
dir(Student)    # =>['__doc__', '__eq__', '__ge__', '__gt__', '__le__', '__lt__', '__module__']
</pre>

partial 相当于一个高阶函数,相当于给函数传递默认函数并返回函数

<pre>
basetwo = partial(int, base=2)  # 相当于固定或者重新改变int函数里的base参数(默认是base=10)
basetwo.__doc__ = 'Convert base 2 string to an int.'
basetwo('10010')			# =>18
</pre>

partialmethod用函数调用替代装饰器调用。

<pre>
class Cell(object):
	def __init__(self):
		self._alive = False
	@property
	def alive(self):
		return self._alive
	def set_state(self, state):
		self._alive = bool(state)
	set_alive = partialmethod(set_state, True)
	set_dead = partialmethod(set_state, False)
c = Cell()
c.alive		# =>False
c.set_alive()
c.alive		# =>True
</pre>

wraps主要用于装饰器函数的定义中，置于包装函数之前。如果没有对包装函数进行更新，那么被装饰后的函数所具有的元信息就会变为包装函数的元信息，而不是原函数的元信息。

<pre>
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
@decorator
def add(x, y):
    return x + y
add     # =><function __main__.add>
functools.WRAPPER_ASSIGNMENTS		# =>('__module__', '__name__', '__doc__')
functools.WRAPPER_UPDATES			# =>('__dict__',)
</pre>

实际上 wraps(wrapped) 相当于 partial(update_wrapper, wrapped=wrapped, \*\*kwargs)

<pre>
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return update_wrapper(wrapper, func)
</pre>
lru_cache装饰器用于缓存函数的调用结果，对于需要多次调用的函数，而且每次调用参数都相同，则可以用该装饰器缓存调用结果，从而加快程序运行,是python3新功能，python2可安装第三方库 functools32。

<pre>
@lru_cache(None)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y
print(add(1, 2))
print(add(1, 2))  # 直接返回缓存信息
print(add(2, 3))
</pre>

functools.singledispatch是单分派泛函数，和c++中函数的重载类似，即传递不同的类型参数，就表现不同的行为。

<pre>
@singledispatch
def show(obj):
    print (obj, type(obj), "obj")
@show.register(str)
def _(text):
    print (text, type(text), "str")
@show.register(int)
def _(n):
    print (n, type(n), "int")
show(1)			# =>1 <class 'int'> int
show("xx")		# =>xx <class 'str'> str
show([1])			# =>[1] <class 'list'> obj
</pre>