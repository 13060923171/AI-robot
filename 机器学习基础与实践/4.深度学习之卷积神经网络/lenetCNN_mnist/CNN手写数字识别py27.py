#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入模块
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
# 读取MNIST数据
mnist = keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()
# 重构数据至4维（样本，像素X，像素Y，通道）
x_train=x_train.reshape(x_train.shape+(1,))
x_test=x_test.reshape(x_test.shape+(1,))
x_train, x_test = x_train/255.0, x_test/255.0
# 数据标签
label_train = keras.utils.to_categorical(y_train, 10)
label_test = keras.utils.to_categorical(y_test, 10)
# LeNet-5构筑
model = keras.Sequential([
    keras.layers.Conv2D(6, kernel_size=(3, 3), strides=(1, 1), activation='tanh', padding='valid'),
    keras.layers.AveragePooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'),
    keras.layers.Conv2D(16, kernel_size=(5, 5), strides=(1, 1), activation='tanh', padding='valid'),
    keras.layers.AveragePooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'),
    keras.layers.Flatten(),
    keras.layers.Dense(120, activation='tanh'),
    keras.layers.Dense(84, activation='tanh'),
    keras.layers.Dense(10, activation='softmax'),])
# 使用SGD编译模型
model.compile(loss=keras.losses.categorical_crossentropy, optimizer='SGD')
# 学习30个纪元（可依据CPU计算力调整），使用20%数据交叉验证 # 不该是20？
records = model.fit(x_train, label_train, epochs=20, validation_split=0.2)
# 预测
y_pred = np.argmax(model.predict(x_test), axis=1)
print("prediction accuracy: {}".format(sum(y_pred==y_test)/len(y_test)))
# 绘制结果
plt.plot(records.history['loss'],label='training set loss')
plt.plot(records.history['val_loss'],label='validation set loss')
plt.ylabel('categorical cross-entropy'); plt.xlabel('epoch')
plt.legend()