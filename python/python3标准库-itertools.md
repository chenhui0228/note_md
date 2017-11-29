# python3标准库-itertools
<p>itertools实现了大量的'迭代器'构建代码块，该模块标准化一套快速且内存高效的核心工具集，独立或组合使用非常有用。使它能够使用纯Python简洁并高效。主要包括‘无限迭代器’，‘有限迭代器’，‘组合生成器’。需要注意的是，迭代器只能使用一次而且不能够回退，需要再次使用时得再生成。</p>
- Infinite Iterators
	- count(start [,step])
	- cycle(p)
	- repeat(elem [,n])
- Finite Iterators
	- accumulate(p [,func])
	- chain(p, q [,...])
	- chain.from_iterable(iterable)
	- compress(data, selectors)
	- dropwhile(pred, seq)
	- filterfalse(pred, seq)
	- groupby(iterable [,key])
	- islice(seq [,start], stop [,step])
	- stramap(func, seq)
	- takewhile(pred, seq)
	- tee(it, n)
	- zip_longest(p, q [,...])
- Combinatoric generators
	- product(p, q [,..., repeat=1])
	- permutations(p [,r])
	- combinations(p, r)
	- combinations_with_replacement(p, r)

<pre>
# 产生的都是无限的,返回的是迭代器，生成后使用一次就无效===========================
itertools.count(10)				# => 10 11 12 13 ...
itertools.cycle('ABCD')			# => A B C D A B C D ...
itertools.repeat(10)			# => 10 10 10 ...
itertools.repeat(10, 3)			# => 10 10 10

# 有限的，返回的也是迭代器，生成后使用一次就无效===============================
itertools.accumulate([1, 2, 3, 4 ,5]) 	# =>1 3 6 10 15
print(list(itertools.accumulate('abcde'))) # =>['a', 'ab', 'abc', 'abcd', 'abcde']
print(list(itertools.accumulate([1, 2, 3], lambda a, b: a+a+b))))  # =>[1, 4, 11]
itertools.chain('ABC', 'DEF')				# =>A B C D E F
itertools.chain.from_iterable(['ABC', 'DEF'])  # =>A B C D E F
itertools.compress('ABCDEF', [1,0,1,0,1,1])    # => A C E F
itertools.dropwhile(lambda x: x<5, [1,4,6,4,1])# => 6 4 1
itertools.filterfalse(lambda x: x%2, range(10)) # => 0 2 4 6 8
itertools.islice('ABCDEFG', 2, None)  # => C D E F G
itertools.starmap(pow, [(2,5), (3,2), (10,3)])  # => 32 9 1000
itertools.takewhile(lambda x: x<5, [1,4,6,4,1]) # => 1 4
itertools.zip_longest('abcd', 'xy', fillvalue='-')# => ('a', 'x'), ('b', 'y'), ('c', '-'), ('d', '-')

# 排序组合相关，返回的也是迭代器，生成后使用一次就无效========================
itertools.product('ABCD', repeat=2)	 	#相当于forloop2次 =>('A', 'A'),('A', 'B'), ('A', 'C'),('A', 'D'),('B', 'A'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'C'), ('C', 'D'), ('D', 'A'),('D', 'B'), ('D', 'C'),('D', 'D')
itertools.permutations('ABCD', 2)	 	#连续长度为2的排列 形式与上=>AB AC AD BA BC BD CA CB CD DA DB DC
itertools.combinations('ABCD', 2)	 	#长度为2的子序列 形式与上=>AB AC AD BC BD CD
itertools.combinations_with_replacement('ABCD', 2)  #允许元素重复 形式与上=>AA AB AC AD BB BC BD CC CD DD

</pre>