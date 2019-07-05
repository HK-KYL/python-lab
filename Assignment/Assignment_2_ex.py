#A2
#Quesiton 1
#%%
def leap_year(x):
    if x % 400 == 0:
        return True
    if x % 100 == 0:
        return False
    if x % 4 == 0:
        return True
    else:
        return False
    
print(leap_year(2019))
print(leap_year(2000))
print(leap_year(2100))

#Question 2
#we ignore the import since we use the same python file to include the leap_year() function
#%%
def days_of_month(x):
    months = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 
              'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}
    print('Year {}:'.format(x))
    for i in months:
        if i != 'February':
            print(i, months[i])
        else:
            if(leap_year(x)):
                print(i, 29)
            else:
                print(i, 28)

days_of_month(2019)
days_of_month(2000)

#Question 3
#%%
import time
for row in range(1, 9):
#output 2x(8-row) spaces
    for i in range(16-2*row):
        print(' ', end='')
#output row #'s
    for i in range(row):
        print('# ', end='')
        time.sleep(1)
    print()
        
#Question 4 Prime Number
#%%
import math
def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    for i in range(2, math.ceil(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

#Question 5
#%%    
def primes(x):
    prime = []
    for num in range(2, x+1):
        if is_prime(num):
            prime.append(num)
    return prime
        
a = primes(10)
print(a)
b = primes(100)
print(b)
