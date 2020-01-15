---  
layout: post  
title: "JetBrains公司软件版本控制"  
date: 2019-11-16 10:26:40  
category: 'notes'  
tags:  
- 工具  
- Git  
---  
* content  
{:toc}  

JetBrains公司软件版本控制












# Git
### 修改设置
1. File -> Settings -> Version Control -> Git -> 配置Git路径`E:\software\Git\bin\git.exe`

2. File -> Settings -> Version Control -> GitHub -> 配置GitHub用户`caoyang529_7@163.com`

### 克隆Git仓库
1. 在GitHub上新建Git仓库

2. VSC -> Checkout from Version Control -> Git -> 粘贴Git仓库地址，选择保存路径

### 使用Git
1. 新建项目或者把要推上去的内容复制到本地文件夹中来

2. 追踪：右键库名 -> Git -> add

3. 提交：右键库名 -> Git -> commit directory -> 输入标记信息 -> 确认commit

4. 推：右键库名 -> Git -> Reposity -> push


### 文件名颜色所代表的含义
1. 绿色，已经加入版本控制暂未提交； 

2. 红色，未加入版本控制； 

3. 蓝色，加入版本控制，已提交，有改动； 

4. 白色，加入版本控制，已提交，无改动； 

5. 灰色：版本控制已忽略文件。