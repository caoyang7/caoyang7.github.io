---    
layout: post    
title: "PyCharm虚拟环境"    
date: 2019-12-12 18:26:40    
category: 'notes'    
tags:    
- Python    
- 框架    
---    
* content    
{:toc}    
    
# Virtualenv












  [VirtualEnv](https://virtualenv.pypa.io/en/latest/)用于在一台机器上创建多个独立的Python虚拟运行环境,多个Python环境相互独立,互不影响,它能够:
	
	1. 在没有权限的情况下安装新套件  
	2. 不同应用可以使用不同的套件版本  
	3. 套件升级不影响其他应用  

### Ubuntu16.04安装

```
$ [sudo] pip3 install virtualenv
```

### 创建虚拟环境

```
$ virtualenv venv
```

### 激活虚拟环境

```
$ source venv/bin/activave
```

当虚拟环境被激活了,Python解释器的位置会被添加到path中,但是这个改动并不是永久的;它只影响当前命令会话。提醒一下,你激活了虚拟环境,该激活命令会将环境的名称包含在命令提示符里面:

```
(venv) $
```

### 停止虚拟环境

当你在虚拟环境中完成工作并想回到全局Python解释器,在命令提示符中输入`deactivate`就可以了

```
$ deactivate
```

### 使用pip安装python包

大多数的Python包是通过`pip`程序安装的,在创建虚拟环境的时候virtualenv会自动添加进去。当一个虚拟环境被激活后,pip程序的位置会被添加到path中

> 注:如果你使用pyvenv创建虚拟环境在Python3.3中,则必须手动安装pip。安装指令在pip网站上可以找到。在Python3.4下,pyvenv会自动安装pip

比如,安装Flask到虚拟环境中,使用下面的命令:

```
(venv)$ pip install flask
```

通过这个命令,Flask和它的依赖集都会安装到虚拟环境中。你可以验证Flask是否正确安装通过启动Python解释器并试着导入它:

```
(venv)$ python
>>> import flask
>>>
```

如果需要安装的包比较多的时候,这样做会比较繁琐,我们还有一键安装的方法。首先新建一个文本文件,如:requirements.txt,然后将你需要安装的包名保存到该文件中(根据自己的需要),如下:

```
Babel==1.3
Flask==0.10.1
Flask-Login==0.2.7
Flask-SQLAlchemy==1.0
Flask-WTF==0.9.3
Jinja2==2.7.1
SQLAlchemy==0.8.2
WTForms==1.0.5
Werkzeug==0.9.4
psycopg2==2.5.1
```

最后你只需要输入以下命令,所有需要的包就可以全部安装好了:

```
(venv)$ pip install -r requirements.txt
```

如果没有出现错误,就安装成功了

若要查看当前环境安装了哪些包,可以使用下面的命令:

```
(venv)$ pip freeze
```

还可以直接导出到文件中:

```
(venv)$ pip freeze > requirements.txt
```

### 移除环境

删除虚拟环境只需要通过停用虚拟环境并删除环境文件夹及其所有内容即可完成

```
(ENV)$ deactivate
$ rm -  /path/to/ENV
```









