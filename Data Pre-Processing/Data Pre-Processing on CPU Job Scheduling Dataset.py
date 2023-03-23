import pandas as pd
import scipy, numpy as np

ds=pd.read_excel("Job_Scheduling.xlsx")
x=ds.iloc[:,0:4].values
y=ds.iloc[:,4].values

print(x)


from sklearn.preprocessing import Imputer

imp=Imputer(missing_values=np.nan,strategy="mean")
X=imp.fit_transform(x)
Y=y.reshape(-1,1)
Y=imp.fit_transform(Y)
Y=Y.reshape(-1)
print(Y)


from sklearn.preprocessing import MinMaxScaler
import numpy 

scaler=MinMaxScaler(feature_range=(0,1))
rescaledX=scaler.fit_transform(X[:,1].reshape(-1,1))
numpy.set_printoptions(precision=3)
X[:,1]=rescaledX.reshape(1,-1)
print(X[:,1])


from sklearn.preprocessing import Normalizer

scaler=Normalizer().fit(X)
normalizedX=scaler.transform(X)
normalizedX