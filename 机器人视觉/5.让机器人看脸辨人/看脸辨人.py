#encoding=utf-8

############################################################

#################Author: Xuyang Jie#########################

 

#################Date: 26/03/2018###########################

############################################################

# 这个是使用PCA/LDA来实现识别人脸后判断人脸是谁。由于网站代码复制过来后格式十分乱，缩进一看就有许多问题。 
# 未修改，这个关于看脸辨人的感觉比较难理解，需要用到numpy的相关知识，后面需要再补充 

import cv2

import os

import time

import sys

import numpy as np

 

class picture(object):

    def __init__(self,path,name):

        self.name = name

        self.path = path

        self.train_vec,self.test_vec, self.train_name, self.test_name, self.train_gray, self.test_gray = self.load_image()

 

    # image to one raw vector

    def mat2vector(self,mat):

       rows,cols = mat.shape

       img_vec = np.zeros((1, rows* cols))

       img_vec = np.reshape(mat,(1, rows * cols))

       return img_vec

 

    # pre-process

    def pre_process(self,path):

       image = cv2.imread(path)

       grayimage = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

       return grayimage

 

    # load images

    def load_image(self):

       integer = int(sys.argv[3])

       file_index = 0

       train_gray_image_list = []

       test_gray_image_list = []

       whole = np.random.permutation(range(10))

 

       if self.name == 'fisherface':

           height = 20

           width = 20

       else:

           height = 112

           width = 92

 

       train_vec = np.zeros((40 * integer, height * width))

       test_vec = np.zeros((40 * (10 - integer), height * width))

       train_face_name = []

       test_face_name = []

       for parent, dirnames, filenames in os.walk(self.path):

           for dirname in dirnames:

              train_list = np.random.randint(10, size = 1)

              counter = 0

              for index in range(10):

                  gray_img = self.pre_process(self.path + dirname + '/' + str(whole[index]) + '.pgm')

                  if self.name == 'fisherface':

                     gray_img = cv2.resize(gray_img,(height,width))

                  vec = self.mat2vector(gray_img)

                  #time.sleep(1)

                  if index < integer:

                     train_vec[file_index * integer + index,:] = vec

                     train_face_name.append(dirname)

                     train_gray_image_list.append(gray_img)

                  else:

                     test_vec[file_index * (10 - integer) + (index - integer)] = vec

                     test_face_name.append(dirname)

                     test_gray_image_list.append(gray_img)

              file_index += 1

 

       return train_vec,test_vec, train_face_name, test_face_name, train_gray_image_list,test_gray_image_list

    # PCA

    def eigenface(self,k):

       data = np.float32(np.mat(self.train_vec))

       height,width = self.train_vec.shape

       data_mean = np.mean(self.train_vec,axis = 0)

       data_mean_all = np.tile(data_mean,(height,1))

       data_diff = self.train_vec - data_mean_all

       S = data_diff.dot(data_diff.T)

       eig_val, eig_vec = np.linalg.eig(S)

       sortindics = np.argsort(eig_val)

       i = len(eig_vec) - 1

       new_eig_vec = np.zeros((eig_vec.shape))

       for index in sortindics:

           new_eig_vec[i] = eig_vec[index]

           i -= 1

       new_eig_vec = new_eig_vec[:,0:k]

       new_eig_vec = data_diff.T.dot(new_eig_vec)

       #for i in range(k):

           #L = np.linalg.norm(new_eig_vec[:,i])

           #new_eig_vec[:,i] /= L

       return new_eig_vec, data_mean

 

    #   LDA

    def fisherface(self,k):

       rows,cols = self.train_vec.shape

       Sw = np.zeros((cols,cols))

       Sb = np.zeros((cols,cols))

       total_train = rows

       each_p = int(sys.argv[3])

       index = 0

 

       if each_p == 1:

           return self.train_vec

 

       # Calculate Sw

       while(index < total_train):

           mean_class = np.mean(self.train_vec[index:index + each_p], axis = 0).reshape((cols ,1))

           sw = np.zeros((cols,cols))

           for each_sample in range(index,index + each_p):

              diff = self.train_vec[each_sample].reshape((cols,1))

              sw += diff.dot(diff.T)

           Sw += sw

           index += each_p

       index = 0

 

       # All_mean

       mean_all = np.mean(self.train_vec,axis = 0).reshape((cols,1))

 

       # Caluculate Sb

       while(index < total_train):

           mean_class = np.mean(self.train_vec[index:index + each_p],axis = 0)

           diff = mean_class - mean_all

           Sb += ((each_p) * diff.dot(diff.T))

           index += each_p

 

       # Caluculate eig_Val and eig_vec

       eig_val,eig_vec = np.linalg.eig(np.linalg.inv(Sw).dot(Sb))

       sortIndices = np.argsort(eig_val)

       i = len(eig_vec) - 1

       new_eig_vec = np.zeros((eig_vec.shape))

       for index in sortIndices:

           new_eig_vec[i] = eig_vec[index]

           i -= 1

       new_eig_vec = new_eig_vec[0:k,:]

       W = new_eig_vec.T

       return W

 

    def show(self,test_index,train_index,predict):

       res = cv2.resize(self.test_gray[test_index],(320,240),interpolation = cv2.INTER_CUBIC)

       cv2.putText(res,'Predict:' + self.train_name[predict] + ' Actual:' + self.test_name[test_index],(30,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),1)

       cv2.imshow('Test Face',res)

       #res2 = cv2.resize(data_test_new[test_index],(320,240),interpolation = cv2.INTER_CUBIC)

       #cv2.imshow('PCA down to ' + str(down_to_dim) + '(Test)',res2)

       res3 = cv2.resize(self.train_gray[predict],(320,240),interpolation = cv2.INTER_CUBIC)

    cv2.putText(res3,self.train_name[predict],(50,80),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,255),3)

       cv2.imshow('Train Face',res3)

       #res4 = cv2.resize(train_d[distindexlist[0]].T,(320,240),interpolation = cv2.INTER_CUBIC)

       #cv2.imshow('PCA down to '+ str(down_to_dim) + '(Train)',res4)

       cv2.waitKey(0)

 

    def predict(self):

       true_num = 0

       num_train = self.train_vec.shape[0]

       num_test = self.test_vec.shape[0]

 

       if self.name == 'eigenface':

           new_eig_vec, data_mean = self.eigenface(int(sys.argv[2]))

           diff = self.train_vec - np.tile(data_mean,(num_train,1))

           train_data = diff.dot(new_eig_vec)

           diff = self.test_vec - np.tile(data_mean,(num_test,1))

           test_data = diff.dot(new_eig_vec)

           for i in range(num_test):

              testface = test_data[i,:]

              diffMat = train_data - np.tile(testface,(num_train,1))

              sqDiffMat = diffMat ** 2

              sqDistance = sqDiffMat.sum(axis = 1)

              sortDistIndicies = sqDistance.argsort()

              indexMin = sortDistIndicies[0]

              if self.train_name[indexMin] == self.test_name[i]:

                  true_num += 1

              self.show(test_index = i,train_index = indexMin,predict = indexMin)

       else:

           if int(sys.argv[3]) == 1:

              train_data = self.train_vec

              test_data = self.test_vec

           else:

              W = self.fisherface(int(sys.argv[2]))

              train_data = self.train_vec.dot(W)

              test_data = self.test_vec.dot(W)

           for test_index in range(test_data.shape[0]):

              distlist = []

              for train_index in range(train_data.shape[0]):

                  dist = np.linalg.norm((test_data[test_index] - train_data[train_index]))

                  distlist.append(dist)

              distindexlist = np.argsort(distlist)

              #print distindexlist

              if(self.train_name[distindexlist[0]] == self.test_name[test_index]):

                  true_num += 1

              self.show(test_index = test_index,train_index = train_index,predict = distindexlist[0])

       accuracy = float(true_num)/num_test

       print 'The classify accuracy is %.2f%%' % (accuracy * 100)

 

 

 

 

if __name__=='__main__':

    face = picture(str(sys.argv[4]),str(sys.argv[1]))

    print 'Predicting'

    start = time.time()

    face.predict()

    print 'Finish predicting\tUse time:%.2f' % (time.time() - start)