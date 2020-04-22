---
layout: post
title: "Django项目开发流程 bookshop"
date: 2019-12-09 18:26:40

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



# bug
### 返回码
403: 拒绝

---
404: 找不到路径

---
500: 服务器内部错误(不用看控制台了,终端中有报错)

### 装了好几个版本的Python,如python2.7,python3.7.2,python3.7.4,python3.8,用乱了

解决方案:把多余的删喽,都想留下的话就配个环境变量,最上面的就是命令行输入python回车默认的,其他的去安装目录改个名就好了,然后在PyCharm里重新导一下解释器,详情请见: [多个版本的 Python 在使用中的灵活切换](https://blog.csdn.net/sylan15/article/details/78389437)

总结:有的时候报版本的错问题不一定真的出在这,尤其是照着代码敲的就更好改了,哪块报错就把哪块的代码注释了,然后把源码复制过来,如果运行没有问题那就是你哪块写错了,一对比就能看出来

### Linux系统里pycharm打不开了

原因:没有权限

解决方案:进入usr/share文件夹,修改pycharm文件夹及子文件的权限`chmod -R 777 pycharm`,'-R'是指子文件的权限也一起修改

总结:遇到软件问题,一定要条理清晰,先搜一下报错信息,什么意思,什么原因,怎么改,但也别乱改,有的时候给你报的错不一定反应根本原因,先回忆一下咋装的,想不起来就去搜个教程,按照教程检查一下,没问题的话就不是安装和破解的原因,那可能就是权限问题或者环境问题。快速定位也很重要,一定要知道各个文件夹都是干啥的

### python版本太多,pip用不明白了,而且项目组版本不一致有冲突,就把多余的卸了,然后也卸不干净疯狂报错,直接删了一堆残留文件,重装后也有问题

原因:电脑里好几个版本的Python,因为之前的问题找解决方案对python进行了修改,关键是忘了改啥了,导致不能直接卸载,所以直接删了文件夹,没有走正规流程,而且本身就好几个版本,都有残余文件

解决方案:

	- 针对当前问题去网上搜了一堆解决方案,都失败了
	- 最终"系统还原"到指定时间: [如何初始化windows](https://jingyan.baidu.com/article/49ad8bce4d964c5834d8faa3.html)
	- 再搜索"如何彻底卸载python",去控制面板卸载,或者检查版本号,然后用安装包卸载都行,但我都不是,忘了咋卸的了
	- 根据流程卸载,卸载3.8时报错说遇到重大问题,经过分析是我之前修改了文件名和文件夹路径,恢复后删除成功
	- 但是还有残留文件,经过搜索删除了注册表里的python相关信息(regedit,然后F3搜索)

总结:没有什么解决不了的问题,就是时间问题,睡一觉或者干点别的思路就清晰了,还有以后不管干啥一定要记下来和写readme,应用的解决方案链接赶紧保存一份,要不是真忘啊

### TemplateDoesNotExist

原因:setting里配置错误/文件夹命名或位置错误

解决方案:

	- [TemplateDoesNotExist at/****](https://blog.csdn.net/sunny_summergood/article/details/79194883)  
	- [django.template.exceptions.TemplateDoesNotExist: blog/index.html](https://blog.csdn.net/weixin_36571185/article/details/73609102)

总结:报的500错误,不是404,一开始就有点想偏了,但人家都把异常给你显示出来了,模板不存在,那就是路径问题被,先检查一下命名是否正确,再检查一下位置是否正确,然后检查setting里配置的是否是你想要的,最后再检查路由代码等问题,你查错顺序怎么还整反了捏!还有以后别报错就去对照代码,可能会因为版本问题,他对你不对,先百度翻译一下,在搜一下原因,分析原因去解决,print,debug用熟了嘛??

### 为节省屏幕空间，用PyCharm菜单View把菜单栏隐藏了，后觉的不便找不到了

解决方案:双击Shift键，出‘搜索’弹出窗口，输入View(中文或是‘视图’？）可以搜出View，点击View进入View菜单，选择显示菜单栏即可！

总结:下次点啥之前注意着点快捷键,要不点没了搜都不知道叫啥

### 表单提交CSRF验证失败,请求中止 403

原因:  

	未设置CSRF cookie。对于POST表单，您需要确保：  
	
		- 您的浏览器正在接受Cookie。  
		- 视图函数将a传递request给模板的render 方法。  
		- 在模板中, { %  c s r f _ t o k e n  % } 每个POST表单内都有一个模板标记，该标记以内部URL为目标。  
		- 如果您没有使用CsrfViewMiddleware，那么您必须 csrf_protect在使用 csrf_token template 标签的所有视图以及接受POST数据的视图上使用。  
		- 该表单具有有效的CSRF令牌。登录另一个浏览器选项卡或登录后单击“后退”按钮后，您可能需要使用表单重新加载页面，因为登录后令牌会旋转。  

解决方案:在ajax之前设置数据/取消保护
	
	方法一:在表单中加上 { %  c s r f _ t o k e n  % } ,会给你生成一个隐藏的input表单
	
	方法二:[在AJAX请求上设置令牌](https://docs.djangoproject.com/en/3.0/ref/csrf/)
	
	方法三:看课件,在js中加上
		```
		$.ajaxSetup({
			data:{csrfmiddlewaretoken:'{ { c s r f _ t o k e n } }'},
		});
		```
	
	方法四:在视图函数中用装饰器取消保护,看课件
		```
		from django.views.decorators.csrf import csrf_exempt
		@csrf_exempt
		```
	
	方法五:如果所有的都取消,可以把settings中的相关代码注释掉
	
总结: 
```
在Django框架里面有一个CSRF机制,它专门针对post提交,post请求必须加一个CSRF,加上CSRF后它会给你生成个口令叫"csrf_token令牌",请求表单的时候这个令牌就会把内容记录到浏览器里边,提交的时候口令会随着表单里的内容一起提交上去,并且浏览器请求也有一个口令,这两个口令再加服务器生成的口令,去对照,一样就没有问题,防止跨站请求伪造,CSRF攻击
```

### GitHub Pages无法建立您的网站。

原因: 第csrf_token75行中的标签_posts/2019-11-29-python问题.md不是公认的液体标签。

解决方案: 总有些东西浏览器给它自动解析,一开始没有注意到问题根本原因,又回滚版本,又重新克隆的,后来才想起来github报错有提示,点进去找到了原因,但是经过多次查询和尝试,如:用代码块,用引号,用转义,用元字符,甚至写成超连接的形式都不行,最后决定在每个字母前加一个空格

总结:虽然没有解决根本问题,但是如果是不影响其他地方的小问题,又已经耗费了大量时间,实在解决不了,能逃避问题也是很好的选择

### 图片上传不上去

原因: 思路不够清晰,没能迅速定位,文件操作不熟

解决方案: 
	
	- 首先检查图片是否能从表单传过来,`file = request.FILES.get('img_url', None)`,打印一下file,如果为None,就去检查一下添加页的方法是否为`post`,加没加`{ %  c s r f _ t o k e n  % }`和`enctype="multipart/form-data"`,js就是让图片在页面上显示出来的,都已经显示出来了,就别浪费时间再去测了  
	- 如果打印file结果不为None,就是视图函数的问题,就不用管HTML页面了,表单是跳到addbook函数,就从这个函数开始检查,检查到图片上传部分打印filename,结果为false说明是imgupload函数里的问题  
	- 上面已经检查过能否接收到图片,所以可以直接进入try里,检查路径是否正确,在服务器里文件夹是否存在,文件名是否正确,文件是否写入成功,到这里就可以发现错误了
	
总结: 文件上传的逻辑是:用户在表单中上传 -> 写入服务器中的静态文件夹中 -> 上传到数据库


### 模型创建多对一关系时报错说你在添加一个不允许为空的字段

原因: 先创建了学生表,又创建班级表,想在班级表里创建一个多对一关系,而班级id不能为空,所以只能设置默认值,或者退出来修改

解决方案: 退出来,把这些模型都注释,运行(相当于把这些表都删了),再取消注释运行

### data写成date不报错

原因:没有及时运行,及时发现错误,浪费了大量时间

解决方案:写一点运行一点,发现错误及时改,别等到最后一起运行,也别想着过一会就能发现自己的问题,能错就说明之前的逻辑还没通,要不一下就能发现出错误

### 分页unsupported operand type(s) for -: 'str' and 'int'

原因: 模板引擎自动解析,HTML注释也没有作用,相当于调了showpage函数,但是没有参数传过来

解决方案: 删除或者使用模板引擎语法注释
```
<!-- 使用自定义分页优化标签 -->
{ % comment % }
	{ % showpage data.paginator.num_pages request % }
{ % endcomment % }
```

### 扒花钱的网站(所见即所得)
1. 右键查看框架源代码,全选复制  
2. 新建一个文件夹,在文件夹里新建一个index.html文件,粘贴  
3. 查看所有js和css的链接,`ctrl+s`全保存下来  
4. 把index.html文件里的链接改成本地的  
5. 执行index.html插件所有功能,F12点Network有缺失的文件,去原网站执行一下,点Network,缺啥右键保存啥  
6. 打开所有css和js代码,搜索新保存下来的文件名,替换成本地文件  
7. 再运行就成了  

### 一堆静态文件404

原因: settings.py中debug=False,改完代码必须手动重启,而且静态文件路径有问题

解决方案: debug=True,修改后自动重启,全部都走路由

