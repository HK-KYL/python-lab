#Lab 9
import numpy as np 
from scipy import stats 
import pandas as pd 
from matplotlib import pyplot as plt

df = pd.read_csv('survey1.csv', index_col="customer id")
salary = df['salary range'].values

median = np.median(salary)

per75 = np.percentile(salary, 75) 
per25 = np.percentile(salary, 25)

iqr = stats.iqr(salary)

labels = ['below 15K',
          '15K <= $ < 20K',
          '20K <= $ < 25K',
          '25K <= $ < 30K',
          '30K <= $ < 35K',
          '35K <= $ < 40K',
          '40K <= $ < 45K',
          '45K <= $ < 50K',
          '50K <= $ < 55K',
          '55K <= $ < 60K',
          '60K <= $ < 65K',
          '65K <= $ < 70K',
          '70K <= $ < 75K',
          '75K <= $ < 80K',
          '80K <= $ < 85K',
          '85K <= $ < 90K',
          '90K <= $ < 95K',
          '95K or above']

edges = np.arange(10000, 100001, 5000)

hist, edges = np.histogram(salary, bins=edges)

print('Score Distribution')
for i in range(len(hist)): 
    print('%s: \t %d' % (labels[i], hist[i]))
    
bin_centers = 0.5 * (edges[1:] + edges[:-1])

plt.plot(bin_centers, hist, color='green') 
plt.xticks(bin_centers, labels, rotation='vertical')

q1 = median-iqr/2
q2 = median
q3 = median+iqr/2

plt.axvline(x=q1, color='lightgrey', linestyle="--") 
plt.axvline(x=q2, color='red', linestyle=":") 
plt.axvline(x=q3, color='lightgrey', linestyle="--")

plt.legend(['Distribution', 'IQR', 'Median = 35000']) 