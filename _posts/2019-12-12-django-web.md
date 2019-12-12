---    
layout: post    
title: "Web开发介绍和Django简介"    
date: 2019-12-12 18:26:40    
category: 'notes'    
tags:    
- Python    
- 框架    
---    
* content    
{:toc}    
    
Web开发介绍,Django简介,URLconf路由













# 1. Web开发介绍

## 一,认识一个网站

### B/S和C/S结构

![csbs.png](/assets/blog/csbs.png)

1. web1.0

开始于1994年,静态网站,只能看不能写,没有交互

![web1.0.png](/assets/blog/web1.0.png)

2. web2.0

始于2004年3月,动态网站,最直接的体现就是我们现在使用的商场,论坛,微博等

![web2.0.png](/assets/blog/web2.0.png)

### Web应用结构 及 工作原理

![webjg.png](/assets/blog/webjg.png)


## 二,Web框架

#### 什么是框架

> 软件框架就是为实现或完成某种软件开发时,提供了一些基础的软件产品  
> 框架的功能类似于**基础设施**,提供并实现**最为基础的软件架构和体系**  
> 通常情况下我们依据框架来实现更为复杂的业务程序开发,框架就是程序的**骨架**

#### 框架的优缺点

> 可重用  
> 成熟,稳健
> 可扩展性良好  
> 选对框架很重要

#### Python中常用框架

> 大包大揽Django被官方称之为完美主义者的web框架  
> 力求精简web.py和Tornodo  
> 新生代微框架Flask和Bottle

#### web框架中的一些概念

1. MVC

	- 大部分开发语言中都有MVC框架  
	- MVC框架的核心思想是:解耦  
	- 降低各功能模块之间的耦合性,方便变更,更容易重构代码,最大程度上实现代码的重用  
	- m表示model,主要用于对数据库层的封装  
	- v表示view,用于向用户展示结果  
	- c表示controller,是核心,用于处理请求,获取数据,返回结果

2. MVT

	- Django是一块python的web开发框架,属于MVT框架  
	- m表示model,负责与数据库交互  
	- v表示view,是核心,负责接收请求,获取数据,返回结果  
	- t表示template,负责呈现内容到浏览器



# 2. Django简介
## 一,认识Django

- Django是一个高级的Python Web框架，它鼓励快速开发和清洁，务实的设计。  
- 由经验丰富的开发人员构建，它负责Web开发的许多麻烦，因此您可以专注于编写应用程序，而无需重新创建轮子。  
- 它是免费的和开源的。  
- 被官方称之为完美主义者的Web框架。  
- Django可以更快地构建更好的Web应用程序并减少代码。  

	[官方文档](https://www.djangoproject.com/)

	[中文文档](http://python.usyiyi.cn/)

## 二,Django框架的特点:

- 快速开发：Django的宗旨在于帮助开发人员快速从概念到完成应用程序。  
- 安全可靠：Django认真对待安全性，帮助开发人员避免许多常见的安全错误。  
- 超可伸缩性: Web上的一些最繁忙的网站利用了Django快速灵活扩展的能力。  

## 三,Django可以使用什么Python版本?

|Django版本	|Python版本															|
|1.8				|2.7，3.2（直到2016年底），3.3, 3.4, 3.5 |
|1.9, 1.10	|2.7, 3.4, 3.5													|
|1.11				|2.7 , 3.4 , 3.5 , 3.6									|
|2.0				|3.5+																		|


## 四,Django的开发版本

![release-roadmap.png](/assets/blog/release-roadmap.png)

## 五,Django安装

作为Python Web框架，Django需要Python，在安装Python同时需要安装pip。

```
在线安装Django
pip3 install Django

检测当前是否安装Django及版本
python3 -m django --version

1.11.7
```



# 2.1 Django入门

## 一,Django框架的搭建

```
django安装后 进行django框架的搭建

django-admin startproject mysite

mysite是项目目录名,可以自定义
```

我们来看看startproject创建的内容:

```
tree是Linux命令负责将当前文件夹以树状结构显示
如若提示未找到命令进行 sudo apt-get install tree 即可

yc@yc-virtual-machine:~/test$ tree
.
└── mysite
    ├── manage.py
    └── mysite
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

2 directories, 5 files
```

关于上面自动生成的目录与文件解释如下:

> - 外部test/根目录只是一个项目的容器。它的名字与Django无关; 您可以将其重命名为您喜欢的任何内容。  
> - manage.py：一个命令行实用程序，可以让您以各种方式与此Django项目进行交互。你可以阅读所有的细节 manage.py在Django的管理和manage.py。  
> - 内部mysite/目录是您的项目的实际Python包。它的名字是您需要用来导入其中的任何内容的Python包名称（例如mysite.urls）。  
> - mysite/init.py：一个空的文件，告诉Python这个目录应该被认为是一个Python包。  
> - mysite/settings.py：此Django项目的设置/配置。 Django设置会告诉你所有关于设置的工作原理。  
> - mysite/urls.py：该Django项目的URL声明; 您的Django动力网站的“目录”。
> - mysite/wsgi.py：WSGI兼容的Web服务器为您的项目提供服务的入口点。  


## 二,启动项目

在当前 manage.py 的文件目录下 执行以下命令:

```
sudo python3 manage.py runserver
```

您将在命令行中看到以下输出:

```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.（注意：现在忽略关于未执行应用数据库迁移的警告）

August 07, 2017 - 15:50:53
Django version 1.11, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

注意:通过ip访问后报如下错误:

```
DisallowedHost at /polls
Invalid HTTP_HOST header: '192.168.*.*:8000'. You may need to add '192.168.*.*' to ALLOWED_HOSTS.

HTTP_HOST标头无效：'192.168.*.*:8000'。您可能需要将“192.168.*.*”添加到ALLOWED_HOSTS
解决：
进入 mysite/settings.py文件
ALLOWED_HOSTS = ['192.168.194.132']
```

## 三,浏览器访问

![llqfw.png](/assets/blog/llqfw.png)



# 2.2 创建应用

## 一,创建应用

Django自带一个实用程序，可以自动生成应用程序的基本目录结构，因此您可以专注于编写代码而不是创建目录。

要创建您的应用程序，请确保您与目录位于同一目录，manage.py 并键入以下命令：

```
python3 manage.py startapp myweb

这将创建一个目录myweb，其目录如下：此目录结构将容纳轮询应用程序。

[root@localhost demo]# tree mysite/
mysite/
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── myweb
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
```

## 二,创建视图

Django具有"视图"的概念来封锁负责处理用户请求和返回响应的逻辑

在myweb/views.py:

```
from django.shortcuts import render
from django.http import HttpResponse

# 定义视图函数,业务逻辑
def index(request):

	# 返回一句话
	return HttpResponse('Hello World!!!')
```

## 三,修改root路由 mysite/urls.py

当用户使用django提供的站点进行访问时,首页由路由进行匹配访问地址,然后指定函数或子路由进行处理

```
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
	# url(r'^admin/',admin.site.urls),
	url(r'^',include('myweb.urls')),
]
```

## 四,在应用下创建子路由

```
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^hello/',views.index),
]
```

## 五,通过浏览器访问服务
注意:url路由,**由上而下**进行匹配,如果在上面就匹配成功,则不会向下匹配

```
通过浏览器访问服务
127.0.0.1:8000/abc => root url(根路由) => 加载子路由(myweb/urls.py)

=> 正则匹配访问的路径(path) => 视图函数(views.index)

=> views.py index() 响应内容
```

## 六,使用模板

作为Web 框架，Django 需要一种很便利的方法以动态地生成HTML。

最常见的做法是使用模板。

模板包含所需HTML 输出的静态部分，以及一些特殊的语法，描述如何将动态内容插入。

```
在当前manage.py的同级目录中创建一个文件夹 templates/index.html

在settings.py文件中 TEMPLATES模块设置选项

'DIRS':[os.path.join(BASE_DIR,"templates")],

在子路由中添加一个路由
url(r'^tmp$',views.tmp,name='myweb_tmp'),

在views.py 创建一个tmp的视图函数
def tmp(request):
	# 加载一个模块
	return render(request,'index.html')
```

如果在视图函数加载模板时,分配了数据,就可以在模板中使用数据

```
def tmp(request):
	# 实例化 模型对象,获取数据
	
	# 分配数据
	context = {'info':'aabbccddee'}
	# 加载一个模块
	return render(request,'index.html',context)
```

在HTML模板中输出变量

```
<h3>加载数据</h3>
<p></p>
```



# 3. URLconf路由

> 一个干净优雅的URL方案是高质量Web应用程序中的一个重要细节。
> 
> Django可以让你设计URL，无论你想要什么，没有框架限制。
> 
> 要为应用程序设计URL，您可以非正式地创建一个名为URLconf（URL配置）的Python模块。
> 
> 这个模块是纯Python代码，是一个简单的Python模式（简单的正则表达式）到Python函数（您的视图）之间的映射。

## 一,Django是如何处理一个请求:

当用户从Django提供的站点请求页面时，系统遵循以下算法来确定要执行的Python代码：

> 首先Django确定要使用的根URLconf模块，通过ROOT_URLCONF来设置，具体在settings.py配置文件中。但是如果传入 HttpRequest对象具有urlconf 属性（由中间件设置），则其值将用于替换ROOT_URLCONF设置。
> 
> Django加载该Python模块并查找该变量 urlpatterns。这应该是一个Python的django.conf.urls.url()实例列表。
> 
> Django按顺序运行每个URL模式，并在匹配所请求的URL的第一个URL中停止。
> 
> 一旦正则表达式匹配，Django将导入并调用给定的视图，这是一个简单的Python函数（或基于类的视图）。
> 
> 如果没有正则表达式匹配，或者在此过程中的任何一点出现异常，Django将调用适当的错误处理视图。

以下是一个URLconf示例：

```
from django.conf.urls import url
from . import views

urlpatterns = [
	  url(r'^articles/2003/$', views.special_case_2003),
    url(r'^articles/([0-9]{4})/$', views.year_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
]
```

说明:

> - 要从URL捕获一个值,只需将其括起来
> - 没有必要添加一个主要的斜杠,因为每个URL都有。例如:^articles,不是^/articles
> - 正则中的'r'证明每个正则表达式中的字符串是可选的,但推荐使用。它告诉python一个字符串是"row",字符串中没有任何内容应该被转义

示例请求

> - /articles/2005/03/将匹配列表中的第三个条目。Django会调用该函数 。views.month_archive(request, '2005', '03')  
> - /articles/2005/3/ 不符合任何网址格式，因为列表中的第三个条目需要两个数字的月份。  
> - /articles/2003/将匹配列表中的第一个模式，而不是第二个模式，因为模式是按顺序测试的，第一个模式是第一个测试通过。随意利用这些命令插入特殊情况。在这里，Django会调用该函数 views.special_case_2003(request)  
> - /articles/2003 将不匹配任何这些模式，因为每个模式要求URL以斜杠结尾。  
> - /articles/2003/03/03/将匹配最终模式。Django会调用该函数。views.article_detail(request, '2003', '03', '03')

**注意:每个捕获的参数都作为纯Python字符串发送到视图,无论正则表达式匹配的是什么,即使[0-9]{4}也只会匹配整数字符串**

## 二,命名组

上述使用为简单实例，属于`正则表达式非命名组`（通过括号）捕获URL定位，并将它们作为`位置参数`传递给视图。

在更高级的使用中，我们可以使用`正则表达式命名组`来捕获URL定位，并将它们作为`关键字参数`传递给视图。

在Python正则表达式中，正则表达式命名组的语法是`(?P<name>pattern)`，其中命名组中的命名就是name，并且 pattern是某些匹配的模式。

#### 实例:

```
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^articles/2003/$',views.special_case_2003),
	url(r'^articles/(?P<year>[0-9]{4})/$',views.year_archive),
	url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',views.month_archieve),
	url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
]
```

这完成了与上一个例子完全相同的事情，有一个微妙的区别：**捕获的值被传递到视图函数作为关键字参数,而不是位置参数**

例如:

- 请求/articles/2005/03/调用函数 ，。views.month_archive(request, year='2005', month='03') 而不是 views.month_archive(request, '2005', '03')

- 请求/articles/2003/03/03/调用函数 。views.article_detail(request, year='2003', month='03', day='03')

- 在实践中，这意味着您的URLconfs稍微更明确，更不容易出现参数命令错误

- 您可以重新排序视图的函数定义中的参数。当然，这些好处是以简洁为代价的; 一些开发人员发现命名组语法丑陋而且太冗长。

#### URLconf搜索

URLconf将根据所请求的URL进行搜索，作为普通的Python字符串。这不包括GET或POST参数或域名。

例如:

- 在请求中<https://www.example.com/myapp/>，URLconf将寻找myapp/。

- 在请求中<https://www.example.com/myapp/?page=3>，URLconf将会查找myapp/。

URLconf不查看请求方法。换句话说，所有的请求方法(GET,POST,HEAD等)都将被路由到相同的URL功能。

#### 指定用于视图函数的默认值

一个方便的技巧是为您的视图参数指定默认参数。下面是一个URLconf和view的例子：

在下面的示例中，`两个URL模式指向相同的视图views.page`，但是第一个模式不会从URL捕获任何内容。

如果第一个模式匹配，该page()函数将使用它的默认参数num，"1"。

如果第二个模式匹配， page()将使用num正则表达式捕获的任何值。

```
# URLconf
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^blog/$', views.page),
    url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
]

# View (in blog/views.py)
def page(request, num="1"):
    # Output the appropriate page of blog entries, according to num.
    ...
```

## 三,错误处理

> 当Django找不到与请求的URL匹配的正则表达式时，或者异常引发时，Django将调用错误处理视图。
> 
> 用于这些情况的视图由四个变量指定。它们的默认值对于大多数项目都是足够的，但通过覆盖其默认值可以进一步定制。
> 
> 有关详细信息，请参阅自定义错误视图的文档。
> 
> 这样的值可以在你的根URLconf中设置。在任何其他URLconf中设置这些变量将不起作用。
> 
> 值必须是可调用的，或者代表视图的完整的Python导入路径的字符串，应该被调用来处理手头的错误条件。

#### 变量:

见django.conf.urls.handler

[菜鸟教程-HTTP状态码](https://www.runoob.com/http/http-status-codes.html)

1. handler400

	- 两种形式：

		1、bad request 意思是 "错误的请求"；  
		2、invalid hostname 意思是 "不存在的域名"。
		
	- 错误原因:
		
		1、前端提交数据的字段名称或者是字段类型和后台的实体类不一致，导致无法封装；  
		2、前端提交的到后台的数据应该是 json 字符串类型，而前端没有将对象转化为字符串类型；
		
	- 解决方案:
		1、对照字段名称，类型保证一致性  
		2、使用 stringify 将前端传递的对象转化为字符串：`data: JSON.stringify(param);`

2. handler403

	- 服务器理解请求客户端的请求，但是拒绝执行此请求

3. handler404

	- 服务器无法根据客户端的请求找到资源（网页）。通过此代码，网站设计人员可设置"您所请求的资源无法找到"的个性页面

4. handler500

	- 服务器内部错误，无法完成请求

#### 关于404错误

> 404的错误页面，在模板目录中创建一个404.html的页面
> 
> 在配置文件中 settings.py DEBUG=False
> 
> 在出现404的情况时，自动寻找404页面。
> 
> 也可以在视图函数中 手动报出404错误，带提醒信息

在视图函数中也可以指定返回一个404

```
注意: Http404需要在django.http的模块中引入
# 响应404
raise Http404('找不到')
```

在模板中 404.html

```
<!DOCTYPE html>
<html>
<head>
    <title>404</title>
</head>
<body>
    <center>
        <h2>404 not found</h2>
        <h3>{ {   exception   } }</h3>
    </center>
</body>
</html>
```

## 四,包括其他的URLconf

> 在任何时候，您urlpatterns都可以“包含”其他URLconf模块。
> 
> 这实质上是将一组网址“植根于”其他网址之下

例如，下面是[Django网站](https://www.djangoproject.com/)本身的URLconf的摘录。它包含许多其他URLconf：

```
from django.conf.urls import include, url

urlpatterns = [
    # ... snip ...
    url(r'^community/', include('django_website.aggregator.urls')),
    url(r'^contact/', include('django_website.contact.urls')),
    # ... snip ...
]
```

请注意,此示例中的正则表达式没有`$`(字符串尾匹配字符),但包含尾部斜线

每当Django遇到 include() (`django.conf.urls.include()`)时,它会截断与该点匹配的URL的任何部分,并将剩余的字符串发送到包含的URLconf以进一步处理

## 五,URL的反向解析

如果在视图,模板中使用硬编码的链接,在urlconf发生改变时,维护是一件非常麻烦的事

> 解决：在做链接时，通过指向urlconf的名称，动态生成链接地址  
> 
> 视图：使用django.core.urlresolvers.reverse()函数
>
> 模板：使用url模板标签








