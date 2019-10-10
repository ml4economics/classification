# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:31:02 2019

@author: Karsten
"""
import warnings
warnings.filterwarnings('ignore')

# turn off tensorflow deprecation warnings
import tensorflow.python.util.deprecation as deprecation
deprecation._PRINT_DEPRECATION_WARNINGS = False

import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

def evaluate_model(model, features, labels):
    _, accuracy = model.evaluate(features, labels)
    print('Accuracy: %.2f' % (accuracy*100))

    # make class predictions with the model
    predictions = model.predict_classes(features)
    print("Confusion Matrix :")   
    print(confusion_matrix(labels, predictions))
    
def plot_history(history):
    # to handle metrics keys changes in Keras 2.3
    # see https://github.com/keras-team/keras/releases/tag/2.3.0
    pre_23 = "acc" in history.history.keys()
    acc_key     = 'acc'     if pre_23 else 'accuracy'
    val_acc_key = 'val_acc' if pre_23 else 'val_accuracy'       
    
    acc = history.history[acc_key]
    val_acc = history.history[val_acc_key]
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(1, len(acc) + 1)

    # "bo" is for "blue dot"
    plt.plot(epochs, loss, 'bo', label='Training loss')
    # b is for "solid blue line"
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    # "go" is for "green dot"
    #plt.plot(epochs, acc, 'go', label='Training accuracy')
    # g is for "solid green line"
    #plt.plot(epochs, val_acc, 'g', label='Validation accuracy')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

def make_model(num_inputs, layers):
    model = Sequential()
    # first layer
    model.add(Dense(layers[0], input_dim=num_inputs, activation='relu'))
    #  intermediate layers
    for i in range(1, len(layers)):
        model.add(Dense(layers[i], activation='relu'))
    # final layer with a single node
    model.add(Dense(1, activation='sigmoid'))
    
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
    
# ============================
#     Data Preprocessing
# ============================
data_sets = ('bank-10percent', 'bank-full', 'bank-balanced')

bank = pd.read_csv('../../data/' + data_sets[1] + '.csv')

label_col = 'y'
label = bank[label_col]
features = bank.drop(columns=['y'])

label_encoded = pd.get_dummies(label, drop_first = True)
features_encoded = pd.get_dummies(features, drop_first = True)

scaler = StandardScaler()
features_normalized = scaler.fit_transform(features_encoded)

X_train, X_test, y_train, y_test = train_test_split(features_normalized, label_encoded, test_size = 0.2, random_state = 167)

feature_count=X_train.shape[1]

# ========================
#     parameters
# ========================
num_epochs=10
layers = [16, 8]

# ========================
# define the keras model
# ========================
model = make_model(feature_count, layers)

# ========================
#     train
# ========================
print("Fitting model")
history = model.fit(X_train, y_train, 
                    epochs=num_epochs,
                    validation_data=(X_test, y_test),
                    verbose=1)

# ========================
#     plot
# ========================
plot_history(history)

# ========================
#   evaluate the model
# ========================
print("Evaluating model on training data")
evaluate_model(model, X_train, y_train)

print("Evaluating model on test data")
evaluate_model(model, X_test, y_test)

