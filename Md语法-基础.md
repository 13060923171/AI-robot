---
title: Md语法-基础
date: 2020-03-29 09:15:55
tags: 
- Markdown
- study
categories: 
- 博客建设
cover: /img/鬼刀冰心.jpg
---

# 关于blog的建设 #
目前只用于写学习笔记。这里就先总结一下Markdown的语法，方便以后
使用。

首先是段落标题使用#来区分，一共6个等级


    # 1 #
	## 2 ##
	### 3 ###
	#### 4 ####
但是我这里的编辑器只能快捷键调用四个，不过也够用了。

## 关于换行有两种方式： ##  
 
	1 要么两个空格接回车  
	2 要么直接空出一个段落

## 关于字体： ##  
	*斜体用*  
	**粗体两个***  
	___粗斜体用3*或者3____

    *斜体文本*
	_斜体文本_
	**粗体文本**
	__粗体文本__
	***粗斜体文本***
	___粗斜体文本___

## 分割线：多种方法创建 ##

    ***

	* * *
	
	*****
	
	- - -
	
	----------

***
* *  *
* ************
---
----------

## 删除线： 


	RUNOOB.COM
	GOOGLE.COM
	~~BAIDU.COM~~
~~BAIDU.COM~~

虽然我的编辑器不能显示出效果，好像是因为被前端认为不合法就没有渲染出来。

## 下划线： ##
	<u>带下划线文本</u>
<u>带下划线文本</u>
## 脚注 ##
    [^要注明的文本]
	创建脚注格式类似这样 [^RUNOOB]。
	[^RUNOOB]: 菜鸟教程 -- 学的不仅是技术，更是梦想！！！
创建脚注格式类似这样 [^RUNOOB]。  
[^RUNOOB]: 菜鸟教程 -- 学的不仅是技术，更是梦想！！！

## 列表 ##
无序列表使用*-+作为标记  

* 1  
- 2  
+ 3  

有序列表：加数字即可

1. 第一项
2. 第二项
3. 第三项

列表嵌套：在字列表前加个缩进tab即可

1. 第一项
	* 第一嵌套
	* 第二嵌套
2. 第二项
	1. 第二有序嵌套
	2. 第二。。。

## 区块： ##
> 使用> 后接一个空格

    > 区块应用
	> > 当然也可以嵌套
	> > > 第二层嵌套
> 区块应用
> > 当然也可以嵌套
> > > 第二层嵌套

列表和区块可以随意搭配哦。

* 第一项
	> 就像这样
2. 第二项
	> en
## 代码 ##
我这里一般使用编辑器的快捷键ctrl+k  
它的语法是用`反引号将代码包起来
## url链接 ##
    [链接名称](链接地址)

	或者
	
	<链接地址>
[百度](https://www.baidu.com)

<https://www.baidu.com>

高级链接：即在md最底部设置链接变量，这样有链接变量的地方就
都可以进行链接，如：

    这个链接用 1 作为网址变量 [Google][1]
	这个链接用 runoob 作为网址变量 [Runoob][runoob]
	然后在文档的结尾为变量赋值（网址）

	  [1]: http://www.google.com/
	  [runoob]: http://www.runoob.com/

这个链接用 1 作为网址变量 [Google][1]  
这个链接用 runoob 作为网址变量 [Runoob][runoob]  
然后在文档的结尾为变量赋值（网址）  

  [1]: http://www.google.com/
  [runoob]: http://www.runoob.com/
## 图片 ##
    ![alt 属性文本](图片地址)
	![alt 属性文本](图片地址 "可选标题")
![alt 爬虫1](http://static.runoob.com/images/runoob-logo.png)

![alt 本地图片](https://s1.ax1x.com/2020/04/01/G8Y3Jx.md.jpg)

![alt 爬虫2](https://raw.githubusercontent.com/HardyDragon/HardyDragon.github.io/master/img/%E9%AC%BC%E5%88%80%E5%86%B0%E5%BF%83.jpg "123")

这里的图片url好像称为图床，要有网址才行，我这一打算使用github的仓库作为图床来推送要图片的blog；

也可以使用变量名来链接图片：

    这个链接用 1 作为网址变量 [RUNOOB][1].
	然后在文档的结尾为变量赋值（网址）
	[1]: http://static.runoob.com/images/runoob-logo.png

这个链接用 1 作为网址变量 [RUNOOB][1].
然后在文档的结尾为变量赋值（网址）
[1]: http://static.runoob.com/images/runoob-logo.png

如果想设置图片的高宽可以使用img标签的width，height

    <img src ="https://raw.githubusercontent.com/HardyDragon/HardyDragon.github.io/master/img/%E9%AC%BC%E5%88%80%E5%86%B0%E5%BF%83.jpg" width="50%">

<img src ="https://raw.githubusercontent.com/HardyDragon/HardyDragon.github.io/master/img/%E9%AC%BC%E5%88%80%E5%86%B0%E5%BF%83.jpg" width="50%">


## 表格 ##
    |  表头   | 表头  |
	|  ----  | ----  |
	| 单元格  | 单元格 |
	| 单元格  | 单元格 |

|  表头   | 表头  |  
|  ----  | ----  |  
| 单元格  | 单元格 |  
| 单元格  | 单元格 |  

    我们可以设置表格的对齐方式：
	| 左对齐 | 右对齐 | 居中对齐 |
	| :-----| ----: | :----: |
	| 单元格 | 单元格 | 单元格 |
	| 单元格 | 单元格 | 单元格 |

| 左对齐 | 右对齐 | 居中对齐 |  
| :-----| ----: | :----: |  
| 单元格 | 单元格 | 单元格 |  
| 单元格 | 单元格 | 单元格 |  

这里的表格在编辑器显示不了。

<img src="https://www.runoob.com/wp-content/uploads/2019/03/87DE9D5C-44FB-4693-8735-194D3779EC3E.jpg" width="50%">

## 高级技巧 ##
支持html元素

    目前支持的 HTML 元素有：<kbd> <b> <i> <em> <sup> <sub> <br>等
	使用 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd> 重启电脑
使用 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd> 重启电脑
### 转义符号\ ###
    \   反斜线
	`   反引号
	*   星号
	_   下划线
	{}  花括号
	[]  方括号
	()  小括号
	#   井字号
	+   加号
	-   减号
	.   英文句点
	!   感叹号

还能写数学公式。。

总结:基本的Markdown语法就这些了。其实也就几个比较常用，其他的都还好。