# Python知识点

## python相关

### python书籍推荐
- python参考手册
- 流畅的python

### python装饰器，迭代器，yield?
- 装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
- 迭代器就是实现了工厂模式的对象，他能在你调用next()方法的时候返回容器中的下一个值，任何实现了__iter__和__next__()；比如itertools函数返回的都是迭代器对象。
- 生成器是一种特殊的迭代器，它的返回值不是通过return而是用yield。
- 带有 yield 的函数不再是一个普通函数，而是一个生成器generator，可用于迭代，工作原理同上。yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。

### python队列安全
- 多线程队列安全 Queue.Queue, Queue.LifoQueue, Queue.PriorityQueue
- 多线程队列安全 multiprocessing.Queue

### logging 是线程安全的么？
- 是的，handler 内部使用了 threading.RLock() 来保证同一时间只有一个线程能够输出。
- 但是，在使用 logging.FileHandler 时，多进程同时写一个日志文件是不支持的。

## 操作系统相关

### TCP and UDP
- TCP（Transmission Control Protocol 传输控制协议）是一种面向连接的、可靠的、基于字节流的传输层通信协议。
- UDP(User Datagram Protocol用户数据报协议）一种无连接的传输层协议，提供面向事务的简单不可靠信息传送服务。
- TCP逻辑通信信道是全双工的可靠信道，UDP则是不可靠信道,UDP没有拥塞机制，因此网络出现拥堵不会使源主机的发送效率降低（有利于实时会议视频等）,TCP的连接只能是点到点的,UDP支持一对一，多对一，多对多的交互通信

### TCP粘包，UDP不粘包
- UDP是基于报文发送的，在UDP首部采用了16bit来指示UDP数据报文的长度，不会粘包
- 一个数据包中包含了发送端发送的两个数据包的信息，这种现象即为粘包。
- 处理方法：每个数据包添加包首部,封装为固定长度,如添加特殊符号

### time_wait是什么情况？出现过多的close_wait可能是什么原因？
- 主动关闭的一方 socket将进入TIME_WAIT状态,TIME_WAIT状态将持续2个MSL(Max Segment Lifetime),在Windows下默认为4分钟,即240秒,TIME_WAIT状态下的socket不能被回收使用. 具体现象是对于一个处理大量短连接的服务器,如果是由服务器主动关闭客户端的连接,将导致服务器端存在大量的处于TIME_WAIT状态的socket, 
- 服务器常用的三个状态是：ESTABLISHED 表示正在通信，TIME_WAIT 表示主动关闭，CLOSE_WAIT 表示被动关闭
- 如果一直保持在CLOSE_WAIT状态，那么只有一种情况，就是在对方关闭连接之后服务器程序自己没有进一步发出ack信号。换句话说，就是在对方连接关闭之后，程序里没有检测到，或者程序压根就忘记了这个时候需要关闭连接，于是这个资源就一直被程序占着。个人觉得这种情况，通过服务器内核参数也没办法解决，服务器对于程序抢占的资源没有主动回收的权利，除非终止程序运行。

### epoll,select的区别
- select和epoll这两个机制都是多路I/O机制的解决方案，select为POSIX标准中的，而epoll为Linux所特有的。
- select的句柄数目受限于头文件FD_SETSIZE的声明, 而epoll它的限制是最大的打开文件句柄数目
- epoll的最大好处是不会随着FD的数目增长而降低效率，epoll只处理就绪的fd，它有一个就绪设备的队列，每次只轮询该队列的数据，然后进行处理。
- epoll是通过内核于用户空间mmap同一块内存实现的,避免不必要的内存拷贝

### epoll 水平触发 边沿触发
- LT可以理解为水平触发，只要有数据可以读，不管怎样都会通知。而ET为边缘触发，只有状态发生变化时才会通知，可以理解为电平变化。

## 数据库相关
### mysql字符集与排序规则
- charset utf8 COLLATE utf8_general_ci
- default-character-set=latin1 default-collation=latin1_swedish_ci

### char, varchar
- char类型是使用固定长度空间进行存储(0-255), varchar类型保存可变长度字符串(0-65535)
- 在utf-8状态下的varchar，最大只能到 (65535 - 2) / 3 = 21844 余 1。(MySQL对于变长类型的字段会有1-2个字节来保存字符长度)

### 主键，外键，索引
- 索引是一种单独的、物理的对数据库表中一列或多列的值进行排序的一种存储结构。相当于图书的目录，可以根据目录中的页码快速找到所需的内容
- 为经常用于查询中的谓词和联接条件的所有列创建非聚集索引

### myisam与innodb的区别
- MyISAM是MySQL的默认数据库引擎，性能极佳，但不支持事务处理，不支持外键
- InnoDB：提供事务支持事务，外部键等高级数据库功能。支持外键