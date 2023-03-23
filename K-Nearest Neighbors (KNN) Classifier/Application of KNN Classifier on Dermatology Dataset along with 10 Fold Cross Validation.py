import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import Imputer

dataset=pd.read_csv("dermatology (2).data")
print(dataset.shape)
x=ds.iloc[:, 0:33].values
y=ds.iloc[:,34].values


t_size=0.30
X_train,X_test, Y_train, Y_test= train_test_split(x,y,test_size=t_size)
knn= KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, Y_train)
predictions= knn.predict(X_test)
print(accuracy_score(Y_test,predictions))