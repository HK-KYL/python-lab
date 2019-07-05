#A4
#%%
import pandas as pd 
#Question 1
df = pd.read_csv('automobile_data.csv')

#Question 2
print(df.shape)

#Question 3
print(df.head(8))
print(df.tail(8))

#Question 4
print(df.dtypes)

#Question 5
df.dropna(inplace=True)

#Question 6
print(df.shape)

#Question 7
grouped = df.groupby('company')
toyota = grouped.get_group('toyota')

#Question 8
print(grouped['average-mileage'].mean())

#Question 9
sortedDf = df.sort_values(by='price', ascending = False)
sortedDf.to_csv('automobile_data_new.csv')

#Question 10
print(sortedDf.describe())
