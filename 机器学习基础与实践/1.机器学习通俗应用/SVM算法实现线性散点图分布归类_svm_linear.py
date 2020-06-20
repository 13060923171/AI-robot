#!/usr/bin/env python

# -*- coding: utf-8 -*-

 

import numpy as np

import matplotlib.pyplot as plt

from sklearn import svm

 

# 保证随机数据的唯一性

np.random.seed(8)

 

# 准备线性可分数据集

array = np.random.randn(20,2)

X = np.r_[array-[3,3],array+[3,3]]

y = [0]*20+[1]*20

#print X

#print y

 

# 建立svm模型

clf = svm.SVC(kernel='linear')

clf.fit(X,y)

 

# 分析数据

x1_min, x1_max = X[:,0].min(), X[:,0].max(),

x2_min, x2_max = X[:,1].min(), X[:,1].max(),

xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))

# 得到向量w  : w_0x_1+w_1x_2+b=0

w = clf.coef_[0]

# 加1后才可绘制 -1 的等高线 [-1,0,1] + 1 = [0,1,2]

f = w[0]*xx1 + w[1]*xx2 + clf.intercept_[0]+1

# 绘制分隔超平面、H1、H2

plt.contour(xx1, xx2, f, [1], colors = 'r')

plt.contour(xx1, xx2, f, [0,2], colors = 'g')

 

# 绘制数据集散点图

plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.Paired)

# 绘制支持向量点

plt.scatter(clf.support_vectors_[:,0],clf.support_vectors_[:,1],color='k')

plt.show()