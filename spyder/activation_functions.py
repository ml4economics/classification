# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:28:49 2019

@author: Karsten
"""

import numpy as np
import matplotlib.pylab as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def softplus(x):
    return np.log(1 + np.exp(x))

def tanh(x):
    return np.tanh(x)

x = np.arange(-4.0, 4.0, 0.1)
y_sigmoid = sigmoid(x)
y_relu = relu(x)
y_tanh = tanh(x)
y_soft = softplus(x)

fig = plt.figure()
plt.plot(x, y_sigmoid, label='Logistisch', color='red',   lw=1)
plt.plot(x, y_relu,    label='ReLU',     color='green', lw=1)
#plt.plot(x, y_soft,    label='Softplus', color='orange', lw=1)
plt.plot(x, y_tanh,    label='TanH',     color='blue',  lw=1)
plt.ylim(-1.1, 1.1)
plt.legend()
plt.grid(True, linestyle='dotted')
plt.show()

fig.savefig('c:/tmp/activation.png')