from sklearn.preprocessing import Normalizer
import numpy as np
from sklearn import metrics
from sklearn import datasets
from sklearn.svm import SVC
import random
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score,classification_report, confusion_matrix
import pandas as pd, scipy
from numpy import genfromtxt
from sklearn.preprocessing import LabelEncoder

names=['1','2','3','4','5','6','7','8','9','10']
dataset=pd.read_csv("C:\\Users\\DELL\\Desktop\\magic04.data",names=names)

randomlist=random.sample(range(3, 19000), 3000)

x=dataset.iloc[randomlist, 0:9].values
y=dataset.iloc[randomlist,9].values

X_train,X_test, Y_train, Y_test= train_test_split(x,y,test_size=0.30)
naive=GaussianNB()
naive.fit(X_train, Y_train,)
predict=naive.predict(X_test)
print("predicted value :",predict)

print("\nAccuracy Score :",metrics.accuracy_score(Y_test, predict))
print("\nConfusion Matrix :")
print(metrics.confusion_matrix(Y_test, predict))
print("\nClassification Report :")
print(metrics.classification_report(Y_test, predict))


X_train,X_test, Y_train, Y_test= train_test_split(x,y,test_size=0.30)
svclassifier=SVC(kernel='linear')
svclassifier.fit(X_train,Y_train)
Y_pred=svclassifier.predict(X_test)
print("predicted value :",predict)

print("\nAccuracy Score :",metrics.accuracy_score(Y_test, predict))
print("\nConfusion Matrix :")
print(metrics.confusion_matrix(Y_test, predict))
print("\nClassification Report :")
print(metrics.classification_report(Y_test, predict))