# 色调（H：hue）：用角度度量，取值范围为0°～360°，从红色开始按逆时针方向计算，红色为0°，绿色为120°,蓝色为240°。它们的补色是：黄色为60°，青色为180°,品红为300°!

![HSV](https://s1.ax1x.com/2020/06/04/t0LyqS.jpg)

![HSV的共同之处](https://s1.ax1x.com/2020/06/04/t0OCZD.png)





# RGB转化到HSV的算法：

max=max**(**R**,**G**,**B**)**

min=min**(**R**,**G**,**B**)**

V=max**(**R**,**G**,**B**)**

S=**(**max-min**)**/max

**if**R = max**,**H =**(**G-B**)**/**(**max-min**)*** 60

**if**G = max**,**H = 120+**(**B-R**)**/**(**max-min**)*** 60

**if**B = max**,**H = 240 +**(**R-G**)**/**(**max-min**)*** 60

**if**H < 0**,**H = H+ 360

(**个人感觉这个有点难理解，最好的方法，其实是把比赛用的那几个常用的颜色的一些H值记好即可，下面的SV基本都是一样的，这些值可以有误差，误差在3-5之间也是可以的，大概大概记住这个值的范围即可**)

![HSV的主要函数](https://s1.ax1x.com/2020/06/04/tBwUGq.png)





# 比赛要用到OpenCV函数解析：

# 1.最基本的函数

```python
#使程序暂停，等待用户触发一个按键操作
cv2.waitKey()
#读取图像，filename，读取的图片文件名。flags，读取标志位。
cv2.imread(filename,flags=None)
#写入图像,filename，写入的文件名。img，待写入的图像。params，特定格式下保存的参数编码，一般情况下为None。
cv2.imwrite(filename,img,params=None)
#创建一个图像窗口，winname，窗口名称。mat，图像矩阵。
cv2.imshow(winname,mat)
#画圆
cv2.Circle（）
#画矩形
cv2.Rectangle（）
#调用XML文件
cv2.CascadeClassifier（）
#用来关闭所有窗口并释放窗口相关的内存空间
cv2.destroyAllWindows()
```

# 2.和模糊有关的函数

```python
#对图像进行高斯模糊,sigmaX，X方向上的方差，一般设为0让系统自动计算。
cv2.GaussianBlur(src,ksize,sigmaX,dst=None,sigmaY=None,borderType=None)
#对图像进行中值模糊
cv2.medianBlur(src,ksize,dst=None)
#erode腐蚀 第二参数是卷积核大小，这里不用核；腐蚀次数
cv2.erode(mask, None, iterations=2)
#dilate膨胀 同上
cv2.dilate(mask, None, iterations=2)
#对图像进行算术平均值模糊,ksize，卷积核的大小。dst，若填入dst，则将图像写入到dst矩阵。
cv2.blur(src,ksize,dst=None,anchor=None,borderType=None)
```

# 3.和小球有关的函数

```python
#contourArea轮廓面积来寻找最大的轮廓确定圆位置
cv2.contourArea
#利用最大轮廓的最小外接圆确认圆心和半径
cv2.minEnclosingCircle()
#从二值图像中寻找轮廓
cv2.findContours()
#RETR_EXTERNAL 如果你选择这种模式的话，只会返回最外边的的轮廓，所有的子轮廓都会被忽略掉
#cv2.CHAIN_APPROX_SIMPLE 会压缩轮廓，将轮廓上冗余点去掉，比如说四边形就会只储存四个角点。
#返回值的第二个是 轮廓列表
cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```

# 4.颜色的相关函数

```python
#将一幅图像从一个色彩空间转换到另一个色彩空间
cv2.cvtColor(src,code,dst=None,dstCn=None)
#生成指定颜色的遮掩层，传入图像，设置最小最大阈值
cv2.inRange(hsv, lower_red, upper_red)
```

# [全部函数的解析大全](https://blog.csdn.net/u013050589/article/details/25188915)

# [OpenCV常用操作函数大全！](https://blog.csdn.net/Vici__/article/details/100714822?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-23.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-23.nonecase#cv2.GaussianBlur)

里面的笔记都整理的很好，我们除了要掌握最基本的函数的含义和应用还要了解一些均值模糊的概念
