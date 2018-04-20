#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.
    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

sys.path.append("D://PycharmProjects//untitled//cкрипты Python//udacity_intro_to_machine_learning//tools")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.metrics import accuracy_score
from sklearn import svm
t0 = time()
clf = svm.SVC(kernel='linear')
#features_train = features_train[:int(len(features_train)/100)]#эта и следующая строка снижают выборку
#labels_train = labels_train[:int(len(labels_train)/100)]#остается 1% выборки, остальное-не учитывается
clf.fit(features_train, labels_train)
predicted_labels = clf.predict(features_test)
accuracy = accuracy_score(labels_test, predicted_labels)
print(accuracy)
print("training time:", round(time()-t0, 3), "s")
#########################################################