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
from collections import Counter
t0 = time()
clf = svm.SVC(C=10000.0, kernel='rbf')# due to task in course experiments \
# were with C 10.0, 100.0, 1000.0, 10000.0. Best accuracy with lowered dataset (to 1% of initial dataset
#  was with C = 10000.0, \
#при этом разделяющая гиперплоскость стала более сложной, чем при С=1.0, а скорость обучения
# увеличилась почти в 2 раза
#features_train = features_train[:int(len(features_train)/100)]#эта и следующая строка снижают выборку
#labels_train = labels_train[:int(len(labels_train)/100)]#остается 1% выборки, остальное-не учитывается
clf.fit(features_train, labels_train)
predictions = clf.predict(features_test)
accuracy = accuracy_score(labels_test, predictions)
print(accuracy)
print("training time:", round(time()-t0, 3), "s")
answer= []
answer1 = predictions[10]
answer2 = predictions[26]
answer3 = predictions[50]
answer.append(answer1)
answer.append(answer2)
answer.append(answer3)
number_of_answers_chris_class = Counter(predictions)
print(answer)
print(number_of_answers_chris_class)
#########################################################