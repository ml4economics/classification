# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:38:05 2019

@author: Karsten
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

bank = pd.read_csv('../data/bank-10percent.csv')
bank.info()

df = bank
name='age'
display_name='Age'
series = df[name]

# range
min_value = series.min()
max_value = series.max()
print('Min age: ', min_value)
print('Max age: ', max_value)
print('Null Values: ', series.isnull().any())

fig, ax = plt.subplots()
fig.set_size_inches(20, 8)
sns.countplot(x = 'age', data = bank)
ax.set_xlabel('Age', fontsize=15)
ax.set_ylabel('Count', fontsize=15)
ax.set_title('Age Count Distribution', fontsize=15)
sns.despine()

from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
jobs = labelencoder_X.fit_transform(bank['job']) 