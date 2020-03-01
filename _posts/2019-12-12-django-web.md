---    
layout: post    
title: "Web开发介绍和Django简介"    
date: 2019-12-12 18:26:40    
    
tags:    
- Python    
- Django    
---    
* content    
{:toc}    
    
1. Web开发介绍  
2. Django简介














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







