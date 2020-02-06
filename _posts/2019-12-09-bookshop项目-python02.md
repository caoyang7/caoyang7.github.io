---
layout: post
title: "Django项目开发流程 bookshop"
date: 2019-12-09 18:26:40
category: 'notes'
tags:
- Python
- 项目
- Django
---
* content
{:toc}

Django项目开发流程 bookshop项目总结













# 项目简介
### 项目描述
1. 项目名称:图书商城管理系统  
2. 架构:前后端不分离MVT  
3. 成果:完整的支付流程,除了后台列表和新增其余相似功能只做一遍  
4. 开发周期:2019/12/09-2019/12/20  
5. 收获:熟悉了Django框架,知道了一个项目整体结构,基本功能都能实现了

### 项目技术
1. [Python3.7](https://docs.python.org/3.7/)  
2. [Django2.2](https://docs.djangoproject.com/en/2.2/)  
3. [jQuery(js框架)](https://api.jquery.com/)  
4. [amazeui(css框架)](http://amazeui.shopxo.net/getting-started/?_ver=2.x)  
5. [MySQL5.7](https://dev.mysql.com/doc/refman/5.7/en/)

### 应用软件
1. PyCharm  
2. Sqlyog  
3. 花生壳  
4. 支付宝开发助手1.0.2  
5. Xftp6.0  
6. Xshell6.0  

### 包文件
```
(venv) D:\OngoingProjects\bookshop>pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

Django==2.2.3
mysqlclient==1.4.4
Pillow==6.2.0
requests==2.22.0
pycryptodomex==3.7.2
pycryptodome==3.9.0
python-alipay-sdk==1.10.1
```

# 需求分析

### 创建流程
1. 创建github或码云仓库  
2. 克隆到本地(这里用的http协议)`git clone https://gitee.com/caoyang7/bookshop.git`  
3. 编写readme文件  
4. 创建虚拟环境`python -m venv venv`  
5. 进入虚拟环境`cd venv/Scripts`,运行虚拟环境`activate`  
6. 右键以pycharm项目形式打开,检查当前环境是否是虚拟环境  
7. 安装环境包  
	django2.2.6  
	mysqlclient  
8. 在bookshop文件夹下创建项目`django-admin startproject web`  
9. 新建templates和static文件夹,修改settings.py文件  
10. 创建数据库`create database bookshop default charset=utf8mb4;`  
11. 写视图函数和路由  
12. 推到码云  
	添加远程仓库地址`git remote set-url --add origin git@gitee.com:caoyang7/bookshop.git`  
	删除远程仓库地址`git remote set-url --delete origin https://gitee.com/caoyang7/bookshop.git`  
	查看远程仓库地址`git remote -v`  
	给码云配置公钥,在`C:user/caoya/.ssh/id_rsa.pub`  
	提交到远程仓库`git commit -m"图书商城django项目初始化"`  
	推`git push origin`  

### 搜索和分页
[Django分页官方文档](https://docs.djangoproject.com/en/2.2/topics/pagination/)

