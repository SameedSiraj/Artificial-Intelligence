import pandas as pd, scipy, numpy as np
import matplotlib.pyplot as plot
from sklearn import datasets,metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

ds= pd.read_excel("weatherTemp (1).xlsx")
#ds.head()
x=ds.iloc[:, 0:2].values
y=ds.iloc[:,2].values

le=LabelEncoder()
x[:,0]=le.fit_transform(x[:,0])
x[:,1]=le.fit_transform(x[:,1])
y=le.fit_transform(y)

print("Weather:", x[:,0])
print("Temp:", x[:,1])
print("Play:", y)

naive=GaussianNB()
naive.fit(x, y)
predict=naive.predict([[0,1]])
print("predicted value :",predict)