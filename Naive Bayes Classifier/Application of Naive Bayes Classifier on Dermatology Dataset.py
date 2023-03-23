import pandas as pd, scipy, numpy as np
import matplotlib.pyplot as plot
from sklearn import datasets,metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split

ds= pd.read_csv("dermatology (2).data")
#ds.head()
x=ds.iloc[:, 0:33].values
y=ds.iloc[:,34].values

X_train,X_test, Y_train, Y_test= train_test_split(x,y,test_size=0.40)
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
naive=GaussianNB()
naive.fit(X_train, Y_train,)
predict=naive.predict(X_test)
print("predicted value :",predict)

print("\nAccuracy Score :",metrics.accuracy_score(Y_test, predict))
print("\nConfusion Matrix :")
print(metrics.confusion_matrix(Y_test, predict))
print("\nClassification Report :")
print(metrics.classification_report(Y_test, predict))


X_train,X_test, Y_train, Y_test= train_test_split(x,y,test_size=0.20)
naive=GaussianNB()
naive.fit(X_train, Y_train,)
predict=naive.predict(X_test)
print("predicted value :",predict)

print("\nAccuracy Score :",metrics.accuracy_score(Y_test, predict))
print("\nConfusion Matrix :")
print(metrics.confusion_matrix(Y_test, predict))
print("\nClassification Report :")
print(metrics.classification_report(Y_test, predict))
