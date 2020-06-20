# usr/bin/env python
# -*-coding:utf-8-*-
'''Test  MNIST dataset Model.
'''

from __future__ import print_function

import keras
from keras.models import Sequential
import matplotlib.pyplot as plt
from keras.preprocessing import image
from keras.models import load_model

model = Sequential()
model=load_model("mnist_mode.h5")
model.summary()

# 这里最大坑就是py3和py2的load_img 的 读取方式参数不同，py3的是可以有多种读取，但是py2就只有是否灰度读取，也就是一个是传入字符串，py2传入grayscale的布尔值
# 这是我查看help函数才发现的。。太坑了，还安装了什么pillow 库,以为是matplotlib的问题一开始。
img = image.load_img(path="mnist_test.png",grayscale=True, target_size=(28,28,1))
img = image.img_to_array(img)

test_img = img.reshape((-1,28,28,1)) # 这里维度也要改 （1,784）-》；表示转换为【-1表示不知道转换后有多少行】28行*28列的3维数组，最后的1表示1个通道即灰度图
img_class = model.predict_classes(test_img)
classname = img_class[0]
print("Class:",classname)

img = img.reshape((28,28))
plt.imshow(img)
plt.title(classname)
plt.show()
