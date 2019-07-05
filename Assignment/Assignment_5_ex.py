#A5
#%% Q1

import matplotlib.pyplot as plt
import numpy as np 

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.scatter(np.linspace(0,1,5), np.linspace(0,5,5), marker="+")

ax2 = fig.add_subplot(222)
ax2.scatter(np.linspace(0,1,5), np.linspace(0,5,5), marker="x")

ax3 = fig.add_subplot(223)
ax3.scatter(np.linspace(0,1,5), np.linspace(0,5,5), marker="3")

ax4 = fig.add_subplot(224)
ax4.scatter(np.linspace(0,1,5), np.linspace(0,5,5), marker="4")

plt.show()

#%% Q2

import matplotlib.pyplot as plt 

books = {'Tom':10,'Dick':11,'Harry':9,'Slim':7,'Jim':12}

x = list(books.values())
y = list(books)

plt.barh(y,x, color="green")

plt.suptitle('How many books do you have?')
plt.xlabel('Number of books')

plt.show()

#%% Q3

import matplotlib.pyplot as plt 
import numpy as np 

fig = plt.figure()

ax1 = fig.add_subplot(311)
ax1.set(title="cosine wave", xlabel='time(s)', ylabel='voltage(mV)')
t = np.arange(0.0, 8.0, 0.02)
s = np.cos(2*np.pi*t)
ax1.plot(t, s, lw=2)
ax1.grid()

ax2 = fig.add_subplot(313)
ax2.set(title="sine wave", xlabel='time(s)', ylabel='voltage(mV)')
t = np.arange(0.0, 8.0, 0.01)
s = np.sin(2*np.pi*t)
ax2.plot(t, s, lw=2)
ax2.grid()

plt.show()

#%%