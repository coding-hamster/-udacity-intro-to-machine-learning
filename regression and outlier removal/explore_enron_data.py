#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import re
import pandas as pd

enron_data = pickle.load(open("D://PycharmProjects//untitled//cкрипты Python//udacity_intro_to_machine_learning//final_project//final_project_dataset.pkl", 'rb'))
list_of_names = enron_data.keys()
number_of_people = len(list_of_names)

number = 0
for i in enron_data:
    d = enron_data.get(i)
    c = len(d)
    number += c
number_of_features = number/number_of_people
poi_counter = 0
for i in enron_data:
    if enron_data[i]['poi'] == 1:
        poi_counter += 1
poi_names = open(r'D:\PycharmProjects\untitled\cкрипты Python\udacity_intro_to_machine_learning\final_project\poi_names.txt', 'r')
poi_names_uncovered = poi_names.read()
poi_names_uncovered_list = poi_names_uncovered.split(sep='(')
list1 = []
for i in poi_names_uncovered_list:
    list1.append(i)
counter_names = len(list1)
stock_value = enron_data["PRENTICE JAMES"]["total_stock_value"]
print("Number of people:" + str(number_of_people))
print("Number of features:" + str(number_of_features))
print("Number of persons of interest:"+str(poi_counter))
print("Number of persons of interest by name:" + str(poi_names_uncovered_list))
print(counter_names)
#print(stock_value)
number_of_features1 = enron_data.values()
print(number_of_features1)
print(stock_value)
messages = enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print(messages)
stock_options = enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print(stock_options)
SKILLING = enron_data["SKILLING JEFFREY K"]["total_payments"]
LAY = enron_data["LAY KENNETH L"]["total_payments"]
FASTOW = enron_data["FASTOW ANDREW S"]["total_payments"]

print(SKILLING)
print(LAY)
print(FASTOW)
count = 0

for person in enron_data:
    if enron_data[person]['email_address'] != 'NaN':
        count += 1

print ("count of emails is " +str(count))

count1 = 0
for i in enron_data:
    if enron_data[i]['salary'] != 'NaN':
        count1 += 1

print("count of salary is "  + str(count1))

number_of_people = 0
number_of_nans = 0
for i in enron_data:
    number_of_people += 1
    if enron_data[i]['total_payments'] == 'NaN':
        number_of_nans += 1
percentage_of_nans = number_of_nans/number_of_people*100
print('nan in total payments:'+str(number_of_nans))
print(percentage_of_nans)

number_of_ppois = 0
number_of_nanspoi = 0
for i in enron_data:
    if enron_data[i]['poi'] == True:
        number_of_ppois += 1
        if enron_data[i]['total_payments'] == 'NaN':
            number_of_nanspoi += 1
percentage_of_nanspoi = number_of_nanspoi/number_of_ppois*100
print(percentage_of_nanspoi)