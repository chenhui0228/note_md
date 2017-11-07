# Python面试题整理与分享
### Class里的共享变量，可变与不可变对象
1. 没有self关键字的，类的实例化对象都共享一片内存空间。
2. 对实例化对象进行赋值，实例化对象会生成一片新的内存空间,但在类空间也有一片内存。如p2.weight=99。
3. 但是p1.a_list.append(1)里a_list是可变对象，没有使用赋值，而是使用append方法，所以改变的还是共享空间。


```
class Person(object):
	name = ""
	weight = 50
	a_list = [4, 5, 6]
	
p1 = Person()
p2 = Person()
Person.name = "Robot"
p1.a_list.append(1)
p2.weight = 99

print(p1.name, p1.weight, p1.a_list) # ('Robot', 50, [4, 5, 6, 1])
print(p2.name, p2.weight, p2.a_list) # ('Robot', 99, [4, 5, 6, 1])
print(Person.name, Person.weight, Person.a_list) # ('Robot', 50, [4, 5, 6, 1])
```

### Python函数传递可变对象
1. 函数只在初始化时对参数进行空间申请与运算，调用时不会在进行运算，只会去找变量对应的内存空间。
2. 调用f(2)时b指向[]的内存空间，f(3, [1, 2]) 会让b临时指向[1, 2]的内存空间。重新调用f(3)时，b还是原先[]的内存空间，只不过该空间里在f(2)的调用下已经有值为[0, 1]。可以调试输出id(b)查看内存地址值进行对比。
3. 所以，函数默认传参尽可能不传递可变变量,除非你真的需要这样做。它既是特性，也有魔性。

```
def f(a, b=[]):
	for i in range(a):
		b.append(i * i)
	# print(id(b))
	print(b)

f(2)  # [0, 1]
f(3, [1, 2])  # [1, 2, 0, 1 ,4]
f(3)  # [0, 1, 0, 1, 4]
```

### 长度为N的整型数组，找出乘积最大的两个数，时间复杂度？
1. 整型数组，得考虑负数。
2. 乘积最大为 max(最大值\*次大值，最小值\*次小值)
3. python不需要担心整数乘法溢出。
4. 时间复杂度`O(n)`

```
import sys
import unittest

def find_mulmaxs_two_value(arr=None):
	if arr is None:
		arr = []
	MAX_INT = sys.maxint
	print(MAX_INT)
	maxs = se_maxs = -MAX_INT
	mins = se_mins = MAX_INT
	for x in arr:
		if x >= maxs:
			se_maxs = maxs
			maxs = x
		if se_maxs < x < maxs:
			se_maxs = x
		if x <= mins:
			se_mins = mins
			mins = x
		if mins < x < se_mins:
			se_mins = x
	# 如果两个最大的数相乘结果如何,不用担心，Python支持“无限精度”的整数，会使用自符串处理的。
	if maxs*se_maxs >= mins*se_mins:
		return maxs, se_maxs
	# 相等的情况也放在上面了
	else:
		return mins, se_mins

class FuncTest(unittest.TestCase):
	def test_func(self):
		self.assertEquals(find_mulmaxs_two_value([4, -3, 4, -5, 2, -6]), (-6, -5))
		self.assertEquals(find_mulmaxs_two_value([4, -3, 4, -5, 2, -3]), (4, 4))
		self.assertEquals(find_mulmaxs_two_value([0, -3, 4, 0, 2, -3]), (-3, -3))
		self.assertEquals(find_mulmaxs_two_value([0, -5]), (0, -5))
		self.assertEquals(find_mulmaxs_two_value([9223372036854775807, 9223372036854775807]), (9223372036854775807, 9223372036854775807))



if __name__ == '__main__':
	unittest.main()
```