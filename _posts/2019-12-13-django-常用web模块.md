---    
layout: post    
title: "常用web模块"    
date: 2019-12-13 18:26:40    
category: 'notes'    
tags:    
- Python    
- Django    
---    
* content    
{:toc}    
    
7. 常用web模块















# 7.1 静态文件配置

> 项目中的CSS、图片、js都是静态文件

## 一,在settings 文件中定义静态内容

```
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

## 二,在项目根目录下创建static目录，再创建当前应用名称的目录

```
mysite/static/myapp/
```

## 三,在模板中可以使用硬编码

```
/static/my_app/myexample.jpg
```

## 四,在模板中可以使用static编码

```
{ % load static from staticfiles % }
<img src="{ % static "my_app/myexample.jpg" % }" alt="My image"/>
```


# 7.2 Csrf(防跨站攻击)

> CSRF（Cross-site request forgery）跨站请求伪造，也被称为“One Click Attack”或者Session Riding，通常缩写为CSRF或者XSRF，是一种对网站的恶意利用。尽管听起来像跨站脚本XSS，但它与XSS非常不同，XSS利用站点内的信任用户，而CSRF则通过伪装来自受信任用户的请求来利用受信任的网站。与XSS攻击相比，CSRF攻击往往不大流行（因此对其进行防范的资源也相当稀少）和难以防范，所以被认为比XSS更具危险性
> 
> CSRF中间件和模板标签为防止跨站点请求伪造提供了易用的保护。
> 
> 当恶意网站包含链接，表单按钮或某些旨在在您的网站上执行某些操作的JavaScript时，会使用在浏览器中访问恶意网站的登录用户的凭据进行此类攻击。
> 
> 还介绍了一种相关攻击类型，即“登录CSRF”，攻击网站欺骗用户的浏览器，以便使用其他人的凭证登录到网站。






# 7.3 Ajax
# 7.4 状态保持(会话跟踪技术)
# 7.5 验证码
# 7.6 中间件
# 7.7 文件上传
# 7.8 密码管理
# 7.9 分页和优化
# 7.10 富文本编辑器
# 7.11 Django部署Apache
# 7.12 Redis缓存应用
# 7.13 Auth认证
# 7.14 admin后台管理



