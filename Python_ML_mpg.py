
"""
Created on Tue Mar 19 11:53:05 2024

@author: Kasia
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from pandas.plotting import andrews_curves
import matplotlib.pyplot as plt

df_auto = pd.read_csv('auto-mpg.csv')
df_auto = df_auto.drop('horsepower',axis=1)



X = df_auto.loc[:,'cylinders':'origin']
y = df_auto.loc[:,'mpg']


lr = LinearRegression()
lr.fit(X.to_numpy(),y)
print(lr.score(X.to_numpy(),y))


my_car1 = [4, 160, 190, 12, 90, 1]
my_car2 = [4, 200, 260, 15, 83, 1]
 
cars = [my_car1, my_car2]

print(lr.predict(cars))
