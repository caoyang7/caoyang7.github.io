---    
layout: post    
title: "View视图"    
date: 2019-12-13 18:26:40    
category: 'notes'    
tags:    
- Python    
- Django    
---    
* content    
{:toc}    
    
5. View视图










> Django具有“视图”的概念来封装负责处理用户请求和返回响应的逻辑
> 
> 视图函数或视图简而言之就是一个Python函数，它接受一个Web请求并返回一个Web响应
> 
> 此响应可以是网页的HTML内容，重定向或404错误，XML文档或图像。
> 
> 为了将代码放在某处，惯例是将视图放在名为views.py的文件中，放在项目或应用程序目录中

## 一, 一个简单的视图

这是一个返回当前日期和时间的视图，作为HTML文档：

	```
	from django.http import HttpResponse
	import datetime

	def current_datetime(request):
			now = datetime.datetime.now()
			html = "<html><body>It is now %s.</body></html>" % now
			return HttpResponse(html)
	```

## 二,返回错误

	```
	# 直接返回一个404,没有去加载404的模板页面
	# return HttpResponseNotFound('<h1>Page not found</h1>')

	# 可以直接返回一个status状态码
	# return HttpResponse(status=403)

	# 返回一个404的错误页面
	raise Http404("Poll does not exist")
	```

## 三,关于重定向

重定向(Redirect)就是通过各种方法将各种网络请求重新定个方向转到其它位置

	```
	from django.shortcuts import redirect
	from django.core.urlresolvers import reverse

	# redirect重定向  reverse反向解析url地址
	# return redirect(reverse('userindex'))

	# 执行一段js代码，用js进行重定向
	# return HttpResponse('<script>alert("添加成功");location.href = "/userindex"; </script>')

	# 加载一个提醒信息的跳转页面
	context = {'info':'数据添加成功','u':'/userindex'}
	return render(request,'info.html',context)
	```


# 5.1 HttpRequest

- 服务器接收到http协议的请求后，会根据报文创建HttpRequest对象

- 视图函数的第一个参数是HttpRequest对象

- 在django.http模块中定义了HttpRequest对象的API

## 一,属性

下面除非特别说明，属性都是只读的

- path：一个字符串，表示请求的页面的完整路径，不包含域名

- method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'

- encoding：一个字符串，表示提交的数据的编码方式

	- 如果为None则表示使用浏览器的默认设置，一般为utf-8  
	- 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值

- GET：一个类似于字典的对象，包含get请求方式的所有参数

- POST：一个类似于字典的对象，包含post请求方式的所有参数

- FILES：一个类似于字典的对象，包含所有的上传文件

- COOKIES：一个标准的Python字典，包含所有的cookie，键和值都为字符串

- session：一个既可读又可写的类似于字典的对象，表示当前的会话，只有当Django 启用会话的支持时才可用，详细内容见“状态保持”

## 二,方法

- is_ajax()：如果请求是通过XMLHttpRequest发起的，则返回True

## 三,QueryDict对象

- 定义在django.http.QueryDict

- request对象的属性GET、POST都是QueryDict类型的对象

- 与python字典不同，QueryDict类型的对象用来处理同一个键带有多个值的情况

- 方法get()：根据键获取值

	- 只能获取键的一个值  
	- 如果一个键同时拥有多个值，获取最后一个值

	```
	dict.get('键',default)
	或简写为
	dict['键']
	```

- 方法getlist()：根据键获取值

	- 将键的值以列表返回，可以获取一个键的多个值

	```
	dict.getlist('键',default)
	```

## 四,GET && POST

- 一键一值

	```
	http://127.0.0.1/get?a=1&b=2&c=3

	request.GET['name']
	request.GET.get('name',None)
	```

- 一键多值

	```
	http://127.0.0.1/get?a=1&a=2&b=3

	request.GET.getlist('name',None)

	request.POST.getlist('name',None)
	```

# 5.2 HttpResponse

> 在django.http模块中定义了HttpResponse对象的API
> 
> HttpRequest对象由Django自动创建，HttpResponse对象由程序员创建
> 
> 在每一个视图函数中必须返回一个HttpResponse对象,当然也可以是HttpResponse子对象

## 一,不用模板,直接返回数据

```
from django.http import HttpResponse

def index(request):
    return HttpResponse('你好')
```

## 二,调用模板返回数据

```
from django.http import HttpResponse

# 返回模板
return render(request,'user/edit.html',{'info':'你好'})
```

## 三,子类HttpResponseRedirect

> 重定向，服务器端跳转
> 构造函数的第一个参数用来指定重定向的地址
> 可以简写为 redirect

```
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

def index(request):
    return redirect(reverse('myindex')
```

## 四,子类JsonResponse

> 返回json数据，一般用于异步请求
> 帮助用户创建JSON编码的响应
> JsonResponse的默认Content-Type为application/json

```
from django.http import JsonResponse

def index2(requeset):
    return JsonResponse({'list': 'abc'})
```

## 五,set_cookie方法

> Cookie 是由 Web 服务器保存在用户浏览器（客户端）上的小文本文件，它可以包含有关用户的信息。
> 服务器可以利用Cookies包含信息的任意性来筛选并经常性维护这些信息，以判断在HTTP传输中的状态。
> Cookies最典型的应用是判定注册用户是否已经登录网站

#### 设置cookie

```
# 获取当前的 响应对象
response = HttpResponse('cookie的设置')

# 使用响应对象进行cookie的设置
response.set_cookie('a','abc')

# 返回响应对象
return response
```

#### 获取cookie

```
# 读取
a = request.COOKIES.get('a',None)

if a:
    return HttpResponse('cookie的读取：'+a)
else:
    return HttpResponse('cookie不存在')
```
