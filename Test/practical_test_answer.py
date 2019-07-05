# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:26:04 2019

@author: chxw
"""

#%%
#Question 1:
#1):
list1 = list(range(101))
#2):
list2 = list(range(0, 100, 3))
#3):
list3 = list(range(100, -1, -5))

#%%
#Question 2:
Players = ['Martina', 'Charles', 'Michael', 'Florence', 'Eli']
Players.sort()
print(Players)
list1 = Players[0:3]
list2 = Players[1:4]
list3 = Players[-3:]

#%%
#Question 3:
dic = {'name' : 'Andrew', 'Age' : 15, 'Sex' : 'Male'}
dic['Age'] = 16
dic['Grade'] = 85.0
dic.pop('Sex')

#%%
#Question 4:
scores = [65, 85, 62, 95, 54, 62, 84, 75, 91, 98]
high = scores[0]
low = scores[0]
i = 1
while i < len(scores):
    if scores[i] > high:
        high = scores[i]
    if scores[i] < low:
        low = scores[i]
    i = i + 1
print(high, low)

#%%
#Question 5:
score = -1
while score > 100 or score < 0:
    score = int(input("please input an integer grade between 0 and 100:"))

if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'
print(grade)
    
#%%    
#Question 6:
scores = {'1' : 95, '2' : 82, '3' : 'absence', '4' : 83, '5' : 85, '6' : 83, '7' : 65, '8' : 85, '9' : 95, '10' : 75}
sum = 0
for i in scores.keys():
    if scores[i] == 'absence':
        scores[i] = 0
    sum += scores[i]

mean = sum / len(scores)
print(mean)

#%%
#Question 7:
import time
for i in range(8):
    for j in range(i + 1, 0, -1):
        print(j, end = '')
        time.sleep(0.2)
    print()
    
#%%
#Question 8:
def replace_hkbu(s):
    return s.replace('HKBU', 'Hong Kong Baptist University')
test = replace_hkbu('HKBU is located at Kowloon Tong. I love HKBU.')
print(test)

#%%
#Question 9:
str = 'Today is Monday. It is sunny and warm.'
str = str.lower()
str = str.replace('.', '')

str_list = str.split(' ')

#%%
#Question 10:
def high_freq(s):
    
    #use dictionary freq to store the frequencies of each non-whitespace character
    freq = {}
    for c in s:
        if not c.isspace():
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

    #find the character with the highest frequency
    index = ''
    high = 0
    for c in freq:
        if freq[c] > high:
            high = freq[c]
            index = c
    
    return index

high_freq('Hong Kong Baptist University is in Kowloon Tong')