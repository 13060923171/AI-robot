#!/usr/bin/env python

# -*- coding: utf-8 -*-

 

import numpy as np

import matplotlib.pyplot as plt

 

# 训练

def standRegres(xArr,yArr): 

    m,n = np.shape(xArr)

    # 加第一列设为1，为计算截距

    xMat = np.mat(np.ones((m, n+1)))

    x = np.mat(xArr)

    xMat[:,1:n+1] = x[:,0:n];

    yMat = np.mat(yArr).T 

    #print xMat

    #print yMat

    xTx = xMat.T*xMat

    if np.linalg.det(xTx) == 0.0:

        #行列式的值为0，无逆矩阵

        print("This matrix is sigular, cannot do inverse")

        return 

    ws = xTx.I*(xMat.T*yMat) 

    return ws

 

# 预测

def predict(xArr, ws):

    m,n = np.shape(xArr)

    # 加第一列设为1, 为计算截距

    xMat = np.mat(np.ones((m, n+1)))

    x = np.mat(xArr)

    xMat[:,1:n+1] = x[:,0:n];

    return xMat*ws

 

if __name__ == '__main__':

    x = [[1], [2], [3], [4]]

    y = [4.1, 5.9, 8.1, 10.1]

    ws = standRegres(x,y)

    print(ws)

    print(predict([[5]], ws))

 

    # 画图

    plt.scatter(x, y, s=20)

    yHat = predict(x, ws)

    plt.plot(x, yHat, linewidth=2.0, color='red')

    plt.show()