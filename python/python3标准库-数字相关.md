# python3标准库-数字相关
<p>在python3中，数字类型有整数型(int:无限大小)，浮点型(float:2.55 or 2.5e2)，复数型(complex: a+bj or complex(a,b)),对应的标准库为math,cmath就可以很好处理，还包括对三角函数，角度与弧度，双曲函数及特殊的函数计算都支持，直接调用即可。随机数相关的需要参考random模块，分数或者有理数的计算与表示需要fraction模块的支持。如果有高精度浮点运算的需求，比如金融方面的计算，则需要参考decimal模块。statistics模块提供了多个数值统计函数,如中数，众数，方差，标准差等</p>
- math
- cmath
- random
- fractions
- decimal
- statistics

### math
<p>math模块实现了许多对浮点数的数学运算函数. 这些函数一般是对平台 C 库中同名函数的简单封装, 所以一般情况下, 不同平台下计算的结果可能稍微地有所不同, 有时候甚至有很大出入.</p>
- ceil(x) 取顶
- floor(x) 取底
- fabs(x) 取绝对值
- factorial (x) 阶乘
- hypot(x,y)  sqrt(x*x+y*y)
- pow(x,y) x的y次方
- sqrt(x) 开平方
- log(x)
- log10(x)
- trunc(x)  截断取整数部分
- isnan (x)  判断是否NaN(not a number)
- degree (x) 弧度转角度
- radians(x) 角度转弧度
- complex(real [,imag]) 创建一个复数

---

- math.pi
- math.e
- math.tau
- math.inf
- math.nan

### cmath
<p>cmath模块包含了一些用于复数运算的函数. cmath模块的函数跟math模块函数基本一致，区别是cmath模块运算的是复数，math模块运算的是数学运算.</p>
- cmath.exp(x)
- cmath.log(x[, base])
- cmath.log10(x)
- cmath.sqrt(x)
- cmath.isfinite(x)
- cmath.isinf(x)
- cmath.isnan(x)
- cmath.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0) 比较a,b在指定范围内是否相等

---

- cmath.pi
- cmath.e
- cmath.tau
- cmath.inf
- cmath.infj
- cmath.nan
- cmath.nanj

### random
<p>random模块用于生成随机数。</p>
- random.seed(a=None, version=2)
- random.getstate()
- random.setstate(state)
- random.getrandbits(k)

---
- random.randrange(stop)   # rangrange(10) => 7
- random.randrange(start, stop[, step]) # rangerange(0, 101, 2) => 26
- random.randint(a, b)   # randint(1, 5) =>2   a <= vlaue <= b

---
- random.choice(seq)		# 随机选取一个元素，返回为单个值
- random.choices(population, weights=None, *, cum_weights=None, k=1) 随机选取一个元素，返回值为列表
- random.shuffle(x[, random])		# 洗牌
- random.sample(population, k)  # 随机选取不重复选取k个

---
- random.random()						# =>0.37444887175646646 # Random float:0.0 <= x < 1.0  
- random.uniform(2.5, 10.0)			# =>3.1800146073117523  # Random float:  2.5 <= x < 10.0
- random.triangular(low, high, mode)
- random.betavariate(aplha, beta)
- random.expovariate(lambd)
- random.gammavariate(alpha, beta)
- random.gauss(mu, sigma)
- random.lognormvariate(mu, sigma)
- random.normalvariate(mu, sigma)
- random.vonmisesvariate(mu, kappa)
- random.paretovariate(alpha)
- random.weibullvariate(alpha, beta)

### fractions
<p> fractions模块为有理数运算提供了支持。</p>
- class fractions.Fraction(numberator=0, denominator=1)
- class fractions.Fraction(other_fraction)
- class fractions.Fraction(string)
- func Fraction.from_float(flt)
- func Fraction.from_decimal(dec)
- func Fraction.limit_denominator(max_denominator=1000000)
- fractions.gcd(a, b)

<pre>
>>> from fractions import Fraction
>>> Fraction(16, -10)
Fraction(-8, 5)
>>> Fraction(123)
Fraction(123, 1)
>>> Fraction()
Fraction(0, 1)
>>> Fraction('3/7')
Fraction(3, 7)
[40794 refs]
>>> Fraction(' -3/7 ')
Fraction(-3, 7)
>>> Fraction('1.414213 \t\n')
Fraction(1414213, 1000000)
>>> Fraction('-.125')
Fraction(-1, 8)
>>> Fraction('7e-6')
Fraction(7, 1000000)
# =======================
>>> from fractions import Fraction
>>> Fraction('3.1415926535897932').limit_denominator(1000)
Fraction(355, 113)
>>> from math import pi, cos
>>> Fraction.from_float(cos(pi/3))
Fraction(4503599627370497, 9007199254740992)
>>> Fraction.from_float(cos(pi/3)).limit_denominator()
Fraction(1, 2)
>>> from math import floor
>>> floor(Fraction(355, 113))
3
</pre>

### decimal
<p>decimal模块用于十进制数学浮点运算支持</p>
- 提供十进制数据类型，并且存储为十进制数序列；
- 有界精度：用于存储数字的位数是固定的，可以通过decimal.getcontext（）.prec=x 来设定，不同的数字可以有不同的精度
- 浮点：十进制小数点的位置不固定（但位数是固定的）
- 内容有点多，用到时参考官方文档

<pre>
>>> getcontext().prec = 28
>>> Decimal(10)
Decimal('10')
>>> Decimal('3.14')
Decimal('3.14')
>>> Decimal(3.14)
Decimal('3.140000000000000124344978758017532527446746826171875')
>>> Decimal((0, (3, 1, 4), -2))
Decimal('3.14')
>>> Decimal(str(2.0 ** 0.5))
Decimal('1.4142135623730951')
>>> Decimal(2) ** Decimal('0.5')
Decimal('1.414213562373095048801688724')
>>> Decimal('NaN')
Decimal('NaN')
>>> Decimal('-Infinity')
Decimal('-Infinity')

# 1.可以传递给Decimal整型或者字符串参数，但不能是浮点数据，因为浮点数据本身就不准确。
# 2.要从浮点数据转换为Decimal类型
from decimal import *
Decimal.from_float(12.222)
# 结果为Decimal('12.2219999999999995310417943983338773250579833984375')
# 3.通过设定有效数字，限定结果样式：
from decimal import *
getcontext().prec = 6
Decimal(1)/Decimal(7)
# 结果为Decimal('0.142857')，六个有效数字
# 4.四舍五入，保留几位小数
from decimal import *
Decimal('50.5679').quantize(Decimal('0.00'))
# 结果为Decimal('50.57')，结果四舍五入保留了两位小数
# 5.Decimal 结果转化为string
from decimal import *
str(Decimal('3.40').quantize(Decimal('0.0')))
# 结果为'3.40'，字符串类型

</pre>

### statistics
<p>总体方差是我们学习时的标准方差，值是唯一的。而样本方差是从n个里最多选取n-1个进行计算，值有点随机性。只做为评估</p>
- staticstics.mean(data)  # 平均数 (a+b+...+n)/n
- staticstics.harmonic_mean(data)  # 调和平均数 n/(1/a + 1/b + ... + 1/n)
- staticstics.median(data)	# 中位数 (偶数，中位数为中间两位的平均数)
- staticstics.median_low(data)  # 中位数 (偶数，则较小的)。
- staticstics.median_high(data)	# 中位数 (偶数，则较大的)。
- staticstics.median_grouped(data, interval=1) # 使用内插法返回分组连续数据的中值，计算为第50%个数？
- staticstics.mode(data)	# 众数
- staticstics.variance(data) # 样本方差 衡量随机变量或一组数据时离散程度的度量。
- staticstics.pvariance(data, mu=None)  # 总体方差
- staticstics.stdev(data)	# 样本标准差，sqrt(样本方差）
- staticstics.pstdev(data, mu=None) # 总体标准差，sqrt(总体方差)


<pre>
>>> mean([1, 2, 3, 4, 4])	# =>2.8
>>> mean([-1.0, 2.5, 3.25, 5.75])		# =>2.625

>>> from fractions import Fraction as F
>>> mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])  # =>Fraction(13, 21)
>>> from decimal import Decimal as D
>>> mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])  # =>Decimal('0.5625')
>>> harmonic_mean([2.5, 3, 10])  # 3/(1/2.5 + 1/3 + 1/10)   # =>3.6

>>> median([1, 3, 5])	# =>3
>>> median([1, 3, 5, 7])	# =>4.0
>>> median_grouped([52, 52, 53, 54])  # =>52.5 ?
>>> median_grouped([1, 3, 3, 5, 7], interval=1)  # =>3.25 ?
>>> median_grouped([1, 3, 3, 5, 7], interval=2)  # =>3.5 ?

>>> mode([1, 1, 2, 3, 3, 3, 3, 4])  # =>3
>>> mode(["red", "blue", "blue", "red", "green", "red", "red"])  # =>'red'


>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> variance(data)  # =>1.3720238095238095
>>> m = mean(data)
>>> variance(data, m)  # =>1.3720238095238095
>>> from decimal import Decimal as D
>>> variance([D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")])  # =>Decimal('31.01875')
>>> from fractions import Fraction as F
>>> variance([F(1, 6), F(1, 2), F(5, 3)])  # =>Fraction(67, 108)
>>> pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])  # =>0.986893273527251
</pre>