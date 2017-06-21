import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

#Set up JB's preferred style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

#Load the data
data_high = np.loadtxt('data/xa_high_food.csv')
data_low = np.loadtxt('data/xa_low_food.csv')

def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, len(data)+1)/len(data)

    return (x, y)

x_low = ecdf(data_low)[0]
y_low = ecdf(data_low)[1]
x_high = ecdf(data_high)[0]
y_high = ecdf(data_high)[1]

# Build figure
fig, ax = plt.subplots(1, 1)
_ = ax.set_xlabel('Cross sectional area (µm$^2$)')
_ = ax.set_ylabel('ECDF')

#paint out plot
low = ax.plot(x_low, y_low)
high = ax.plot(x_high, y_high)
_ = ax.legend(labels=('low', 'high'), loc='lower right')
plt.show()
