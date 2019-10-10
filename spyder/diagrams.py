# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:31:05 2019

@author: Karsten
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-5., 5., 0.1)

def logistic(x):
    return 1 / (1+np.exp(-x))

fig = plt.figure()
plt.plot(t, logistic(t))
plt.text(-4.5, .8, r'$h(x)=\dfrac{1}{1+exp(-x)}$', fontsize=12, bbox=dict(facecolor='white', alpha=1))
plt.grid(True, linestyle='dotted')
#plt.title('Logistische Funktion')
plt.show()

fig.savefig('c:/tmp/logistic.png')
