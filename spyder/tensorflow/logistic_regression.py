# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:34:25 2019

@author: Karsten
"""

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import tensorflow as tf

# turn off tensorflow deprecation warnings
import tensorflow.python.util.deprecation as deprecation
deprecation._PRINT_DEPRECATION_WARNINGS = False

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

# ============================
#     Data Preprocessing
# ============================
data_sets = ('bank-10percent', 'bank-full', 'bank-balanced')

bank = pd.read_csv('../../data/' + data_sets[1] + '.csv')

label_col = 'y'
label = bank[label_col]
features = bank.drop(columns=['y'])

label_encoded = pd.get_dummies(label, drop_first = False)
features_encoded = pd.get_dummies(features, drop_first = True)

X_train, X_test, y_train, y_test = train_test_split(features_encoded, label_encoded, test_size = 0.2, random_state = 167)

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

class_count=2
feature_count=X_train.shape[1]

# ============================
#       TF Setup
# ============================
# Parameters
learning_rate = 0.1
training_epochs = 100
display_step = 5

# tf Graph Input
x = tf.placeholder(tf.float32, [None, feature_count]) 
y = tf.placeholder(tf.float32, [None, class_count]) 

# Set model weights
W = tf.Variable(tf.zeros([feature_count, class_count]))
b = tf.Variable(tf.zeros([class_count]))

# Construct model
prob = tf.nn.softmax(tf.matmul(x, W) + b) # Softmax

# Minimize error using cross entropy
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(prob), reduction_indices=1))

pred_class = tf.argmax(prob, 1);
true_class = tf.argmax(y, 1);
     
_, accuracy = tf.metrics.accuracy(true_class, pred_class)
    
# Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initialize the variables (i.e. assign their default value)
init = [ 
        tf.global_variables_initializer(), 
        tf.local_variables_initializer()    # for metrics
        ]

# ============================
#       Start training
# ============================
with tf.Session() as sess:

    # Run the initializer
    sess.run(init)

    # Training cycle
    for epoch in range(training_epochs):
        # Run optimization op (backprop) and cost op (to get loss value)
        _, c, acc = sess.run([optimizer, cost, accuracy], feed_dict={x: X_train, y: y_train})
        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c), "Accuracy: {0:.2f} %".format(acc*100))

    print("Optimization Finished!")

    # Test model
    pc, tc, acc = sess.run([pred_class, true_class, accuracy], 
                            feed_dict={x: X_test, y: y_test})
    
    # Calculate accuracy
    print("Confusion Matrix :")   
    print(confusion_matrix(tc, pc))
    
    print("Accuracy: {0:.2f} %".format(acc*100))
