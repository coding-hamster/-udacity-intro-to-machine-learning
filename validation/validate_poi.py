#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
from sklearn import tree
from sklearn.metrics import accuracy_score
from time import time
from sklearn.model_selection import train_test_split


sys.path.append( r"D:\PycharmProjects\untitled\cкрипты Python\udacity_intro_to_machine_learning\tools" )
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]
t0 = time()

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
clf = tree.DecisionTreeClassifier()
clf.fit(features, labels)
predicted_values = clf.predict(features)
accuracy = accuracy_score(labels, features)
print(accuracy)
print("training time:", round(time()-t0, 3), "s")
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)
### it's all yours from here forward!

clf1 = tree.DecisionTreeClassifier()
clf1.fit(features_train, labels_train)
predicted_values1 = clf.predict(features_test)
accuracy1 = accuracy_score(labels_test, predicted_values1)
number_of_features = len(features_train[0])
print(accuracy1)
print("training time:", round(time()-t0, 3), "s")
print(number_of_features)

