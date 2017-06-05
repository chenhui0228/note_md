# Requests 使用总结
## 安装
- pip install requests

## 帮助手册

```
	$ ipython
	>>> help(requests)
	>>> help(requests.get)
	>>> help(requests.post)
```


## 基本使用
- 发送请求

```
	>>> import requests
	>>> resp = requests.get(url, params=None) or requests.post(url, data=None)
	>>> resp = requests.put() or requests.delete() or requests.head() or requests.options()
```

- 响应内容

```
	>>> resp.status_code 	# 响应码
	>>> resp.history		# 重定向码历史记录 [301]
	>>> resp.url			# 安全编码后的url
	>>> resp.headers		# 响应头字典
	>>> resp.cookies		# 响应cookies
	>>> resp.content		# 响应内容，已经按resp.encoding进行编码
	>>> resp.text			# 响应内容，没有编码的unicode字节串
	>>> resp.json()			# 响应内容，json解码器
	>>> resp.raw			# 响应对象， resp.raw.read(10)
	>>> resp.encoding		# 响应内容的编码格式
	>>> resp.iter_lines()	# 流式API
	>>> resp.request.headers # 请求头
```

- 定制参数

```
	>>> headers = {'user-agent': 'my-app/0.0.1'}	# 请求头
	>>> cookies = {'cookies_are': 'working'}		
	>>> allow_redirects = False						# 是否允许重定向
	>>> proxies = {'http': 'http://127.0.0.1:8888', 'https': 'https://127.0.0.1:8888'}    # 设置IP代理，http网页对应http代理
	>>> proxies = {'http': 'http://user:pass@127.0.0.1:8888'}
	$ pip install requests[socks]
	>>> proxies = {'http': 'socks5://user:pass@host:port', 'https': 'socks5://user:pass@host:port'} # 使用socks5代理，使用之前得安装sockes 依赖
	>>> timeout = (3.05, 23)	# (tcp连接超时，读取超时)
	>>> verify = False		# 针对https,是否验证服务器的SSL证书
	>>> cert = ('/path/server.crt', '/path/key')	# 指定客户端的证书及密钥(解码状态)
	$ pip install certifi # 经常更新证书，默认使用的证书
	>>> resp = requests.get(url, headers=headers, cookies=cookies, allow_redirects=True, timeout=(3.25, 23))
```

## 高级用法及用例
- 如何保持cookies记录？

```
	>>> s = requests.Session()
	>>> s.get(url)
	>>> s.get(url, cookies={'a':'b'}) # 但注意方法级别的cookies参数不会跨请求保持
```

- 配置代理

```
	>>> s = request.Session()
	>>> s.get(url, proxies=proxies)
```

- 如何在发送请求之前，对某些参数做修改，并且一直保持cookies

```
	>>> from request import Request, Session
	>>> s = Session()
	>>> req = Request('GET', url, data=data, headers=headers)
	>>> prepped = s.prepare_request(req)
	>>> resp = s.send(prepped, stream=stream, verify=verify,proxies=proxies, cert=cert, timeout=timeout)
	>>> print(resp.statsu_code)
```

- 下载https文档对SSL证书验证问题

```
	>>> requests.get('https://kennethreitz.com', verify=True) # 验证主机的SSL证书
	>>> requests.get('https://kennethreitz.com', verify=False) # 忽略对SSL证书的验证
	>>> requests.get('https://kennethreitz.com', cert=('/path/server.crt', '/path/key')) # 指定指定客户端的证书及密钥(解码状态)
```

- 如何流式下载

```
	>>> from contextlib import closing
	>>> with closing(requests.get('https://www.baidu.com', stream=True)) as r:
			for line in r:
				print line
```
```
	import requests
	r = requests.get('http://httpbin.org/stream/20', stream=True)
	lines = r.iter_lines()
	first_line = next(lines)
	for line in lines:
	    print(line)
```

- 流式上传（强烈建议使用二进制模式打开文件，"Content-Length"?）

```
	>>> with open('massive-body') as f:
			requests.post('http://some.url/streamed', data=f)
```

- 块编码请求

```
	>>> def gen():
			yield 'hi'
			yield 'there'
	>>> requests.post('https://some.url/chunked', data=gen())
```

- 上传多个图像文件(强烈建议你用二进制模式打开文件)

```
	>>> url = 'http://httpbin.org/post'
	>>> multiple_files = [
	        ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
	        ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
	>>> r = requests.post(url, files=multiple_files)
	>>> r.text
	{
	  ...
	  'files': {'images': 'data:image/png;base64,iVBORw ....'}
	  'Content-Type': 'multipart/form-data; boundary=3131623adb2043caaeb5538cc7aa0b3a',
	  ...
	}
```

- 使用适配器配置指定的SSL版本

```
	import ssl
	from requests.adapters import HTTPAdapter
	from requests.packages.urllib3.poolmanager import PoolManager
	class Ssl3HttpAdapter(HTTPAdapter):
	    """"Transport adapter" that allows us to use SSLv3."""
	    def init_poolmanager(self, connections, maxsize, block=False):
	        self.poolmanager = PoolManager(num_pools=connections,
	                                       maxsize=maxsize,
	                                       block=block,
	                                       ssl_version=ssl.PROTOCOL_SSLv3)
	                                       
```

- 下一步
	- [grequests](https://github.com/kennethreitz/grequests)
	- [requests_futures](https://github.com/ross/requests-futures)

