#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keras.models import load_model
from keras.preprocessing.image import load_img
import numpy as np
import matplotlib.pyplot as plt

model = load_model('mnist_model_5.h5')
image = load_img('mnist_test.png', color_mode='grayscale', target_size=(28, 28, 1))
image = np.array(image) / 255
plt.imshow(image)
image = image.reshape(-1, 28, 28, 1)
result = model.predict_classes(image)
plt.title(result[0])
plt.show()
