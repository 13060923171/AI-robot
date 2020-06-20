import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
from keras.preprocessing.image import load_img

img = np.array(load_img('test/27.jpg', target_size=(100, 100, 3)))
plt.imshow(img)

img = img / 255
img = img.reshape(1, 100, 100, 3)
print(img.shape)
model = load_model('6_18cat_dog_model_a80_v70.h5')
result = model.predict_classes(img)
print(result)
plt.axis('off')
plt.title('cat' if result[0][0] == 0 else 'dog')
plt.show()
