#Lab 8
#%%
import pandas as pd
import numpy as np

records = pd.read_csv('door_access_records.csv')
hourly_rate = pd.read_csv('hourly_rate.csv', index_col='Staff Name')

#%%
in_time, out_time = records['Working Hours (In & Out)'].str.split('-').str
records['In'] = in_time
records['Out'] = out_time
in_time = pd.to_datetime(in_time)
out_time = pd.to_datetime(out_time)
working_hours = out_time - in_time
working_hours = working_hours.astype('timedelta64[m]')
working_hours = round(working_hours/60, 2)
records['Working Hours'] = working_hours
#%%
records.drop('Working Hours (In & Out)', axis = 1, inplace = True)

#%%
records = pd.merge(records, hourly_rate, how='left', left_on='Staff Name', right_index=True)

#%%
records['Daily Wage'] = records['Salary Rate (per hour)'] * records['Working Hours']

records.sort_values(by = ['Working Hours', 'Staff Name'], ascending = False, inplace = True)

#%%
table1 = pd.pivot_table(records, values = 'Working Hours', index = 'Staff Name', aggfunc = np.sum)

#%%
table2 = pd.pivot_table(records, values = 'Working Hours', index = 'Department', columns='Date',  aggfunc = np.sum)

#%%
table3 = pd.pivot_table(records, values = ['Working Hours', 'Daily Wage'], index = 'Staff Name', aggfunc = {'Working Hours':[min, max, np.mean, np.sum], 'Daily Wage':np.sum})

#%%
table4 = pd.pivot_table(records, values = ['Daily Wage', 'Working Hours'], index = 'Department', aggfunc = np.sum)

table4.rename(columns={'Daily Wage':'Total salary', 'Working Hours':'Total Working Hours'}, inplace = True)
