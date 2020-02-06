---
layout: post
title: "vue-cli搭配django快速开发及使用"
date: 2020-01-31 18:26:40
category: 'notes'
tags:
- Python
- Django
- Vue
---
* content
{:toc}










# P11. 必要的环境、软件安装配置
1. 安装node.js  
2. 安装编辑器pycharm和webstorm  
3. 安装谷歌浏览器  
4. npm换源  
> npm config set registry https://registry.npm.taobao.org  
> npm config get registry  
> npm install -g vue-cli  

# P22. 脚手架创建 、使用webstorm打开浏览了解具体内容
1. 创建脚手架  
> vue init webpack vueproject  
> 项目名称,项目描述,作者等4个回车  
> 只安装vue-router,其他全是n  
> 使用npm来安装,y  

 运行项目  
> cd vueproject  
> npm run dev  

# P33. 路由、来看看前端是如何路由的
### src里目录结构  
1. assets:静态文件  
2. component:放组件的  
3. router:路由  
4. App.ve:页面入口文件  
5. main.js:程序入口文件，加载各种公共组件  
	
### 创建路由  
1. 新建一个组件User.vue  

	```js
	<template>
		<div id="user">
			{ { page_info } }
		</div>
	</template>
	<script>
		export default {
			name: "User",
			data(){
				return {
					page_info: "this User page"
				}
			}
		}
	</script>
	<style scoped>
	</style>
	```

2. 在router/index.js中配置User路由  

	```js
	import Vue from 'vue'
	import Router from 'vue-router'
	import HelloWorld from '@/components/HelloWorld'
	import User from '@/components/User'
	
	Vue.use(Router)
	
	export default new Router({
	  routes: [
	    {
	      path: '/',
	      name: 'HelloWorld',
	      component: HelloWorld
	    },
	    {
	      path: '/user',
	      name: 'User',
	      component: User,
	    }
	  ]
	})
	```
	
3. 在App.vue中应用路由`/`和`/user`  

	```js
	<template>
	  <div id="app">
	    <img src="./assets/logo.png"><br />
	    <router-link to="/">Root</router-link>
	    <router-link to="/user">User</router-link>
	    <hr />
	    <router-view/>
	  </div>
	</template>
	
	<script>
	export default {
	  name: 'App'
	}
	</script>
	
	<style>
	#app {
	  font-family: 'Avenir', Helvetica, Arial, sans-serif;
	  -webkit-font-smoothing: antialiased;
	  -moz-osx-font-smoothing: grayscale;
	  text-align: center;
	  color: #2c3e50;
	  margin-top: 60px;
	}
	</style>
	```


# P44. 发送请求前的准备工作, 搭建django运行环境
### 创建django项目
1. 用pycharm直接创建django项目webproject,应用mysite  
2. 初始化数据库`python manage.py migrate`

### 修改settings.py
1. 允许所有主机访问`ALLOWED_HOSTS = ['*']`  
2. 注释掉`'django.middleware.csrf.CsrfViewMiddleware',`  
3. 语言改成中文`LANGUAGE_CODE = 'zh-Hans'`  
4. 时区改为上海`TIME_ZONE = 'Asia/Shanghai'`  
5. `USE_TZ = False`
6. 运行项目`python manage.py runserver`  
7. 静态文件改为前后端分离的`STATIC_URL = '/api/static/'`  

### 配置URL路由
1. 总路由  

	```python
	from django.contrib import admin
	from django.urls import path, include

	urlpatterns = [
		path('admin/', admin.site.urls),
		path('api/', include("mysite.urls"))
	]
	```

2. 子路由  

	```python
	from django.urls import path
	from mysite import views

	urlpatterns = [
		path("test/", views.test)
	]
	```

3. 视图函数  

	```python
	from django.http import JsonResponse

	def test(request):
		return JsonResponse({"status": 0, "message": "this is message"})
	```

4. 在浏览器中访问`http://127.0.0.1:8000/api/test/`

# P55. 初探django 跨域代理 并使用axios请求django数据
1. 安装axios`npm install axios --save`  
2. 在main.js中注册axios  

	```js
	import Vue from 'vue'
	import App from './App'
	import router from './router'
	import axios from 'axios'

	Vue.use(axios);
	Vue.config.productionTip = false
	Vue.prototype.$axios = axios

	/* eslint-disable no-new */
	new Vue({
	  el: '#app',
	  router,
	  components: { App },
	  template: '<App/>'
	})
	```

3. 在User.vue中接收后端传过来的数据  

	```js
	<template>
		<div id="user">
			{ { page_info } }
		</div>
	</template>
	<script>
		export default {
			name: "User",
			data(){
				return {
					page_info: "this User page"
				}
			},
	    created() {
	      this.$axios.get("/api/test/")
	        .then(response => {
	          console.log(response.data)
	        })
	    }
		}
	</script>
	<style scoped>
	</style>
	```

4. 解决跨域问题,修改config/index.js  

	```js
	proxyTable: {
	  '/api': {
	    target: 'http://127.0.0.1:8000/api/', //接口域名
	    changeOrigin: true, //是否跨域
	    pathRewrite: {
	      '^/api':'' ,//需要rewrite重写的
	    }
	  }
	},
	```

5. 访问http://localhost:8080/#/user就能接到数据了,但是还不能显示出来

# P66. 从数据库取数据给vue渲染表格
1. 修改User.vue把后端传过来的数据显示出来  

	```js
	<template>
		<div id="user">
			{ { page_info } }
	    <br />
	    { { django_message } }
		</div>
	</template>
	<script>
		export default {
			name: "User",
			data(){
				return {
					page_info: "this User page",
	        django_message: ""
				}
			},
	    created() {
	      this.$axios.get("/api/test/")
	        .then(response => {
	          this.django_message = response.data.message
	        })
	    }
		}
	</script>
	<style scoped>
	</style>
	```

2. 在models.py中创建Stu表  

	```python
	from django.db import models

	# Create your models here.
	class Stu(models.Model):
		id = models.IntegerField(primary_key=True,auto_created=True)
		name = models.CharField(max_length=200)
	```

3. 生成迁移文件`python manage.py makemigrations`  
4. 执行迁移文件`python manage.py migrate`  
5. 在models.py中注册Stu表  

	```python
	from django.contrib import admin
	from . import models

	# Register your models here.
	admin.site.register(models.Stu)
	```

6. 创建超级管理员`python manage.py createsuperuser`,用户名`caoyang`,密码`Mm23456`  
7. 运行项目,访问`127.0.0.1:8000/admin/login`  
8. 往学生表中添加几个用户  
9. 在views.py中返回表中数据  

	```python
	from django.http import JsonResponse
	from .models import Stu

	# Create your views here.
	def test(request):
		return JsonResponse({"status": 0, "message": "this is django_message"})

	def ret_user(request):
		if request.method == "GET":
			db = Stu.objects.all()
			db = [i.name for i in db]
			return JsonResponse({"status":0,"data":db})
		else:
			return JsonResponse({"status":1,"message":"you need GET method"})
	```

10. 配置子路由`path("user/",views.ret_user)`  
11. 访问`http://127.0.0.1:8000/api/user/`就能返回数据了  
12. 修改前端界面User.vue  

	```js
	<template>
		<div id="user">
			{ { page_info } }
	    <br />
	    { { django_message } }
	    <br />
	    <table>
	      <tr>
	        <th>user</th>
	      </tr>
	      <tr v-for="user in user_list" :key='user'>
	        <td>{ { user } }</td>
	      </tr>
	    </table>
		</div>
	</template>
	<script>
		export default {
			name: "User",
			data(){
				return {
					page_info: "this User page",
	        django_message: "",
	        user_list: [],
				}
			},
	    created() {
	      this.$axios.get("/api/test/")
	        .then(response => {
	          this.django_message = response.data.message
	        });
	      this.$axios.get("/api/user/")
	        .then(response => {
	          this.user_list = response.data.data
	        })
	    }
		}
	</script>
	<style scoped>
	</style>
	```

13. 访问`http://localhost:8080/#/user`即可接受到数据了

# P77. django序列化json数据方便vue识别
1. 在views.py中导入`from django.core import serializers`序列化的模块,可以将queryset转化为json  
2. 修改ret_user视图函数,访问`http://127.0.0.1:8000/api/user/`  

	```python
	def ret_user(request):
		if request.method == "GET":
			json = serializers.serialize("json",Stu.objects.all())
			return JsonResponse({"status":0,"data":json})
		else:
			return JsonResponse({"status":1,"message":"you need GET method"})
	```

3. 修改前端界面User.vue,访问`http://localhost:8080/#/user`  

	```js
	<template>
		<div id="user">
			{ { page_info } }
	    <br />
	    { { django_message } }
	    <br />
	    <table>
	      <tr>
	        <th>id</th>
	        <th>user</th>
	      </tr>
	      <tr v-for="user in user_list" :key='user'>
	        <td>{ { user.pk } }</td>
	        <td>{ { user.fields.name } }</td>
	      </tr>
	    </table>
		</div>
	</template>
	<script>
		export default {
			name: "User",
			data(){
				return {
					page_info: "this User page",
	        django_message: "",
	        user_list: [],
				}
			},
	    created() {
	      this.$axios.get("/api/test/")
	        .then(response => {
	          this.django_message = response.data.message
	        });
	      this.$axios.get("/api/user/")
	        .then(response => {
	          this.user_list = JSON.parse(response.data.data)
	        })
	    }
		}
	</script>
	<style scoped>
	</style>
	
	```