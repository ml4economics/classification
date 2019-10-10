# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:22:41 2019

@author: Karsten
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

import warnings
warnings.filterwarnings('ignore')

data_sets = ('bank-10percent', 'bank-full', 'bank-balanced')

bank = pd.read_csv('../data/' + data_sets[1] + '.csv')

label_col = 'y'
label = bank[label_col]
features = bank.drop(columns=['y'])

label_encoded = pd.get_dummies(label, drop_first = True)
features_encoded = pd.get_dummies(features, drop_first = True)

X_train, X_test, y_train, y_test = train_test_split(features_encoded, label_encoded, test_size = 0.2, random_state = 167)

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


logmodel = LogisticRegression() 
logmodel.fit(X_train,y_train)

"""
print("Coefficients :")
keys = features_encoded.keys()
for i in range(0,keys.size):
    print("{} : {:.4f}".format(keys[i],logmodel.coef_[0][i]))
""" 

logpred = logmodel.predict(X_test)

logtrainpred = logmodel.predict(X_train)

print(confusion_matrix(y_train, logtrainpred))
print(round(accuracy_score(y_train, logtrainpred),2)*100)
print(confusion_matrix(y_test, logpred))
print(round(accuracy_score(y_test, logpred),2)*100)

