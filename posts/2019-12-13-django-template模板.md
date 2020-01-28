---    
layout: post    
title: "Template模板"    
date: 2019-12-13 18:26:40    
category: 'notes'    
tags:    
- Python    
- Django    
---    
* content    
{:toc}    
    
6. Template模板
















> 作为Web框架，Django需要一种很便利的方法以动态地生成HTML。最常见的做法是使用模板。
> 
> 模板包含所需HTML输出的静态部分，以及一些特殊的语法，描述如何将动态内容插入。

## 一,模板引擎配置

> 模板引擎使用该TEMPLATES设置进行配置。这是一个配置列表，每个引擎一个。
> 默认值为空。在 settings.py由所产生的startproject命令定义一个更有用的值：

```
TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR,'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
```


# 6.1 模板语法

## 一,变量

- 变量输出语法

	```
	{ {  var  } }
	```
	
- 当模版引擎遇到一个变量，将计算这个变量，然后将结果输出  
- 变量名必须由字母、数字、下划线（不能以下划线开头）和点组成  
- 当模版引擎遇到点(".")，会按照下列顺序查询：  
	- 字典查询，例如：foo["bar"]  
	- 属性或方法查询，例如：foo.bar  
	- 数字索引查询，例如：foo[bar]  
- 如果变量不存在， 模版系统将插入'' (空字符串)  
- 在模板中调用方法时不能传递参数

## 二,标签

- 语法

	```
	{ %  tag  % }
	```
	
- 作用

	- 在输出中创建文本  
	- 控制循环或逻辑  
	- 加载外部信息到模板中

#### for标签

```
{ %  for ... in ...  % }
    循环逻辑

{ %  endfor  % }
```

#### if标签

```
{ %  if ...  % }
    逻辑1
{ %  elif ...  % }
    逻辑2
{ %  else  % }
    逻辑3
{ %  endif  % }
```

#### comment标签

```
{ %  comment  % }
    多行注释
{ %  endcomment  % }
```

#### include：加载模板并以标签内的参数渲染

```
{ %  include "base/index.html"  % }
```

#### url:反向解析

```
{ %  url 'name' p1 p2  % }
```

#### csrf_token：这个标签用于跨站请求伪造保护

```
{ %  csrf_token  % }
```

## 三,过滤器

- 语法:

	```
	{ {  变量|过滤器  } }，例如{ {  name|lower  } }，表示将变量name的值变为小写输出
	```
	
- 使用管道符号 (|)来应用过滤器  
- 通过使用过滤器来改变变量的计算结果  
- 关闭HTML自动转义

	```
	{ {  data|safe  } }
	```
	
- 可以在if标签中使用过滤器结合运算符

	```
	if list1|length > 1
	```
	
- 过滤器能够被“串联”，构成过滤器链

	```
	name|lower|upper
	```

- 过滤器可以传递参数，参数使用引号包起来

	```
	list|join:", "
	```

- default：如果一个变量没有被提供，或者值为false或空，则使用默认值，否则使用变量的值

	```
	value|default:"什么也没有"
	```

- date：根据给定格式对一个date变量格式化

	```
	value|date:'Y-m-d'
	```
	
## 四,注释

- 单行注释

	```
	{# #}
	```

- 多行注释

	```
	{ %  comment  % }
		多行注释
	{ %  endcomment  % }
	```
	
## 五,模板运算

- 加

	```
	{ {  value|add:10  } }
	note:value=5,则结果返回15
	```

- 减

	```
	{ {  value|add:-10  } }
	note:value=5,则结果返回-5，加一个负数就是减法了
	```

- 乘

	```
	{ %  widthratio 5 1 100  % }
	note:等同于：(5 / 1) * 100 ，结果返回500，
	withratio需要三个参数，它会使用参数1/参数2*参数3的方式进行运算，进行乘法运算，使「参数2」=1
	```

- 除

	```
	{ %  widthratio 5 100 1  % }
	note:等同于：(5 / 100) * 1,则结果返回0.05,和乘法一样，使「参数3」= 1就是除法了。
	```

## 六,自定义 标签 或 过滤器

```
templatetags
├── pagetag.py
----------------pagetag.py-------------------------
from django import template
register = template.Library()
# 自定义过滤器
@register.filter
def kong_upper(val):
	# print ('val from template:',val)
	return val.upper()

# 自定义标签
from django.utils.html import format_html
@register.simple_tag
def jia(a,b):
	res = int(a) + int(b)
	return res
```

# 6.2 模板继承

- 模板继承可以减少页面内容的重复定义，实现页面内容的重用  
- 典型应用：网站的头部、尾部是一样的，这些内容可以定义在父模板中，子模板不需要重复定义  
- block标签：在父模板中预留区域，在子模板中填充  
- extends继承：继承，写在模板文件的第一行  
- 定义父模板base.html  

	```
	{ %  block block_name  % }
	   这里可以定义默认值
	   如果不定义默认值，则表示空字符串
	{ %  endblock  % }
	```
	
- 定义子模板index.html

	```
	{ %  extends "base.html"  % }
	```
	
- 在子模板中使用block填充预留区域

	```
	{ %  block block_name  % }
	实际填充内容
	{ %  endblock  % }
	```

- 说明:

	- 如果在模版中使用extends标签，它必须是模版中的第一个标签  
	- 不能在一个模版中定义多个相同名字的block标签  
	- 子模版不必定义全部父模版中的blocks，如果子模版没有定义block，则使用了父模版中的默认值  
	- 如果发现在模板中大量的复制内容，那就应该把内容移动到父模板中  
	- 使用可以获取父模板中block的内容  
	- 为了更好的可读性，可以给endblock标签一个名字  

	```
	{ %  block block_name  % }
		区域内容
	{ %  endblock block_name  % }
	```

## 一,三层继承结构

- 三层继承结构使代码得到最大程度的复用，并且使得添加内容更加简单  
- 如下图为常见的电商页面

![scjcjg.png](/img/posts/assets/blog/scjcjg.png)

#### 创建根级模板

- 名称为“base.html”  
- 存放整个站点共用的内容

	```
	<!DOCTYPE html>
	<html>
		<head>
			<title>{ %  block title  % }{ %  endblock  % } 水果超市</title>
		</head>
		<body>
			top--
			<hr/>
			{ %  block left  % }

			{ %  endblock  % }

			{ %  block content  % }

			{ %  endblock  % }
			<hr/>
			bottom
		</body>
	</html>
	```

#### 创建分支模板

- 继承自base.html  
- 名为“base_*.html”  
- 定义特定分支共用的内容  
- 定义base_goods.html

	```
	{ %  extends 'temtest/base.html'  % }

	{ %  block title  % }商品{ %   endblock   % }

	{ %  block left  % }
		<h1>goods left</h1>
	{ %  endblock  % }
	```

- 定义base_user.html

	```
	{ %  extends 'temtest/base.html'  % }

	{ %  block title  % }用户中心{ %  endblock   % }

	{ %  block left  % }
		<font color='blue'>user left</font>
	{ %  endblock  % }
	```

- 定义index.html，继承自base.html，不需要写left块

	```
	{ %  extends 'temtest/base.html'  % }

	{ %  block content  % }
		首页内容
	{ %  endblock content  % }
	```

#### 为具体页面创建模板,继承自分支模板

- 定义商品列表页goodslist.html

	```
	{ %  extends 'temtest/base_goods.html'  % }
	{ %  block content  % }
		商品正文列表
	{ %  endblock content  % }
	```

- 定义用户密码页userpwd.html

	```
	{ %  extends 'temtest/base_user.html'  % }
	{ %  block content  % }
		用户密码修改
	{ %  endblock content  % }
	```

#### 视图调用具体页面，并传递模板中需要的数据

- 首页视图index

	```
	logo='welcome to itcast'
	def index(request):
		return render(request, 'temtest/index.html', {'logo': logo})
	```
	
- 商品列表视图goodslist

	```
	def goodslist(request):
		return render(request, 'temtest/goodslist.html', {'logo': logo})
	```
	
- 用户密码视图userpwd

	```
	def userpwd(request):
		return render(request, 'temtest/userpwd.html', {'logo': logo})
	```

#### 配置url

	```
	from django.conf.urls import url
	from . import views
	urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'^list/$', views.goodslist, name='list'),
		url(r'^pwd/$', views.userpwd, name='pwd'),
	]
	```




