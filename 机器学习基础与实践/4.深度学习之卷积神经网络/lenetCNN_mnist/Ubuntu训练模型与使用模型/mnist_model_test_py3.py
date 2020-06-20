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

img = image.load_img(path="mnist_test.png", color_mode="grayscale", target_size=(28,28,1))
img = image.img_to_array(img)

test_img = img.reshape((-1,28,28,1)) # 需要修改此处维度！ test_img = img.reshape((1,784)) 原本的代码
img_class = model.predict_classes(test_img) 
classname = img_class[0]
print('预测结果维度：',classname.shape)
print("Class:",classname)
# print("Class:",img_class)


img = img.reshape((28,28))
plt.imshow(img)
plt.title(classname)
# plt.title(img_class)

plt.show()
