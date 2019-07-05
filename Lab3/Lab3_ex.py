#Lab 3
#%%
#Exercise 1
def min(a, b, c):
    minimun = a
    if b &lt; minimun:
        minimun = b
    
    if c &lt; minimun:
        minimun = c
    return minimun

min(4, 7, 2)

#%%
#Exercise 2
def converter(x):
    return 1.8 * x + 32

converter(37)

#%%
#Exercise 3
def odd(x):
    if x &lt; 0:
        print("Required a positive number")
        return
    return tuple(range(1, x+1, 2))

odd(-1)
odd(20)
odd(21)

#%%
#Exercise 4
def reverse(s):
    result = ""
    for i in range(len(s)):
        result += s[-i -1] 
    return result

reverse("Hello world!")

#%%
#Exercise 5
def intersection(a, b):
    result = [];
    for i in range(len(a)):
        if a[i] in b:
            result.append(a[i])
    return result

a = [1, 3, 5, 7, 9]
b = (6, 2, 3, 7, 10)

intersection(a,b)