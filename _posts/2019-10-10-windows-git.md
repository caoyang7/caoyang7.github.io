---
layout: post
title: "Windows下git"
date: 2019-10-10 13:26:40

tags:
- 工具
- Git
---
* content
{:toc}

Windows下如何使用git管理github
















### 一、下载gitbash
github是远程的一个仓库，gitbash是win下一个工具，我们打代码都是在本地打代码，然后通过gitbash把自己代码传到github上面去。  
[gitbash下载地址:https://git-scm.com/downloads](https://git-scm.com/downloads)  

### 二、打开刚刚安装好的gitbash
#### 1. 配置一下gitbash和github的通信协议  
先输入ssh-keygen -t rsa -C “邮箱地址” 然后一直按回车回车回车回车...箭头指向的邮箱填写我当时填的是和github上写的邮箱一致。

```
caoya@DESKTOP-EUP3RV2 MINGW64 ~
$ ssh-keygen -t rsa -C "caoyang529_7@163.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/caoya/.ssh/id_rsa):
Created directory '/c/Users/caoya/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/caoya/.ssh/id_rsa.
Your public key has been saved in /c/Users/caoya/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:BNVKOKxAnWxDNXhUVY0nqfYmbkkggvsunF/9RfS52yQ caoyang529_7@163.com
The key's randomart image is:
+---[RSA 3072]----+
| ..+.*=+oo...+   |
|  . B =o. . + o  |
|   + + o.. ..o   |
|  . o ..o o. . . |
|   . . .So .. o  |
|  .    .  o.o  . |
| . o  . .o +. E .|
|  + ..   .+.   = |
|   +o    ..   . .|
+----[SHA256]-----+
 
```

#### 2. 根据上图提示信息打开文件目录
/c/Users/caoya/.ssh/id_rsa，找到那个文件。用文本方式打开.pub文件。直接全选复制。  
![/c/Users/caoya/.ssh/id_rsa](https://img-blog.csdn.net/20170319144714095?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbHVvc2Fvc2Fv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  

#### 3. 打开github自己的主页Settings->SSH->newSSHkey  

#### 4. 验证设置
输入命令：`ssh –T git@github.com`，问你yes or no，就输入yes，回车完事。

```
caoya@DESKTOP-EUP3RV2 MINGW64 ~
$ ssh -T git@github.com
The authenticity of host 'github.com (13.229.188.59)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com,13.229.188.59' (RSA) to the list of known hosts.
Hi caoyang7/caoyang7.github.io! You've successfully authenticated, but GitHub does not provide shell access.
```

#### 5. 配置gitbash的用户名和邮箱  
git config –global user.name “用户名”  
git config –global user.email “邮箱”  
用户名邮箱，用你github上的用户名和邮箱。  
配置成功，你会发现gitbash命令行哪里多了个master字样：

```
caoya@DESKTOP-EUP3RV2 MINGW64 ~
$ git config --global user.name "caoyang7"
caoya@DESKTOP-EUP3RV2 MINGW64 ~
$ git config --global user.email "caoyang529_7@163.com"
```

#### 6. 大功告成  
此时我们的git就配置成功了,该克隆克隆,该推推,其他就是Git的东西啦!  

