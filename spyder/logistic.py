# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score

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

def quality(model, features, labels):
    predictions = model.predict(features)
    probabilities = model.predict_proba(features)
    conf_matrix = confusion_matrix(labels, predictions)   
    accuracy = accuracy_score(labels, predictions)  
    auc = roc_auc_score(labels, probabilities[:,1])
    return conf_matrix, accuracy, auc

def fit_and_evaluate(model, X_train,y_train, X_test, y_test, confusion_matrix = False):
    model.fit(X_train,y_train)
    conf_matrix, accuracy, auc = quality(model, X_test, y_test)
    if confusion_matrix:
        print("\nConfusion Matrix:\n{0}".format(conf_matrix))
    print("Accuracy: {0:.2f} %".format(accuracy*100), "AUC: {0:.3f} %".format(auc))

print("\n------ Zero Rule ------")
dummy = DummyClassifier(strategy='most_frequent') 
fit_and_evaluate(dummy, X_train, y_train, X_test, y_test)

print("\n------ Logistic Regression ------")
logistic = LogisticRegression() 
fit_and_evaluate(logistic, X_train, y_train, X_test, y_test)

print("\n------ LDA ------")
lda = LinearDiscriminantAnalysis() 
fit_and_evaluate(lda, X_train, y_train, X_test, y_test)

print("\n------ Gaussian Naive Bayes ------")
gaussianNB = GaussianNB()
fit_and_evaluate(gaussianNB, X_train, y_train, X_test, y_test)


print("\n------ KNN ------")
knn = KNeighborsClassifier(n_neighbors=13)
fit_and_evaluate(knn, X_train, y_train, X_test, y_test)

print("\n------ Decision Tree (Gini) ------")
dtree = DecisionTreeClassifier(criterion='gini')
fit_and_evaluate(dtree, X_train, y_train, X_test, y_test)

print("\n------ Decision Tree (Entropy) ------")
dtree = DecisionTreeClassifier(criterion='entropy')
fit_and_evaluate(dtree, X_train, y_train, X_test, y_test)

print("\n------ Random Forest (Gini) ------")
rfc = RandomForestClassifier(criterion='gini')
fit_and_evaluate(rfc, X_train, y_train, X_test, y_test)

print("\n------ Random Forest (Entropy) ------")
rfc = RandomForestClassifier(criterion='gini')
fit_and_evaluate(rfc, X_train, y_train, X_test, y_test)

print("\n------ Gradient Boosting Classifier ------")
boosting = GradientBoostingClassifier()
fit_and_evaluate(boosting, X_train, y_train, X_test, y_test)

print("\n------ SVM ------")
svc = SVC(kernel = 'rbf', probability=True)
fit_and_evaluate(svc, X_train, y_train, X_test, y_test)