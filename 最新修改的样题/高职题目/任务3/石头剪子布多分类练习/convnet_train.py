import os
import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import load_img
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout
from keras.utils import to_categorical
from keras.models import Sequential

'''
    这样训练出来的模型准确度虽然很高，但是验证集的准确度却低， vali loss 很高，上网查了一下是过拟合，主要
    问题出现在数据是顺序的，过于集中，我用了数据集分隔0.2，导致了数据集样本不均匀。需要添加shuffle 来打乱样本和标签
    在数据处理前先打乱，后面训练的时候再将shuffle 设置True；注意打乱是样本和标签一起打乱；不然样本和标签会不匹配
    需要用到seed。
'''

# paper:0;  rock:1;  scissors:2
x_train = []
y_train = []
for subfloder in os.listdir('rps/'):
    for picname in os.listdir('rps/' + subfloder):
        img = np.array(load_img('rps/' + subfloder + '/' + picname, target_size=(100, 100, 3)))
        img = img / 255.0
        x_train.append(img)
        if 'paper' in picname:
            y_train.append(0)
        if 'rock' in picname:
            y_train.append(1)
        if 'scissors' in picname:
            y_train.append(2)

x_train = np.array(x_train)
y_train = to_categorical(y_train, 3)
y_train = np.array(y_train)

# 新加 为了消除过拟合：打乱训练集的样本和标签；
np.random.seed(200)
np.random.shuffle(x_train)
np.random.seed(200)
np.random.shuffle(y_train)

# print(x_train.shape)
# print(y_train.shape)
# print(y_train[:10])
# for i in range(10):
#     plt.subplot(2, 5, i+1)
#     plt.title(np.argmax(y_train[i]))
#     plt.imshow(x_train[i])
# plt.show()


model = Sequential()
model.add(Conv2D(input_shape=(100, 100, 3), filters=16, kernel_size=3))
model.add(Conv2D(filters=16, activation='relu', kernel_size=3, strides=2))
model.add(MaxPool2D(pool_size=2))

model.add(Conv2D(filters=32, activation='relu', kernel_size=3))
model.add(MaxPool2D(pool_size=2))

model.add(Conv2D(filters=64, activation='relu', kernel_size=3))
model.add(MaxPool2D(pool_size=2))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(3, activation='softmax'))

model.summary()

model.compile(
    optimizer=keras.optimizers.Adam(lr=0.0001),
    loss=keras.losses.categorical_crossentropy,
    metrics=['accuracy']
)

model.fit(x=x_train, y=y_train, epochs=10, verbose=2, validation_split=0.2, batch_size=32, shuffle=True)


model.save('rps_shuffle_model_cnn.h5')
