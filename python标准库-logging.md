# python标准库-logging
- 几个重要的概念
	- Logger 记录器，暴露了应用程序代码能直接使用的接口。
	- Handler 处理器，将（记录器产生的）日志记录发送至合适的目的地。
	- Filter 过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
	- Formatter 格式化器，指明了最终输出中日志记录的布局。

### logging模块使用过程
- 第一次导入logging模块或使用reload函数重新导入logging模块，logging模块中的代码将被执行，这个过程中将产生logging日志系统的默认配置。
- 自定义配置(可选)。logging标准模块支持三种配置方式: dictConfig，fileConfig，listen。其中，dictConfig是通过一个字典进行配置Logger，Handler，Filter，Formatter；fileConfig则是通过一个文件进行配置；而listen则监听一个网络端口，通过接收网络数据来进行配置。当然，除了以上集体化配置外，也可以直接调用Logger，Handler等对象中的方法在代码中来显式配置。
- 使用logging模块的全局作用域中的getLogger函数来得到一个Logger对象实例(其参数即是一个字符串，表示Logger对象实例的名字，即通过该名字来得到相应的Logger对象实例)。
- 使用Logger对象中的debug，info，error，warn，critical等方法记录日志信息。

### 模块处理流程（转载)
- 判断日志的等级是否大于Logger对象的等级，如果大于，则往下执行，否则，流程结束。
- 产生日志。第一步，判断是否有异常，如果有，则添加异常信息。第二步，处理日志记录方法(如debug，info等)中的占位符，即一般的字符串格式化处理。
- 使用注册到Logger对象中的Filters进行过滤。如果有多个过滤器，则依次过滤；只要有一个过滤器返回假，则过滤结束，且该日志信息将丢弃，不再处理，而处理流程也至此结束。否则，处理流程往下执行。
- 在当前Logger对象中查找Handlers，如果找不到任何Handler，则往上到该Logger对象的父Logger中查找；如果找到一个或多个Handler，则依次用Handler来处理日志信息。但在每个Handler处理日志信息过程中，会首先判断日志信息的等级是否大于该Handler的等级，如果大于，则往下执行(由Logger对象进入Handler对象中)，否则，处理流程结束。
- 执行Handler对象中的filter方法，该方法会依次执行注册到该Handler对象中的Filter。如果有一个Filter判断该日志信息为假，则此后的所有Filter都不再执行，而直接将该日志信息丢弃，处理流程结束。
- 使用Formatter类格式化最终的输出结果。 注：Formatter同上述第2步的字符串格式化不同，它会添加额外的信息，比如日志产生的时间，产生日志的源代码所在的源文件的路径等等。
- 真正地输出日志信息(到网络，文件，终端，邮件等)。至于输出到哪个目的地，由Handler的种类来决定。

### 配置方式
- 显式创建记录器Logger、处理器Handler和格式化器Formatter，并进行相关设置；
- 通过简单方式进行配置，使用basicConfig()函数直接进行配置；
- 通过配置文件进行配置，使用fileConfig()函数读取配置文件；
- 通过配置字典进行配置，使用dictConfig()函数读取配置信息；
- 通过网络进行配置，使用listen()函数进行网络配置。


- getLogger Class
	- logger = logging.getLogger()
	- logger = logging.getLogger(\_\_name\_\_)
	- logger = logging.getLogger('str\_you\_like')
- Logger Object
	- Logger.setLevel()
	- Logger.isEnableFor()
	- Logger.getEffectiveLevel()
	- Logger.getChild()
	- Logger.debug()
	- Logger.info()
	- Logger.warning()
	- Logger.error()
	- Logger.critical()
	- Logger.log()
	- Logger.exception()
	- Logger.addFilter()
	- Logger.removeFilter()
	- Logger.filter()
	- Logger.addHandler()
	- Logger.removeHandler()
	- Logger.findCaller()
	- Logger.handle()
	- Logger.makeRecord()
	- Logger.hasHandlers()

- Handler Class
	- `logging.StreamHandler(stream=None)  # 将日志信息打印输出在标准输出上`
	- `logging.FileHandler(filename, mode='a', encoding=None, delay=False) # 重定向到文件的处理器`
	- `logging.NullHandler() # 不做任何的格式化或者输出,由开发库者使用`
	- logging.handlers.WatchedFileHandler(filename, mode='a', encoding=None, delay=False)
	- logging.handlers.BaseRotatingHandler(filename, mode, encoding=None, delay=False)
	- logging.handlers.RotatingFileHandler(filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=False)
	- logging.handlers.TimeRotatingFileHandler(filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None)
	- logging.handlers.SocketHandler(host, port)
	- logging.handlers.DatagramHandler(host, port)
	- logging.handlers.SysLogHandler(address=('localhost', SYSLOG_UDP_PORT), facility=LOG_USER, socktype=socket.SOCK_DGRAM)
	- logging.handlers.NTEventLogHandler(appname, dllname=None, logtype='Application')
	- logging.handlers.SMTPHandler(mailhost, fromaddr, toaddrs, subject, credentials=None, secure=None, timeout=1.0)
	- logging.handlers.BufferingHandler(capacity)
	- logging.handlers.MemoryHandler(capacity, flushLevel=ERROR, target=None, flushOnClose=True)
	- logging.handlers.HTTPHandler(host, url, method='GET', secure=False, credentials=None, context=None)
	- logging.handlers.QueueHandler(queue)
	- logging.handlers.QueueListener(queue, *handlers, respect_handler_level=False)

- Handler Objects
	- Handler.__init__(level=NOTSET)
	- Handler.createLock()
	- Handler.acquire()
	- Handler.release()
	- Handler.setLevel()
	- Handler.setFormatter()
	- Handler.addFilter()
	- Handler.removeFilter()
	- Handler.filter()
	- Handler.flush()
	- Handler.close()
	- Handler.handle()
	- Handler.handleError()
	- Hander.format()
	- Handler.emit()

- Formatter Object
	- logging.Formatter(fmt=None, datefmt=None, style='%')
- fmt	  # 处理器的日志显示形式
	- %(name)s
	- %(levelname)s
	- %(process)d
	- %(message)s
- Filter Object
	- logging.Filter(name='')
- SetLevel()
	- logging.DEBUG
	- logging.INFO
	- logging.WARNING
	- logging.ERROR
	- logging.CRITICAL
	
```
import logging
import logging.handlers

logger = logging.getLogger()

formatter = logging.Formatter('%(asctime)s %(levelname)-%s: %(message)s')
file_handler = logging.FileHandler('test.log')
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.formatter = formatter

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.setLevel(logging.INFO)
logger.removeHandler(console_handler)

try:
	1/0
except:
	logger.exception('this is an exception message')
```

### 总结
- Logger是一个树形层级结构;
- Logger可以包含一个或多个Handler和Filter，即Logger与Handler或Fitler是一对多的关系;
- 一个Logger实例可以新增多个Handler，一个Handler可以新增多个格式化器或多个过滤器，而且日志级别将会继承。