#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import time
from sklearn.neighbors import KNeighborsClassifier

#This is a sample to classify 1 mouse 2 keyboard 3 cup

def load_datasets(data_path):
    feature = np.ndarray(shape=(0,3))
    label = np.ndarray(shape=(0,1))

    #print feature.shape
    df = pd.read_table(data_path,delimiter=',',na_values='?',header=None)

    fpiece = df.ix[:, :2]
    feature = np.concatenate((feature,fpiece))

    data = df.ix[:,3].values
    lpiece = pd.DataFrame(data)
    label = np.concatenate((label,lpiece))
    return feature,label

if __name__ == '__main__':
    data_path = 'dataset.txt'
    x_train,y_train = load_datasets(data_path)
    #print x_train
    #print y_train
    print('start training knn')
    knn = KNeighborsClassifier().fit(x_train,y_train)
    print('training done')
    print('请输入待测物体的长、宽、高:a,b,c;长为a厘米,宽为b厘米,高为c厘米.')
    x_test = []
    X = raw_input('长,宽,高：')
    X = X.strip('').split(',')
    x_test.append(int(X[0]))
    x_test.append(int(X[1]))
    x_test.append(int(X[2]))
    #x_test1 = [[43,16,2]]
    answer_knn = int(knn.predict([x_test]))
    #answer_knn1 = int(knn.predict(x_test1))
    print('prediction done:')
    result_name = {1:'鼠标',2:'键盘',3:'水杯'}
    #print result_name[answer_knn1]
    print(result_name[answer_knn])