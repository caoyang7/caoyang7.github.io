---    
layout: post    
title: "Model模型"    
date: 2019-12-13 18:26:40    
category: 'notes'    
tags:    
- Python    
- Django    
---    
* content    
{:toc}    
    
4. Model模型












# 4. Model模型

> 模型是你的数据的唯一的、权威的信息源。它包含你所存储的数据的必要字段和行为。
>  
> 通常,每个模型对应数据库中唯一的一张表。

- 每个模型都是django.db.models.Model的一个Python 子类。

- 模型的每个属性都表示为数据库中的一个字段。

- Django 提供一套自动生成的用于数据库访问的API；

- 这极大的减轻了开发人员的工作量，不需要面对因数据库变更而导致的无效劳


## 一,模型与数据库的关系

> 模型(Model)负责业务对象和数据库的关系映射(ORM)

ORM是“对象-关系-映射”的简称，主要任务是：

1. 根据对象的类型生成表结构  
2. 将对象、列表的操作，转换为sql语句  
3. 将sql查询到的结果转换为对象、列表

## 二,为什么要用模型

Model是MVC框架中重要的一部分,主要负责程序中用于处理数据逻辑的部分。通常模型对象负责在数据库中存取数据

它实现了数据模型与数据库的解耦，即数据模型的设计不需要依赖于特定的数据库，通过简单的配置就可以轻松更换数据库

## 三,配置MySQL数据库

1. 在当前环境中安装mysql

	```
	sudo apt-get install mysql-server
	
	sudo apt install mysql-client
	
	sudo apt install libmysqlclient-dev
	```
	
2. 在当前Python环境中安装pymysql

	```
	pip3 install pymysql
	```
	
3. 在mysql中创建数据库

	```
	create database mydb default charset=utf8
	```
	
4. 在Django项目中配置数据库

	修改settings.py文件中的DATABASE配置项

	```
	DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',#选择数据库的名,请确认你的mysql中有这个库
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
        }
	}
	```
	
5. 告诉Django在接下来的mysql操作中使用pymysql

	打开mysite/__init__.py，写入以下代码导入pymysql：
	
	```
	import pymysql
	pymysql.install_as_MySQLdb()
	```

## 四,开发流程

1. 在models.py中定义模型类，要求继承自models.Model

	```
	from django.db import models

	# Create your models here.

	#用户信息模型
	class Users(models.Model):
			username = models.CharField(max_length=32)
			password = models.CharField(max_length=32)
			email = models.CharField(max_length=50)

		 # class Meta:
		 #    db_table = "polls_users"  # 指定表名
	```
	
2. 把应用加入settings.py文件的installed_app项

	编辑mysite/settings.py文件，并将项目应用文件名添加到该INSTALLED_APPS设置。
	
	```
	INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myweb',
	]
	```
	
3. 生成迁移文件

	```
	python3 manage.py makemigrations
	```
	
4. 执行迁移

	```
	python3 manage.py migrate
	```
	
5. 使用模型类进行crud操作


# 4.1 定义模型

> 在模型中定义属性，会生成表中的字段
> django会为表增加自动增长的主键列，每个模型只能有一个主键列
> 如果使用选项设置某属性为主键列后，则django不会再生成默认的主键列
> 属性命名限制
> 
> - 不能是python的保留关键字
> - 由于django的查询方式，不允许使用连续的下划线

## 一,定义属性

- 定义属性时，需要字段类型  
- 字段类型被定义在django.db.models.fields目录下，为了方便使用，被导入到django.db.models中  
- 使用方式  
	1. 导入from django.db import models  
	2. 通过models.Field创建字段类型的对象，赋值给属性  
- 对于重要数据都做逻辑删除，不做物理删除，实现方法是定义isDelete属性，类型为BooleanField，默认值为False  

#### 字段类型

- AutoField：一个根据实际ID自动增长的IntegerField，通常不指定  
	- 如果不指定，一个主键字段将自动添加到模型中  
- BooleanField：true/false 字段，此字段的默认表单控制是CheckboxInput  
- NullBooleanField：支持null、true、false三种值  
- CharField(max_length=字符长度)：字符串，默认的表单样式是 TextInput  
- TextField：大文本字段，一般超过4000使用，默认的表单控件是Textarea  
- IntegerField：整数  
- DecimalField(max_digits=None, decimal_places=None)：使用python的Decimal实例表示的十进制浮点数  
	- DecimalField.max_digits：位数总数  
	- DecimalField.decimal_places：小数点后的数字位数  
- FloatField：用Python的float实例来表示的浮点数  
- DateField[auto_now=False, auto_now_add=False])：使用Python的datetime.date实例表示的日期  
	- 参数DateField.auto_now：每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为false  
	- 参数DateField.auto_now_add：当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为false  
	- 该字段默认对应的表单控件是一个TextInput. 在管理员站点添加了一个JavaScript写的日历控件，和一个“Today"的快捷按钮，包含了一个额外的invalid_date错误消息键  
	- auto_now_add, auto_now, and default 这些设置是相互排斥的，他们之间的任何组合将会发生错误的结果  
- TimeField：使用Python的datetime.time实例表示的时间，参数同DateField  
- DateTimeField：使用Python的datetime.datetime实例表示的日期和时间，参数同DateField  
- FileField：一个上传文件的字段  
- ImageField：继承了FileField的所有属性和方法，但对上传的对象进行校验，确保它是个有效的image  

#### 字段选项

- 通过字段选项，可以实现对字段的约束  
- 在字段对象时通过关键字参数指定  
- null：如果为True，Django 将空值以NULL 存储到数据库中，默认值是 False  
- db_column：字段的名称，如果未指定，则使用属性的名称  
- db_index：若值为 True, 则在表中会为此字段创建索引  
- default：默认值  
- primary_key：若为 True, 则该字段会成为模型的主键字段  
- unique：如果为 True, 这个字段在表中必须有唯一值  

## 二,元选项

- 在模型类中定义类Meta，用于设置元信息  
- 元信息db_table：定义数据表名称，推荐使用小写字母  
- 数据表的默认名称:<app_name>_<model_name>  
- 例如myweb_users  

- ordering：对象的默认排序字段，获取对象的列表时使用，接收属性构成的列表

	```
	class BookInfo(models.Model):
			...
			class Meta():
					ordering = ['id']
	```

- 字符串前加"-"表示倒序，不加"-"表示正序

	```
	class BookInfo(models.Model):
			...
			class Meta():
					ordering = ['-id']
	```

- 排序会增加数据库的开销

## 三,案例

	```
	class Stu(models.Model):
		sid = models.AutoField(primary_key=True)
		name = models.CharField(max_length=50)
		age = models.IntergerField()
		
		class Meta():
			db_table = 'stu'
			
		def __str__(self):
			return self.name
	```


# 4.2 模型实例

## 一,模型属性

- objects：是Manager类型的对象，用于与数据库进行交互

- 当定义模型类时没有指定管理器，则Django会为模型类提供一个名为objects的管理器

- 支持明确指定模型类的管理器

	```
	class BookInfo(models.Model):
		...
		books = models.Manager()
	```

当为模型类指定管理器后，django不再为模型类生成名为objects的默认管理器

## 二,创建对象

- 当创建对象时，django不会对数据库进行读写操作

- 调用save()方法才与数据库交互，将对象保存到数据库中

- 说明：init方法已经在基类models.Model中使用，在自定义模型中无法使用，

## 三,实例的属性

- DoesNotExist：在进行单个查询时，模型的对象不存在时会引发此异常，结合try/except使用

## 四,实例的方法

- str(self)：重写object方法，此方法在将对象转换成字符串时会被调用

- save()：将模型对象保存到数据表中

- delete()：将模型对象从数据表中删除



# 4.3 模型查询

## 一,查询集

> 在管理器上调用过滤器方法会返回查询集,查询集表示从数据库中获取的对象集合
> 
> 查询集经过过滤器筛选后返回新的查询集，因此可以写成链式过滤
>
> 惰性执行：创建查询集不会带来任何数据库的访问，直到调用数据时，才会访问数据库
> 
> 何时对查询集求值：迭代，序列化，与if合用
> 
> 返回查询集的方法，称为过滤器

- all()  
- filter()  
- exclude()  
- order_by()  
- values()：一个对象构成一个字典，然后构成一个列表返回
 
- 写法:

	```
	filter(键1=值1,键2=值2)
	等价于
	filter(键1=值1).filter(键2=值2)
	```

#### 返回单个值的方法

- get()：返回单个满足条件的对象

	- 如果未找到会引发"模型类.DoesNotExist"异常  
	- 如果多条被返回，会引发"模型类.MultipleObjectsReturned"异常

- count()：返回当前查询的总条数

- first()：返回第一个对象

- last()：返回最后一个对象

- exists()：判断查询集中是否有数据，如果有则返回True

#### 限制查询集

- 查询集返回列表，可以使用下标的方式进行限制，等同于sql中的limit和offset子句

- 注意：不支持负数索引

- 使用下标后返回一个新的查询集，不会立即执行查询

- 如果获取一个对象，直接使用[0]，等同于[0:1].get()，但是如果没有数据，[0]引发IndexError异常，[0:1].get()引发DoesNotExist异常

	```
	#这会返回前5个对象 LIMIT 5
	Entry.objects.all()[:5]

	#这将返回第六个到第十个对象 OFFSET 5 LIMIT 5
	Entry.objects.all()[5:10]
	```

## 二,字段查询

- 实现where子名，作为方法filter()、exclude()、get()的参数  
- 语法：属性名称__比较运算符=值  
- 表示两个下划线，左侧是属性名称，右侧是比较类型  
- 对于外键，使用“属性名_id”表示外键的原始值  
- 转义：like语句中使用了%与，匹配数据中的%与，在过滤器中直接写，例如：filter(title__contains="%")=>where title like '%\%%'，表示查找标题中包含%的

#### 比较运算符

- exact：表示判等，大小写敏感；如果没有写“ 比较运算符”，表示判等

	```
	filter(isDelete=False)
	```

- contains：是否包含，大小写敏感

	```
	exclude(btitle__contains='传')
	```

- startswith、endswith：以value开头或结尾，大小写敏感

	```
	exclude(btitle__endswith='传')
	```

- isnull、isnotnull：是否为null

	```
	filter(btitle__isnull=False)
	```

- 在前面加个i表示不区分大小写，如iexact、icontains、istarswith、iendswith

- in：是否包含在范围内

	```
	filter(pk__in=[1, 2, 3, 4, 5])
	```

- gt、gte、lt、lte：大于、大于等于、小于、小于等于

	```
	filter(id__gt=3)
	```

- year、month、day、week_day、hour、minute、second：对日期间类型的属性进行运算

	```
	filter(bpub_date__year=1980)
	filter(bpub_date__gt=date(1980, 12, 31))
	```
	
## 三,用Q对象进行复杂查找

关键字参数查询

	- 输入[filter()](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#django.db.models.Q)等

	- “AND”编辑在一起的。如果您需要执行更复杂的查询（例如，带有OR语句的查询），则可以使用[Qobjects](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#django.db.models.query.QuerySet.filter)

例如 查询or“或”的对象
	
	```
	# Q对象 
	from django.db.models import Q

	ob = Goods.objects.filter(Q(id__contains=v)|Q(title__contains=v))
	```
	
#### 其他查询方案

	```
	# 模型提供 extra
	ob = Types.objects.extra(select = {'paths':'concat(path,id)'}).order_by('paths')
	#等同于
	select *,concat(path,id) as paths from types order by paths;
	```

# 4.4 模型关系

## 一,OneToOneField 一对一

> 将字段定义在任意一端中
> 
> 创建两个模型类 Users UserInfo
> 
> 例如: 一个用户信息,对应一个用户详情信息

```
# 用户    
class Users(models.Model):
    username = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'用户名')

    class Meta:
        db_table = 'Users'

#用户详情
class UserInfo(models.Model):
    # 在用户详情表中，关联用户表，让两个表的数据产生联系
    # 第一个参数：是被关联的模型名称
    # 第二个参数：当user用户表中的一条数据被删除的时候，与之对应的详情表数据也会被删除
    uid = models.OneToOneField(Users, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'UserInfo'

增:
    a = Users(username=request.POST['username'])
    a.save()
    b = UserInfo(uid=a,address=request.POST['address'])
    b.save()
    return HttpResponse('<script>location.href="/"</script>')
删:
    a1 = Users.objects.get(id=uid)
    a1.delete()
改:
    a = Users.objects.get(id=request.POST['uid'])
    a.username = request.POST['username']
    a.save()
    b = UserInfo.objects.get(uid=request.POST['uid'])
    b.address = request.POST['address']
    b.save()
查:
    # 通过用户查详情
    users = Users.objects.all()
    uinfo = Users.objects.get(id=uid)
      # print(users[0].userinfo.address)

    # 通过详情查用户
```

## 二,ForeignKey 一对多

> 将字段定义在多的端中
> 
> 例如: 一个班级对应多个学员信息
> 
> 创建两个模型 Class Stu

```
# 班级
class Class(models.Model):
    id = models.AutoField(primary_key=True)
    classname = models.CharField(max_length=32)
    class Meta:
        db_table = 'Class'

    def __str__(self):
        return self.classname

# 学员
class Stu(models.Model):
    id = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=32)

    # 一对多
    cid = models.ForeignKey(to="Class", to_field="id")

    class Meta:
        db_table = 'Stu'

    def __str__(self):
        return self.sname

 # 查询所有学员
# b = Stu.objects.all()

# print(b) #<QuerySet [<Stu: 张三>, <Stu: 李四>, <Stu: 王五>, <Stu: 赵六>]>

# 通过学员信息,查询所在班级
# print(b[1].cid.classname)


# # 查询所有班级
# a = Class.objects.all()
# # print(a[0].classname)
# # print(a[0].classname)
# # print(a[1].classname)

# # 通过班级,查询所有学员信息
# # print(a[1].stu_set.all()) #<QuerySet [<Stu: 张三>, <Stu: 王五>]>
# print(a[1].students.all())

# 修改
    # 获取id为2的学员信息,转移班级到1期
    # c = Class.objects.get(id=1)

    # ob = Stu.objects.get(id=2)
    # ob.sname = '李思思'
    # ob.cid=c

    # ob.save()
# 添加

    # ob = Stu()
    # ob.sname = '张三丰'
    # ob.cid = Class.objects.get(id=1)
    # ob.save()

# 删除
    # 如果删除班级,那么班级对应的学员信息也会被删除
    # c = Class.objects.get(id=2)
    # c.delete()
    # 如果删除学员,对班级信息没有影响
    # c = Stu.objects.get(id=2)
    # c.delete()
```

## 三,ManyToManyField 多对多

> 只将它放在其中一个模型中 - 而不是两个模型
> 
> 创建两个模型类 Class Teacher
> 
> 例如: 一个班级需要多个老师代课,一个老师要带多个班级

```
# 班级
class Class(models.Model):
    id = models.AutoField(primary_key=True)
    classname = models.CharField(max_length=32)
    class Meta:
        db_table = 'Class'

    def __str__(self):
        return self.classname


# 讲师信息表
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=32)
    cid = models.ManyToManyField(to="Class")

    def __str__(self):
        return self.tname

#添加
# 添加班级
    # p1 = Class(classname='py1期')
    # p1.save()
    # p2 = Class(classname='py2期')
    # p2.save()

# 添加老师
    # a1 = Teacher(tname='王老师')
    # a1.save()

# 添加老师进班级
    # w = Teacher.objects.get(id=4)
    # c = Class.objects.get(id=5)
    # w.cid.add(c)

    # 获取所有班级
    # p = Class.objects.all()
    # a2 = Teacher(tname='浩老湿')
    # a2.save()
    # 把一个老师,添加进多个班级
    # a2.cid.add(p[0], p[1])

# 查询

    # 通过班级 查询老师信息
        # c = Class.objects.first()
        # print(c)
        # print(c.cname)
        # print(c.teacher_set.all())

    # 通过老师,查询班级信息
        t = Teacher.objects.first()
        print(t)
        print(t.tname)
        print(t.cid.all())
```

