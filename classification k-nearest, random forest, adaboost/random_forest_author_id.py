#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.
    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
sys.path.append("D://PycharmProjects//untitled//cкрипты Python//udacity_intro_to_machine_learning//tools")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

t0 = time()

clf = RandomForestClassifier()
#features_train = features_train[:int(len(features_train)/100)]#эта и следующая строка снижают выборку
#labels_train = labels_train[:int(len(labels_train)/100)]#остается 1% выборки, остальное-не учитывается
clf = clf.fit(features_train, labels_train)
predicted_values = clf.predict(features_test)
accuracy = accuracy_score(labels_test, predicted_values)
number_of_features = len(features_train[0])
print(accuracy)
print("training time:", round(time()-t0, 3), "s")



#########################################################
### your code goes here ###


#########################################################
