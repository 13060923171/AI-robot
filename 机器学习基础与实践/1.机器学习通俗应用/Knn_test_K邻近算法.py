#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 需要自己准备一个数据集txt文本，详情看官网对应教程
import pandas as pd
import numpy as np
import time
from sklearn.neighbors import KNeighborsClassifier

# 前三列是长宽高的值单位厘米，最后一列是标签值：1代表鼠标、2代表键盘、3代表水杯
#This is a sample to classify 1 mouse 2 keyboard 3 cup

def load_datasets(data_path):
    feature = np.ndarray(shape=(0,3))
    label = np.ndarray(shape=(0,1))

    #print feature.shape
    df = pd.read_table(data_path, delimiter=',', na_values='?', header=None) # 读取，逗号分隔的数据，没有行首设置为None，将NA替换为？

    fpiece = df.ix[:, :2] # ix 传入两个列表 第一个列表表示要提取元素的行号，第二个为列号，即全部行的前2列（0,1）为长、宽？理论应该是3列？
    feature = np.concatenate((feature, fpiece)) # 拼接数组

    data = df.ix[:, 3].values # 取每行的第4列即类别标签的值
    lpiece = pd.DataFrame(data) # 根据现有分类构建表格结构
    label = np.concatenate((label, lpiece)) # 数组拼接，即标签数组只存储了最后1列的分类信息。特征数组存储了前3列。
    return feature, label

if __name__ == '__main__':
    data_path = 'dataset.txt'
    x_train, y_train = load_datasets(data_path)
    #print x_train
    #print y_train
    print ('start training knn')
    knn = KNeighborsClassifier().fit(x_train, y_train) # 传入参数
    print ('training done')
    print ("请输入待测物体的长、宽、高: a,b,c ; 长为 a 厘米, 宽为 b 厘米, 高为 c 厘米.")
    x_test = []
    X = raw_input('长,宽,高 : ')
    X = X.strip(' ').split(',')
    x_test.append(int(X[0]))
    x_test.append(int(X[1]))
    x_test.append(int(X[2]))
    #x_test1 = [[43, 16, 2 ]]
    answer_knn = int(knn.predict([x_test])) # 利用模型预测测试集
    #answer_knn1 = int(knn.predict(x_test1))
    print ('prediction done:')
    result_name = {1: '鼠标', 2: '键盘', 3:'水杯'}
    #print result_name[answer_knn1]
    print result_name[answer_knn] # 返回对应的索引123的值即名称