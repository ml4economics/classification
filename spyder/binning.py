# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:57:07 2019

@author: Karsten
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from sklearn.preprocessing import KBinsDiscretizer
from sklearn.datasets import make_blobs

strategies = ['uniform', 'quantile', 'kmeans']
cmap = cm.get_cmap("Accent") #ListedColormap(['r', 'g', 'b', 'c'])

lower = 0
upper = 10
n_samples = 150
n_bins = 4
blob_centers = np.array([[1], [2], [6], [9]])

data = ['Gleichverteilte Werte', 
        '4 normalverteilte Gruppen mit Mitten {}'.format(blob_centers.ravel())]

# construct the datasets
random_state = 47
X_list = [
        
    # first data set is uniformly distributed
    np.random.RandomState(random_state).uniform(lower, upper, size=n_samples),
    
    # second data set - four clusters with normaldistribution
    make_blobs(n_samples=[n_samples // 10, n_samples * 4 // 10,
                          n_samples // 10, n_samples * 4 // 10],
               cluster_std=0.5, centers=blob_centers,
               random_state=random_state)[0].reshape(n_samples)
]

def plot_pts(ax, X, X_binned, counts):
    ax.set_xticks([]) # remove axis
    ax.set_yticks([])
    Y = np.zeros_like(X)
    ax.scatter(X, Y, c=X_binned, cmap = cmap,  marker = 'x')
    ax.set_ylim(-1,1)
    ax.text(5, -0.5, counts, horizontalalignment='center')

def bin_and_plot(X, n_bins, strategy, ax):
    enc = KBinsDiscretizer(n_bins=n_bins, encode='ordinal', strategy=strategy)
    X_binned = enc.fit_transform(X.reshape(-1,1))
    unique, counts = np.unique(X_binned, return_counts=True)
    plot_pts(ax, X, X_binned.ravel(), counts)
    
fig, axarr = plt.subplots(len(strategies), len(data), figsize=(10,5))

if axarr.ndim == 1:
    axarr = axarr.reshape(-1,1)

for ax, col in zip(axarr[0], data):
    ax.set_title(col, size='large')
    
for ax, row in zip(axarr[:,0], strategies):
    ax.set_ylabel(row, size='large')

for data_index, data_name in enumerate(data, 0):
    base_index = data_index * len(strategies)
   
    for strategy_index, strategy in enumerate(strategies, 0):
        index = base_index + strategy_index
        
        bin_and_plot(X_list[data_index], n_bins, strategy, 
                     axarr[strategy_index][data_index])

fig.tight_layout()
#fig.suptitle('Binning with KBinsDiscretizer', fontsize=16)
fig.subplots_adjust(top=0.88)

plt.show()

fig.savefig('c:/tmp/binning.png')