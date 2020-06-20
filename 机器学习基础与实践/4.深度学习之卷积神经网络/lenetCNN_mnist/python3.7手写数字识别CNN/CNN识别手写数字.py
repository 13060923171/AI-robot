import numpy as np
import matplotlib.pyplot as plt
# plt.rcParams['figure.figsize']=(5,7) # 设置显示窗口大小
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense,Dropout,Activation,Flatten
from keras.utils import np_utils
from keras import backend as K
from keras.layers import Conv2D,MaxPooling2D # 图像卷积、池化

# print('OK')

nb_classes = 10 # 识别0-9 10个标签分类
img_rows,img_cols = 28,28 # 预处理时要转化图像为row行col列
# 下载数据集,分为训练集和测试集
# X shape (60,000 28x28), y shape (10,000, )
# X（总数据集）可理解为60000行数据，每一行是一张28 x 28 的灰度图片。
# 或者说该数据集有60000张图片，每个图片用28*28的矩阵表示
(X_train,y_train),(X_test,y_test) = mnist.load_data() 
# 查看训练样本图片
plt.figure(num='hello',figsize=(5,5)) # 对话框名，窗口大小，这个比较好记忆
'''
for i in range(6):
    plt.subplot(2,3,i+1) # 指定显示一共3行3列中的第几个,这里的行列积最好和图片个数一样，显示效果好点
    plt.imshow(X_train[i],cmap='gray',interpolation='none')
    plt.title('Class{0}'.format(y_train[i]))
    # plt.show() # 这样写会报错，因为它要显示的是整合在一个窗口的图像
plt.show()
'''
# 数据预处理
if K.image_data_format() == 'channels_first': #image_data_format返回默认的图像数据格式约定。通道优先？
    X_train = X_train.reshape(X_train.shape[0],1,img_rows,img_cols) # （n,1,28,28） 四维矩阵，先1表示通道要是灰度；简单说就是矩阵中最小元素表示每个图片的像素点，方便当成节点处理
    X_test = X_test.reshape(X_test.shape[0],1,img_rows,img_cols)
    input_shape = (1,img_rows,img_cols)
else:
    X_train = X_train.reshape(X_train.shape[0],img_rows,img_cols,1) # (n,28,28,1)
    X_test = X_test.reshape(X_test.shape[0],img_rows,img_cols,1)
    input_shape = (img_rows,img_cols,1)


# print(X_train.shape) # (60000, 28, 28, 1) 训练集存储的维度，60000张图片以28*28矩阵灰度 一通道 channel 存储
# print(X_test.shape) # (10000, 28, 28, 1)
# print(input_shape) # (28, 28, 1) # 输入的数据维度为28*28的的三维数组，

# 样本数据标准化到0-1
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255 # 取整
X_test /= 255 # 取整

# print("训练集X矩阵维度：",X_train.shape) # (60000, 28, 28, 1)
# print("测试集/验证集X矩阵维度：",X_test.shape) # (10000, 28, 28, 1)
# print(y_train.shape) # (60000,) 一维矩阵

# 将标签Y处理成 binary matrix 二维矩阵
y_train = np_utils.to_categorical(y_train,nb_classes)
y_test = np_utils.to_categorical(y_test,nb_classes)

# print(y_train.shape) # (60000, 10) 10个分类

# 建立神经网络模型 
model = Sequential()
# 创建第一层（一般输入层没有激活函数，但是这里卷积直接当第一层可以有），卷积层（32个3*3的卷积核）
model.add(Conv2D(filters=32,kernel_size=(3,3),padding='valid',input_shape=input_shape)) # 当卷积当做第一层时需要指定input_shape元组
model.add(Activation('relu')) # 激活函数
# 创建第二层卷积
model.add(Conv2D(filters=32,kernel_size=(3,3)))
model.add(Activation('relu')) # 激活函数
# 第三层为池化层
model.add(MaxPooling2D(pool_size=(2,2)))
# 第四层，全连接层（普通层Dense）
model.add(Flatten())
model.add(Dense(128)) # 128输出维数
model.add(Activation('relu')) # ReLu:接受实数输入，将负值=0，正值不变输出;激活函数
model.add(Dense(nb_classes)) # 输出10个分类
model.add(Activation('softmax')) 
# 设置损失函数和优化器
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
# 开始训练模型
model.fit(X_train,y_train,batch_size=128,nb_epoch=15,verbose=1,validation_data=(X_test,y_test))
# 观察测试集的准确率
score = model.evaluate(X_test,y_test,verbose=1)
print('验证集对训练模型测试得分：',score[0])
print('accuracy精准度：',score[1])
# 保存模型为json/h5格式，方便以后调用
model_structure = model.to_json()

with open("model_digit.json", "w") as json_file:
    json_file.write(model_structure)
# serialize weights to HDF5
model.save_weights("model_digit.h5")
print("权重保存在hdf5文件格式！")
print('生成json模型文件！')












