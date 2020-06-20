# 代码 机器人 树莓派 深度学习 opencv 
---
**创建时间 2020/5/13 18:19:43** 

----

![https://i.ibb.co/PjYqCF5/image.jpg](https://i.ibb.co/PjYqCF5/image.jpg)
# 第一次提交
第一个项目是利用face++的API来实现人脸识别，识别人脸的表情，年龄，等等；然后根据返回的响应解析成json数据提取里面的参数来对机器人进行控制；2020/5/13 19:58:53 

# 第二次提交
目前更新到AIoT物联网应用，里面项目代码已经整理好了，看看以后会不会补充，主要是有些代码在确认后自己又看了一遍，把一些缩进和注释调了一下，不得不说有些代码真的一看就是错的。。 2020/5/13 21:23:29 

# 第三次提交
更新完了机器人视觉的教程项目，后面设计到了使用CNN神经网络，使用sklearn库，每一个项目代码都挺多的，所以后面一些大项目我只是单纯的将他们有的仓库整合在一起。至于如何使用还是得看网站上面的教程。2020/5/14 17:35:44 

# 第四次提交
更新了一些机器人的传感器语音基础部分，将竞赛样题转化为md，有个md语法基础。有个在线图床可以使用[在线图床](https://imgbb.com/);

# 查看机器人RestfulAPI接口
在每台机器人上，可以通过在浏览器上输入 [http://127.0.0.1:9090/v1/ui](http://127.0.0.1:9090/v1/ui) 来获得本地的RESTful API, 也可以通过获得机器人的IP地址从远程连接上 http://机器人IP:9090/v1/ui。意思是可以在同一网络下使用PC查看API文档。

同时还可以访问在线文档 [Yanshee RESTful API](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_cn/1.0.0#/) 来学习已经支持到的API。

VNC登录时默认账号`pi raspberry`

# 切换成test_branch 分支提交
    git checkout test_branch
    在测试分支使用gitee的WebIDE修改readme,然后在本地pull测试；

# CNN卷积神经网络（多用于图像识别）

CNN是前反馈神经网络（输入、隐藏、输出）的一类，但是多了卷积和池化两层，且一般池化跟在卷积后边；为了训练效果好一般有多层的卷积和池化；本次提交更新了使用keras对mnist手写数字数据集进行训练来识别手写数字的图像，保存了对应的model和权重(h5文件)；但是使用python3，有些库的函数还是很不一样的。

```python
值得一提的是python2文件的前缀在linux系统下要记得：
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```

2020/5/18 19:00:55 

# 5.19日提交

训练模型的大概流程应该是使用Ubuntu的python2环境（keras、tensorflow）去训练model模型，然后部署到机器人的py3环境使用，这次提交发现了一个py3和py2不同的参数导致的问题。在识别手写数字哪里，训练好的模型以上传准确度98%左右，然后就是使用模型验证的代码一份是py3的，一份是py2的。有一些修改的地方都已标注了。2020/5/19 21:32:11 

# 5.20提交

这次提交了人脸训练的训练代码和验证代码以及训练后95%准确的模型文件，使用123.gif作为训练集；然后我使用windows的python3环境训练的，除了读入路径要修改其他没什么大问题。检测模型只需要注释掉训练部分代码查看模型准确率即可；在Ubuntu环境下使用py2来验证的时候记得加上文件前缀# usr/bin/env python .....来让系统识别为py文件，路径也要修改为当前目录来读取模型。读取模型仍旧需要数据集来判断。

![https://i.ibb.co/FgQtBzY/image.png](https://i.ibb.co/FgQtBzY/image.png)

## Ubuntu/win/树莓派？py环境配置

​	

```python
安装虚拟环境3.5/3.6,3.7的话可能有些函数参数不一样
conda create -n py36 python=3.6
conda install tensorflow-gpu==1.8
conda install keras-gpu==2.2
# 最好版本指定好！不然也可能报错。以上安装的是GPU训练的。装在Ubuntu/win
# 树莓派/机器人应该就只装默认CPU的keras和tensorflow，去掉-gpu后缀安装即可
# 如果需要其他库同样conda install 安装即可。例如PIL/matplotlib
# 其中PIL是python2的库。如果安装时不想输入y，可以最后加个 -y
# py3里面使用PIL需要安装pillow，导入正常py2写法
```

# 5.21更新keras猫狗识别

发现用keras来处理数据和设计网络训练模型相对简单，更新了视觉部分的keras训练猫狗识别，但是原来的训练集太少，模型准确度只有0.6左右，看能不能把tensorflow的猫狗识别数据集拿过来训练。而且keras生成的h5模型文件方便保存和部署。

​		 








