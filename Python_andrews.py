"""Is there a pattern in our satisfaction survey data?
Are they potentially suitable for the ML algorithm?"""



import pandas as pd
from pandas.plotting import andrews_curves
import matplotlib.pyplot as plt

train_file = 'test.csv'
df_train = pd.read_csv(train_file)

df_train_s = df_train.loc[:,'satisfaction']
df_train_p = df_train.loc[:,'Inflight wifi service':'Arrival Delay in Minutes']
df_train = pd.concat([df_train_s, df_train_p], axis = 1)

#print(df_train.columns)
#print(df_train.head(5))



plt.figure()
andrews_curves(df_train,'satisfaction')

plt.show()

"""Looking at the final figure, the answer is yes:)"""





