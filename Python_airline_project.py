import pandas as pd
import matplotlib.pyplot as plt

file_test = 'test.csv'
df_test = pd.read_csv(file_test)

#print(df_test.head(2))

"""Three things that passengers are least happy about"""

df_test_points = df_test.loc[:,'Inflight wifi service':'Cleanliness'] #I limit only to those that are measured on a scale of 0 to 5
df_test_points_sum = df_test_points.sum()
df_test_points_sum = df_test_points_sum.sort_values().head(3)

print(f'Passangers are least happy about:\n\n{df_test_points_sum}. \n\nI`ll analize this three aspects. Let`s go:)')


"""-----------"""

df_test_3 = df_test.loc[:,('Gender','Customer Type','Age','Inflight wifi service','Ease of Online booking','Gate location')]


df_age = pd.DataFrame(columns=('Age','Age range'))
for i in range(1,101):

    if i < 18:
        a = 'kid'
    elif i < 30:
        a = 'mature'
    elif i < 60:
        a = 'middleage'
    else:
        a = 'senior'
    df_age.loc[i]=[i,a]

df_test_3 = pd.merge(df_test_3,df_age, how = 'left', on='Age')    



def grouping(category):
    df_test_3_group_mean = df_test_3.loc[:,(category,'Inflight wifi service','Ease of Online booking','Gate location')].groupby([category]).mean()
    df_test_3_group_mean.plot.bar(color={'Inflight wifi service': 'red', 'Ease of Online booking': 'orange','Gate location':'blue'})
    plt.show()

    

y_n = 'Yes'

while y_n == 'Yes':

    a = input("""By what category would you like to analyze\n\n
    1: Gender
    2: Customer Type
    3: Age\n""")
    
    if a == '1':
        grouping('Gender')
    elif a == '2':
        grouping('Customer Type')
    elif a=='3':
        grouping('Age range')
    else:
        print('You have selected an incorrect value')
    y_n = input('Do you continue? \nYes/No\n')
    y_n = y_n.capitalize()










