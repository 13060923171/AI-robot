# !/usr/bin/env python
# coding=utf-8

# 尝试手写minist数据集识别；利用keras框架搭建简单的神经网络并生成模型保存；

import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.optimizers import SGD,RMSprop # 优化器

# 导入数据集，由于mnist被人玩烂了，所以直接就把训练集和测试集给分好了。
# 所以这个入门就是注重搭建神经网络
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# print(x_train.shape) # (60000, 28, 28) 训练图片的特征矩阵
# print(y_train.shape) # (60000,) 训练图片的标签矩阵
# print(y_train[0]) # 第一张图片为5
# plt.imshow(x_train[0])
# plt.show()

# 搭建神经网络要求将特征矩阵的数据处理为浮点型方便之后的梯度运算；
#
x_train = x_train.reshape((-1,28,28,1)).astype('float')/255
x_test = x_test.reshape((-1, 28,28,1)).astype('float')/255
# print(x_train.shape)  # (60000, 784) 6万张训练图
# print(x_test.shape)  # (10000, 784) 1万张测试图
# print(x_train[0]) # 1维数组
# print(x_train[0].shape) #
# 将标签进行one-hot编码，可利用keras提供的方法
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
# print(y_train.shape) # (60000, 10)
# print(y_train[0]) # [0. 0. 0. 0. 0. 1. 0. 0. 0. 0.] 表示5

# 搭建神经网络，搭积木
model = Sequential()
model.add(Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D(2, 2))
model.add(Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Flatten())
model.add(Dense(84, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.summary()

model.compile(optimizer=RMSprop(lr=0.001),loss=keras.losses.categorical_crossentropy,metrics=['accuracy'])

model.fit(x_train,y_train,epochs=5)

test_loss,test_accurary = model.evaluate(x_test,y_test)
print('测试集损失：',test_loss,'测试集预测得分：',test_accurary)

print('训练结束！')