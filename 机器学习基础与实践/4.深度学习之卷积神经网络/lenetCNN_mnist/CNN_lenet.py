# !/usr/bin/env python
# coding=utf-8
# 读取minist数据集识别手写图片
import cv2
import keras
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from keras.models import Sequential
import matplotlib.pyplot as plt
import numpy as np
# from sklearn.preprocessing import label

mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# print(y_train[0]) # 5
# plt.imshow(x_train[0]) # 将二维矩阵显示成图片
# plt.show()
print('hi')

# img = cv2.imread('cat.jpg')
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# plt.figure(figsize=(4,3),facecolor='r')
# plt.axis('off')
# plt.imshow(img)
# plt.show()
# cv2.imshow('cat',img)
# cv2.waitKey()
# x_train = x_train.reshape(x_train.shape+(1,))
# print(x_train.shape) # (60000, 28, 28)
# reshape 的第一个参数 -1 表示转换为最多个 28*28*1维度的矩阵；也可以指定为60000, 28, 28 , 1
x_train = x_train.reshape(-1, 28, 28, 1)
# print(x_train.shape) # (60000, 28, 28 , 1)
# print(x_train[0])
x_test = x_test.reshape(-1, 28, 28, 1)
# a = np.squeeze(x_train[0])
# plt.imshow(a)
# plt.show()

x_train = x_train / 255.0  # 限定范围-1——1
x_test = x_test / 255.0
# ctrl+alt+L 格式化代码
# print(y_train[0]) # 5
y_train = keras.utils.to_categorical(y_train)  # 将标签转换为矩阵,也称one-hot处理
# print(y_train[0]) # [0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
# print(y_test[0]) # 7
y_test = keras.utils.to_categorical(y_test)
# print(y_test[0])  # [0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]

lenet = Sequential()
lenet.add(Conv2D(6, kernel_size=3, strides=1, padding='same', input_shape=(28, 28, 1)))
lenet.add(MaxPooling2D(pool_size=2, strides=2))
lenet.add(Conv2D(16, kernel_size=5, strides=1))
lenet.add(MaxPooling2D(pool_size=2, strides=2))
lenet.add(Flatten()) # 变为一维向量
lenet.add(Dense(120))
lenet.add(Dense(84))
lenet.add(Dense(10, activation='softmax'))

lenet.summary()
# 优化器一般sgd，损失函数交叉验证，指标使用['accuracy']
lenet.compile(optimizer='sgd', loss=keras.losses.categorical_crossentropy,metrics=['accuracy'])

records = lenet.fit(x_train, y_train, epochs=10, validation_split=0.2)
y_pred = np.argmax(lenet.predict(x_test), axis=1)  # 按行比较大小，返回最大值索引即标签中1的索引矩阵
# print('预测准确率：{}'.format(sum(y_pred == y_test) / len(y_test))) # 取平均值
# 绘制结果
plt.plot(records.history['loss'],label='train loss')
plt.plot(records.history['val_loss'],label='test loss')
plt.ylabel('binary cross-entropy')
plt.xlabel('epochs')
plt.legend()
plt.show()

# lenet.save('mnist_lenet_keras_20.h5')
