import numpy as np
import matplotlib.pyplot as plot
import pandas
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

ds=pandas.read_excel("SalaryAge.xlsx")
x=ds['YearsExperience'].values.reshape(-1,1)
y=ds['Salary'].values.reshape(-1,1)

ds.plot(x='YearsExperience',y=['Salary'],style='*',color='blue')
plot.title('YearsExperience Vs Salary')
plot.xlabel('YearsExperience')
plot.ylabel('Salary')
plot.show()

xTrain,xTest,yTrain,yTest=train_test_split(x,y,test_size=0.20,random_state=12)

xTrain,xTest,yTrain,yTest=train_test_split(x,y,test_size=0.20,random_state=12)

yPrediction=LR.predict(xTest)
compare=pandas.DataFrame({'Actual':yTest.flatten(),'Predicted':yPrediction.flatten()})

plot.scatter(xTrain,yTrain,color='blue')
plot.plot(xTrain,LR.predict(xTrain),color='red')
plot.title('YearsExperience Vs Salary')
plot.xlabel('YearsExperience')
plot.ylabel('Salary')
plot.show()

plot.scatter(xTest,yTest,color='yellow')
plot.plot(xTest,LR.predict(xTest),color='purple')
plot.title('YearsExperience Vs Salary')
plot.xlabel('YearsExperience')
plot.ylabel('Salary')

plot.show()

print('Mean Absolute Error :',
 metrics.mean_absolute_error(yTest,yPrediction)/100)
 
print('Mean Squared Error :',
 metrics.mean_squared_error(yTest,yPrediction)/100)
 
print('Root Mean Squared Error :',
 np.sqrt(metrics.mean_squared_error(yTest,yPrediction))/100)

compare