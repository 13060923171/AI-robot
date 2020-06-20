import os
import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import load_img
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout
from keras.models import Sequential

x_train = []
y_train = []
for subfloder in os.listdir('train/'):
    for picname in os.listdir('train/' + subfloder):
        img = np.array(load_img('train/' + subfloder + '/' + picname, target_size=(100, 100, 3)))
        img = img / 255.0
        x_train.append(img)
        if 'cat' in picname:
            y_train.append(0)  # cat-0
        if 'dog' in picname:
            y_train.append(1)  # dog-1

x_train = np.array(x_train)
y_train = np.array(y_train)
# print(y_train[0:1000])
# print(y_train[1000:])
# print(y_train.shape)
np.random.seed(200)
np.random.shuffle(x_train)
np.random.seed(200)
np.random.shuffle(y_train)

# for i in range(10):
#     plt.subplot(2, 5, i+1)
#     plt.title((y_train[i]))
#     plt.imshow(x_train[i])
# plt.show()

model = Sequential()
model.add(Conv2D(16, 3, input_shape=(100, 100, 3)))
model.add(Conv2D(16, 3, activation='relu'))
model.add(MaxPool2D(2, 2))

model.add(Conv2D(32, 3, activation='relu', padding='same'))
model.add(MaxPool2D(2, 2))

model.add(Conv2D(64, 3, activation='relu', strides=2, padding='same'))
model.add(MaxPool2D(2, 2))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(1, activation='sigmoid'))

model.summary()

model.compile(
    optimizer=keras.optimizers.Adam(lr=0.0002),
    loss=keras.losses.binary_crossentropy,
    metrics=['accuracy']
)

model.fit(x=x_train, y=y_train, validation_split=0.2, epochs=10, verbose=2, batch_size=32)
model.save('6_18cat_dog_model.h5')
