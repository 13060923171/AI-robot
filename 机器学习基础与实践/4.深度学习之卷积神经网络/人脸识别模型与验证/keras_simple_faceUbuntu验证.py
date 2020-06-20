# usr/bin/env python
# -*-coding:utf-8-*-

'''Train a simple convnet on the part olivetti faces dataset.
Run on CPU: python keras_simple_face.py
there is still a lot of margin for parameter tuning.
'''

from __future__ import print_function
from keras.utils import np_utils
from keras.optimizers import SGD
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.models import Sequential
from PIL import Image
import numpy
numpy.random.seed(1337)  # for reproducibility


# There are 40 different classes
nb_classes = 40
epochs = 40
batch_size = 40

# input image dimensions
img_rows, img_cols = 57, 47
# number of convolutional filters to use
nb_filters1, nb_filters2 = 5, 10
# size of pooling area for max pooling
nb_pool = 2
# convolution kernel size
nb_conv = 3

def load_data(dataset_path):
    img = Image.open(dataset_path)
    img_ndarray = numpy.asarray(img, dtype='float64')/256
    #400pictures,size:57*47=2679
    faces = numpy.empty((400, 2679))
    for row in range(20):
        for column in range(20):
            faces[row*20+column] = numpy.ndarray.flatten(
                img_ndarray[row*57:(row+1)*57, column*47:(column+1)*47])
    label = numpy.empty(400)
    for i in range(40):
        label[i*10:i*10+10] = i
    label = label.astype(numpy.int)
    #train:320,valid:40,test:40
    train_data = numpy.empty((320, 2679))
    train_label = numpy.empty(320)
    valid_data = numpy.empty((40, 2679))
    valid_label = numpy.empty(40)
    test_data = numpy.empty((40, 2679))
    test_label = numpy.empty(40)

    for i in range(40):
        train_data[i*8:i*8+8] = faces[i*10:i*10+8]
        train_label[i*8:i*8+8] = label[i*10:i*10+8]
        valid_data[i] = faces[i*10+8]
        valid_label[i] = label[i*10+8]
        test_data[i] = faces[i*10+9]
        test_label[i] = label[i*10+9]
    rval = [(train_data, train_label), (valid_data, valid_label),
            (test_data, test_label)]
    return rval

def Net_model():
    model = Sequential()
    model.add(Conv2D(nb_filters1, (nb_conv, nb_conv),
                    padding="valid",
                    input_shape=(img_rows, img_cols, 1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))

    model.add(Conv2D(nb_filters2, (nb_conv, nb_conv)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(1000))  # Full connection
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy',
                    optimizer='rmsprop', metrics=['accuracy'])
    return model

def train_model(model, X_train, Y_train, X_val, Y_val):
    model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs,
            verbose=1, validation_data=(X_val, Y_val))
    model.save_weights('facemodel_weights.h5', overwrite=True)
    return model

def test_model(model, X, Y):
    model.load_weights('facemodel_weights.h5')
    score = model.evaluate(X, Y, verbose=0)
    print('Test score:', score[0])
    print('Test accuracy:', score[1])
    return score

if __name__ == '__main__':
    # img = Image.open("olivettifaces.gif") # 多个参数py读取mode
    # img = Image.open(r"E:\github远程仓库管理\python机器学习\simple_40_face\123.png") # win要加绝对路径r避免报错。吐了
    
    # print('读取成功！')
    # the data, shuffled and split between train and test sets
    (X_train, y_train), (X_val, y_val), (X_test,
                                        y_test) = load_data(r"123.gif")
    X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
    X_val = X_val.reshape(X_val.shape[0], img_rows, img_cols, 1)
    X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
    print('X_train shape:', X_train.shape)
    print(X_train.shape[0], 'train samples')
    print(X_val.shape[0], 'validate samples')
    print(X_test.shape[0], 'test samples')

    # convert class vectors to binary class matrices
    Y_train = np_utils.to_categorical(y_train, nb_classes)
    Y_val = np_utils.to_categorical(y_val, nb_classes)
    Y_test = np_utils.to_categorical(y_test, nb_classes)

    model = Net_model()
    # 验证训练集，只需打开模型就可以了。注意这里的模型名为facemodel_weights
    # train_model(model, X_train, Y_train, X_val, Y_val)
    # score = test_model(model, X_test, Y_test)

    model.load_weights(r"facemodel_weights.h5") # 同样报错就改成这样的绝对路径
    classes = model.predict_classes(X_test, verbose=0)
    test_accuracy = numpy.mean(numpy.equal(y_test, classes))
    print("accuarcy:", test_accuracy)
