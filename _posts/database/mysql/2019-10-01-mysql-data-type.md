---
title: "MySQL的基础数据类型"  
tags: database mysql   
---

<script>
window.location.href='https://blog.csdn.net/bt517840374/article/details/101828585';
</script>


一 介绍
存储引擎决定了表的类型，而表内存放的数据也要有不同的类型，每种数据类型都有自己的宽度，但宽度是可选的
详细参考：

菜鸟教程
mysql文档
mysql常用数据类型概览

数字
整型：tinyinit int bigint
小数：float double
字符串
char(10):简单粗暴，浪费空间，存区速度快
varchar：精准，节省空间，存区速度慢
sql优化：创建表时，定长的类型往前放，变长的往后放
> 255个字符，超了就把文件路径存放到数据库中。
时间类型
datatime
枚举类型与集合类型
enum set