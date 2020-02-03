---
layout: post
title: "Python基础自测"
date: 2222-01-13 13:26:40
category: 'notes'
tags:
- 考试
---
* content
{:toc}

基础太差,记性不好,就得补起来,加油,问题不大








# 1. Python简介及安装
### 1.1. Python简介
1. 什么是Python?  
2. Python是谁发明的?  
3. Python的语言特色?  
4. Python的应用领域?  
5. Python的优势?

### 1.2. 安装及版本检测
1. Python目前有几个主流的版本?  
2. 如何检测当前环境中Python的版本?  

### 1.3. 第一个Python程序
1. Python如何运行?

# 2. Python基本语法
### 2.1. 注释及语句分类
1. Python有哪几种注释?  
2. Python语句分类?

### 2.2. 命名方式和关键字
1. 什么是标识符？什么是关键字？如何查看系统保留关键字?  
2. 分别用大驼峰、小驼峰、下划线分隔三种形式给变量命名?  
3. 文件命名规则?  
4. 文件后缀有哪些?查看文件后缀的方法有哪些?  

# 3. 变量和数据类型
### 3.1. 变量
1. 什么是变量?  
2. 变量的命名规范?  
3. 变量赋值的格式?  
4. 如何获取变量值?查看数据类型?获取变量在内存中的id标识?

### 3.2. 数据类型
1. 系统默认提供了几种数据类型?  
2. 数据类型是如何定义的呢?  
3. 什么是转义字符?转义字符有哪些?换行和回车的区别?  

### 3.3. 数据类型转换
1. 显式转换 和 隐式转换 的区别是?  
2. 数据类型如何转换?  
3. 有哪些数据转换为布尔值时得到的结果是False?

### 3.4. 运算和运算符
1. 运算的分类?  
2. 算数运算符?除法,取商,底板除的区别?  
3. 关系运算/比较运算?  
4. 赋值运算?  
5. 逻辑运算?  
6. 位运算?  
7. 成员运算?  
8. 身份检测?  
9. 运算优先级?  
10. 如何检测数据归属类型?

# 4. 流程控制
### 4.1. 顺序结构和分支结构
1. 什么是流程?什么是流程控制?流程控制分类?  
2. 分支结构有哪几种?有什么特征?  

### 4.2. 循环结构
1. 为什么用循环结构?  
2. Python中循环结构分类?语法格式?  
3. 什么是死循环?  
4. else的用法和作用?  
5. 流程控制语句有哪些?作用是什么?  

# 5. 函数及作用域
### 5.1. 函数
1. 函数的作用?  
2. 函数名的命名规则?  
3. 函数的定义?语法格式?  
4. 函数的调用方式?  
5. 参数的分类?  
6. 多种参数怎么混合使用?  
7. 两种函数的返回值类型?  
8. return的用法?  
9. 什么是递归函数?什么时候使用递归函数?  

### 5.2. 函数文档
1. 查看函数文档的方法?  
2. 定义函数文档的方法?  
3. 函数文档的内容?  

### 5.3. 变量作用域
1. 变量按作用域分为哪几种?有什么特点?  
2. global关键字的使用?

### 5.4. 内部函数和闭包操作
1. 什么是内部函数?语法格式?使用方法?  
2. 什么是闭包?语法格式?  
3. 闭包的优缺点?  
4. 闭包环境查看?  
5. nonlocal关键字的使用?

### 5.5. lambda表达式
1. lambda表达式的语法结构?  
2. lambda表达式的优缺点?  

# 6. 内置函数及操作
### 6.1. 字符串相关
1. 字符串操作?  
2. 字符串函数?  
	- capitalize()  
	- title()  
	- upper()/lower()  
	- swapcase()  
	- len()  
	- count()  
	- find()/index()  
	- startswith()/endswith()  
	- isupper()/islower()  
	- isalnum()/isalpha()  
	- isdigit()/isnumeric()/isdecimal()  
	- isspace()  
	- istitle()  
	- split()/splitlines()  
	- join()  
	- zfill()  
	- center()/ljust()/rjust()  
	- strip()/lstrip()/rstrip()  
	- maketrans()和translate()

### 6.2. format格式字符串
1. format格式字符串语法格式?  
2. 格式限定符号有哪些?  

### 6.3. 内建函数
1. 类型相关  
2. 变量相关  
	- id()  
	- type()  
	- print()  
	- locals()  
3. 数学相关  
	- abs()  
	- sum()  
	- max()/min()  
	- pow()  
	- round()  
	- range()  
4. 进制相关  
	- hex()/oct()/bin()  
	- chr()/ord()  
	- repr()  
	- eval()

### 6.4. 列表
1. 创建列表?  
2. 基本操作  
	- 访问列表中的元素  
	- 修改列表中的元素  
	- 添加列表元素  
	- 删除列表中的元素  
	- 删除整个列表  
3. 序列操作  
	- 序列相加  
	- 列表相乘  
	- 索引操作  
	- 分片操作  
	- 成员检测  
4. 序列操作函数  
5. 列表的遍历操作?  
6. 列表内涵/列表推导式?  
7. 列表专用函数  
	- append()  
	- clear()  
	- copy()  
	- count()  
	- extend()  
	- index()  
	- insert()  
	- pop()  
	- remove()  
	- reverse()  
	- sort()  

### 6.5. 元组
1. 创建元组?  
2. 基本操作  
	- 访问元组中的元素  
3. 元组操作  
	- 元组相加  
	- 元组相乘  
	- 索引操作  
	- 分片操作  
	- 成员检测  
4. 元组操作函数  
5. 元组的遍历操作?  
6. 元组内涵/元组推导式?  
7. 列表专用函数  
	- count() 
	- index()  

### 6.6. 字典
1. 创建元组?  
2. 基本操作  
	- 访问字典中的元素  
	- 修改字典中的元素  
	- 添加字典元素  
	- 删除字典中的元素  
	- 删除整个字典  
	- 成员检测  
3. 序列操作  
	- 成员检测  
4. 字典操作函数  
5. 字典的遍历操作?  
6. 元组内涵/元组推导式?  
7. 列表专用函数  
	- clear()  
	- copy()  
	- fromkeys()  
	- get()  
	- items()  
	- keys()  
	- values()  
	- pop()/popitem()  
	- setdefault()  
	- update()  

### 6.7. 集合
1. 什么是集合?  
2. 创建集合  
3. 集合的序列操作  
	- 成员检测  
4. 集合的序列函数  
5. 集合的遍历  
6. 集合内涵/推导式  
7. 集合专用函数  
	- add()  
	- pop()/remove()/discard()  
	- clear()  
	- copy()  
	- difference()/difference_update()  
	- intersection()/intersection_update()  
	- union()/update()  
	- issuperset()  
	- issubset()  
	- isdisjoint()  
	- symmetric_difference()/symmetric_difference_update()  
8. 冰冻集合/固定集合
	- 创建冰冻集合  
	- 冰冻集合的遍历  

### 6.8. 文件操作
1. 文件的基本操作  
	- open()  
	- 打开模式?  
	- read()  
	- write()  
	- close()  
2. 读写函数  
	- read()/readline()/readlines()  
	- write()/writelines()  
	- truncate()  
3. 文件指针操作  
	- tell()  
	- seek()  
4. 什么是字符,字节,字符集?  


# 7. 常用的模块
### 7.1. String模块
1. String模块函数  
	- ascii_letters()  
	- ascii_uppercase()/ascii_lowercase()  
	- digits()/octdigits()/hexdigits()  
	- printable()  
	- whitespace()  
	- punctuation()  
2. python中与ascii码相关的两个函数?  
	- chr()  
	- ord()  
3. 什么是ASCII码?  
4. AZaz09对应的ASCII码?  

### 7.2. 数学模块
1. 数学模块函数  
	- ceil()/floor()/round()  
	- pow()  
	- sqrt()  
	- fabs()/abs()  
	- modf()  
	- copysign()  
	- fsum()/sum()
2. 数学模块提供的常见值  
	- pi  
	- e  
3. 随机模块  
	- random()  
	- choice()  
	- shuffle()  
	- rangrange()  
	- uniform()  

### 7.3. os模块
1. os模块中的函数
	- getcwd()  
	- chdir()  
	- listdir()  
	- mkdir()/makedirs()  
	- rmdir()/removedirs()  
	- rename()  
	- stat()  
	- system()  
	- getenv()/putenv()  
	- exit()  
2. 当前os模块的值  
	- curdir()  
	- pardir()  
	- path()  
	- name()  
	- sep()/extsep()/linesep()  
3. os.environ模块是干啥的  
4. os.path模块函数  
	- abspath()  
	- basename()  
	- dirname()  
	- join()  
	- split()/splitext()  
	- getsize()  
	- isfile()/isdir()  
	- getctime()/getmtime()/getatime()  
	- exists()  
	- isabs()  
	- islink()  
	- samefile()  
5. 相对路径和绝对路径的区别

### 7.4. zip压缩
### 7.5. shutil模块
1. shutil模块函数  
	- copy()/copy2()/copyfileobj()/copyfile()/copytree()/copymode()/copystat()  
	- rmtree()/move()  
	- which()  
	- disk_usage()  
2. 什么是归档,解包,压缩,解压缩?  
3. 归档和解包操作函数  
	- make_archive()  
	- unpack_archive()  
	- get_archive_formats()  
	- get_unpack_formats()

### 7.6. 与时间相关的模块
1. 日历模块  
	- calendar()  
	- month()  
	- monthcalendar()  
	- isleap()  
	- leapdays()  
	- monthrange()  
	- weekday()  
	- timegm()  
2. time模块的概念  
	- 什么是时间戳?  
	- 什么是UTC时间?  
	- 什么是夏令时?  
	- 什么是时间元组?  
3. 时间模块的值  
	- timezone  
	- altzone  
	- daylight  
4. 时间模块的函数  
	- asctime()  
	- localtime()  
	- gmtime()  
	- ctime()  
	- mktime()  
	- clock()  
	- perf_counter()  
	- sleep()  
	- time()  
	- strftime()  
	- strptime()  

# 8. 面向对象
### 8.1. 类和对象-上
### 8.2. 魔术方法
### 8.3. 类和对象-下
### 8.4. 装饰器和抽象类
### 8.5. 错误和异常处理
# 9. 初级项目-计算器
### 9.1. 模块和包
### 9.2. tkinter模块
### 9.3. 简易计算器示例






