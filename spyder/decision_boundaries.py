# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:49:26 2019

@author: Karsten
"""

from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression(solver='liblinear')
svm = SVC(gamma='auto')
gaussian = GaussianNB()

# Sample Data

blob_X, blob_y = datasets.make_blobs(n_samples=300, n_features=3, centers=[[2, 2, 0],[-2, -2, 0]],
                                     cluster_std=[2, 2], random_state=42)

circle_X, circle_y = datasets.make_circles(n_samples=100, noise=0.1, factor=0.6)

rng = np.random.RandomState(9)
xor_X = rng.randn(300, 3)
xor_y = np.array(np.logical_xor(xor_X[:, 0] > 0, xor_X[:, 1] > 0),  dtype=int)

def fit_and_plot(X, y, clf, ax, value=0.0, width=0.5):
    ax.set_axis_off()
    clf.fit(X,y)
    # Plot training sample with feature 3 = 0.0 +/- 0.5
    plot_decision_regions(X, y, clf=clf,
                          filler_feature_values={2: value},
                          filler_feature_ranges={2: width},
                          #markers='s^oxv<>',
                          #colors='green,blue,limegreen,gray,cyan',
                          legend=0, ax=ax)

def plot_clfs(X, y, clf1, clf2, axarr):
    fit_and_plot(X, y, clf1, axarr[0])
    fit_and_plot(X, y, clf2, axarr[1])
    
fig, axarr = plt.subplots(1, 2, figsize=(10,5))
fit_and_plot(blob_X, blob_y, logmodel, axarr[0])
fit_and_plot(xor_X, xor_y, svm, axarr[1])
#plot_clfs(blob_X, blob_y, logmodel, svm, axarr)
plt.show()

fig.savefig('c:/tmp/decision_boundaries.png')

