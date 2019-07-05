#Lab 5
#%% 
# Exercise 1
import numpy as np
a = np.arange(1, 200, 2)
a = a.reshape(10, 10)
print(a.shape)
print(a.size)
print(a)

#%% 
# Exercise 2
import numpy as np
a = np.full((8, 8), 2.5)
print(a)
#%%
a = np.arange(0, 16)
a = a.reshape(4, 4)
print(a)
#%%
a = np.eye(6, 6)
print(a)
#%%
a = np.random.randn(20)
x = a.mean()
print(a)
print("The mean value is {}.".format(x))
#%%
a = np.random.randint(1, 50, 18).reshape(3, 6)
print(a)
#%%
a = np.random.uniform(0, 10, 20).reshape(4, 5)
print(a)
print("The mean is {}.".format(a.mean()))
print("The max is {}.".format(a.max()))
print("The min is {}.".format(a.min()))