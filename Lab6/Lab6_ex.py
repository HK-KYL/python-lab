#Lab 6
#%%
#Exercise
import pandas as pd

df = pd.read_csv('lab6_sampledata1.csv')
df['Category'] = df['CategoryProduct'].str[:4]
df['Product'] = df['CategoryProduct'].str[4:]
del df['CategoryProduct']
