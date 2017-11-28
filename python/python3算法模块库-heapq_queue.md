# Python3算法模块库
<p>主要介绍了heapq,queue两个模块里的些类与方法。其中heapq模块实现了python中的堆排序，queue 模块实现了多生产者、多消费者队列。它特别适用于信息必须在多个线程间安全地交换的多线程程序中。</p>
- heapq
- queue

---
- sum()
- max()
- min()
- sorted()

### heapq
<p>heapq模块实现了python中的堆排序(这个模块提供heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]。)，并提供了有关方法。heap最小的元素总是heap[0]。</p>
- heapq.heappush(heap, item)
- heapq.heappop(heap)
- heapq.heappushpop(heap, item)
- heapq.heapreplace(heap, item)
- heapq.heapify(x)
- heapq.merge(*iterables, key=None, reverse=False)
- heapq.nlargest(n, iterable, key=None)
- heapq.nsmalllest(n, iterable, key=None)

<pre>
# python堆排序==========================
from heapq import *
def heapsort(iterable):
	h = []
	for value in iterable:
		heappush(h, value)  # 每一次heappush都会维持小顶堆
	return [heappop(h) for i in range(len(h))]  # 每一次heappop都会返回h[0],并重新维持小顶堆
heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])  # =>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ======================================
a = [1, 7, 2, 6, 5, 3]
heapify(a)   # 将a变成小顶堆 =>a=[1, 5, 2, 6, 7, 3]
heappushpop(a, 4)  # heappush,heapop的合体 =>1, a=[2, 5, 3, 6, 7, 4]
heapreplace(a, 1)  # heappop(), heappush(a,1)的合体 =>2, a=[1, 5, 3, 6, 7, 4]
# ====================
a = [2, 4, 6]
b = [1, '3', 5]
c = list(merge(a, b, key=int))   # =>[1, 2, '3', 4, 5, 6],merge方法一般用于归并排序
a = [6, 4, 2]
b = [5, '3', 1]   # =>确保两个列表依据reverse参数的设定都是有序的。
c = list(merge(a, b, key=int, reverse=True))  # =>[6, 5, 4, '3', 2, 1]
# =====================
a = [1, 7, 2, 6, 5, 3]
nlargest(3, a)   # =>获取列表中最大的n个值 [7, 6, 5]
nsmallest(3, a)  # =>获取列表中最小的n个值 [1, 2, 3]
b = ['aa', 'bbb', 'dddd', 'c']
nlargest(2, b, key=len)  # => ['dddd', 'bbb']
</pre>

### queue
<p>queue 模块实现了多生产者、多消费者队列。它特别适用于信息必须在多个线程间安全地交换的多线程程序中。这个模块中的queue 类实现了所有必须的锁语义。它依赖于Python中的线程支持的可用性；实现了三类队列，主要差别在于取得数据的顺序上。在FIFO（First In First Out，先进先出）队列中，最早加入的任务会被最先得到。在LIFO（Last In First Out，后进先出）队列中，最后加入的任务会被最先得到（就像栈一样）。在优先队列中，任务被保持有序（使用heapq模块），拥有最小值的任务（优先级最高）被最先得到。</p>
- queue.Queue(maxsize=0)
- queue.LifoQueue(maxsize=0)
- queue.PriorityQueue(maxsize=0)
- queue.Empty  # exception
- queue.Full   # exception

---
- Queue.qsize()
- Queue.empty()
- Queue.full()
- Queue.put(item, block=True, timeout=None)
- Queue.put_nowait(item)
- Queue.get(block=True, timeout=None)
- Queue.nowait()
- Queue.task_done()
- Queue.join()

<pre>
# =================基本FIFO(First In First Out: 先进先出)队列 queue.Queue
# put()有两个参数，第一个item为必需的，为插入项目的值；第二个block为可选参数，默认为1。如果队列当前为空且block为1，put()方法就使调用线程暂停,直到空出一个数据单元。如果block为0，put方法将引发Full异常。
from queue import Queue
q = Queue()
for i in range(5):
	q.put(i)
while not q.empty():
	print q.get()    # =>0, 1, 2, 3, 4
# ==================LIFO(Last In First Out: 后进先出)队列，与栈类似 queue.LifoQueue
# 可选参数为block，默认为True。如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。如果队列为空且block为False，队列将引发Empty异常。
from queue import LifoQueue
q = Queue.LifoQueue()
for i in range(5):
    q.put(i)
while not q.empty():
    print q.get()    # =>4, 3, 2, 1, 0
# ==================task_done()由队列的消费者线程调用。每一个get()调用得到一个任务，接下来的task_done()调用告诉队列该任务已经处理完毕。如果当前一个join()正在阻塞，它将在队列中的所有任务都处理完时恢复执行
import functools
import queue
import threading

@functools.total_ordering
class Job:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)
    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented
    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented
            
q = queue.PriorityQueue()

q.put(Job(3, 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))

def process_job(q):
    while True:
        next_job = q.get()
        print('Processing job:', next_job.description)
        q.task_done()
        
workers = [
    threading.Thread(target=process_job, args=(q,)),
    threading.Thread(target=process_job, args=(q,)),
]
for w in workers:
    w.setDaemon(True)
    w.start()
    
q.join()
</pre>