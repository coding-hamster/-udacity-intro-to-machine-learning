#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "D://PycharmProjects//untitled//cкрипты Python//udacity_intro_to_machine_learning//text learning//your_word_data.pkl"
authors_file = "D://PycharmProjects//untitled//cкрипты Python//udacity_intro_to_machine_learning//text learning//your_email_authors.pkl"
word_data = pickle.load( open(words_file, "rb"))
authors = pickle.load( open(authors_file, "rb") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import model_selection
features_train, features_test, labels_train, labels_test = model_selection.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]



### your code goes here
from sklearn import tree
from sklearn.metrics import accuracy_score
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
predicted_values = clf.predict(features_test)
accuracy = accuracy_score(labels_test, predicted_values)
print(accuracy)
'''importances = clf.feature_importances_
importance_list = []
for i in importances:
    if i > 0.2:
        importance_list.append(i)
print(importance_list)'''

problemWordIndices = []

importances = clf.feature_importances_
for index in range(len(importances)):
    if importances[index] > 0.2:
        print ("index:", index)
        problemWordIndices.append(index)
        print ("importance:", importances[index])

for index in problemWordIndices:
    print ("problem word:", vectorizer.get_feature_names()[index])