import pandas as pd
import scipy, numpy as np
from sklearn.preprocessing import Imputer

ds=pd.read_csv("iris (1).data")
x=ds.iloc[:,0:4].values
y=ds.iloc[:,4].values

print(ds)


from sklearn.preprocessing import MinMaxScaler
import numpy 

scaler=MinMaxScaler(feature_range=(0,1))
rescaledX=scaler.fit_transform(x[:,2].reshape(-1,1))
numpy.set_printoptions(precision=3)
x[:,2]=rescaledX.reshape(1,-1)
print(x[:,2])


from sklearn.preprocessing import Normalizer

scaler=Normalizer().fit(x)
normalizedX=scaler.transform(x)
normalizedX
