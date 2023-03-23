import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

names=['sepal-length','sepal-width','petal-length','petal-width','class']
dataset=pd.read_csv("iris (1).data", names=names)
print(dataset.shape)
array=dataset.values
#dividing in train and test
X=array[:,0:4]
Y=array[:,4]
t_size=0.30
X_train,X_test, Y_train, Y_test= train_test_split(X,Y,test_size=t_size)
knn= KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, Y_train)
predictions= knn.predict(X_test)
print(accuracy_score(Y_test,predictions))


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

names=['sepal-length','sepal-width','petal-length','petal-width','class']
dataset=pd.read_csv("iris (1).data", names=names)
print(dataset.shape)
array=dataset.values
#dividing in train and test
X=array[:,0:4]
Y=array[:,4]
t_size=0.30
X_train,X_test, Y_train, Y_test= train_test_split(X,Y,test_size=t_size)
knn= KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)
predictions= knn.predict(X_test)
print(accuracy_score(Y_test,predictions))


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

names=['sepal-length','sepal-width','petal-length','petal-width','class']
dataset=pd.read_csv("iris (1).data", names=names)
print(dataset.shape)
array=dataset.values
#dividing in train and test
X=array[:,0:4]
Y=array[:,4]
t_size=0.30
X_train,X_test, Y_train, Y_test= train_test_split(X,Y,test_size=t_size)
knn= KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, Y_train)
predictions= knn.predict(X_test)
print(accuracy_score(Y_test,predictions))