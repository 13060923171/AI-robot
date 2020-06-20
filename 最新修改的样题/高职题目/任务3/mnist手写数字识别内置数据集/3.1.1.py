#!/usr/bin/env python
# -*- coding: utf-8 -*-

import keras
from keras.datasets.mnist import load_data
from keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = load_data()
x_train = x_train / 255
x_train = x_train.reshape(-1, 28, 28, 1)
print(x_train.shape)
y_train = to_categorical(y_train, 10)

from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten

model = Sequential()
model.add(Conv2D(
    input_shape=(28, 28, 1),
    filters=32,
    kernel_size=2,
    strides=2,
    activation='relu'
))
model.add(MaxPool2D(
    pool_size=2,
    strides=2
))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.summary()

model.compile(
    optimizer=keras.optimizers.SGD(lr=0.02),
    loss=keras.losses.categorical_crossentropy,
    metrics=['accuracy']
)

model.fit(
    x=x_train,
    y=y_train,
    epochs=5,
    validation_split=0.2,
    batch_size=64,
)

model.save('mnist_model_5.h5')
