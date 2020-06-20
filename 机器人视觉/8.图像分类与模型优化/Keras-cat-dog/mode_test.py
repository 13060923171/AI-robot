'''Test a cat_dog Cnn net model.
'''

from __future__ import print_function

import keras
from keras.models import Sequential
import matplotlib.pyplot as plt
from keras.preprocessing import image
from keras.models import load_model


model = Sequential()
#load the model
model=load_model("cat_dog_model.h5")
model.summary()

img1 = image.load_img(path="./testmodel/dog7.jpg", target_size=(234,234,3))
img = image.img_to_array(img1)

img = img.astype('float32')
img /= 255
test_img = img.reshape((1,234,234,3))
preds = model.predict(test_img)
print (preds[0])
#predict the result
img_class = model.predict_classes(test_img)
classname = img_class[0]
print("Class:",classname)
if classname == 0:
    title = 'cat'
    print ("cat")
if classname == 1:
    title = 'dog'
    print ("dog") 
#show the picture
plt.imshow(img1)
plt.title(title)
plt.show()
