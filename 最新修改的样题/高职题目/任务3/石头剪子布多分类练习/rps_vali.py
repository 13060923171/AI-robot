import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import load_img
from keras.models import load_model
from keras.utils import to_categorical

# paper:0;  rock:1;  scissors:2
img = np.array(load_img('test/testpaper01-00.png', target_size=(100, 100, 3)))
img = img / 255
plt.imshow(img)

img = img.reshape((1, 100, 100, 3))
model = load_model('rps_shuffle_model_cnn_99.h5')
result = model.predict_classes(img)
lable = ['paper', 'rock', 'scissors']
print(result[0])
plt.title(lable[result[0]])
plt.show()

# img_label = to_categorical([0], 3)  # 测试标签。
# print(img_label)
# test_loss, test_accuracy = model.evaluate(img, img_label)
# print("test_loss:", test_loss, "    test_accuracy:", test_accuracy)
