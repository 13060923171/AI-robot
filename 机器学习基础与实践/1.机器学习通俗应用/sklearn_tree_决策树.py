#!/usr/bin/env python

 

from sklearn import tree

 

feature=[[178,1],[155,0],[177,0],[165,0],[169,1],[160,0]]

label = ['male','female','male','female','male','female']

 

clf = tree.DecisionTreeClassifier()

clf = clf.fit(feature,label)

 

test = [[158,0],[170,1]]

result = clf.predict(test)

print result