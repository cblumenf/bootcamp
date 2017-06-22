import bootcamp_utils
import numpy as np
import matplotlib.pyplot as plt
import scipy

import seaborn as sns

#Set up JB's preferred style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

#Load the data
data_high = np.loadtxt('data/xa_high_food.csv')
data_low = np.loadtxt('data/xa_low_food.csv')

# Make smooth x-values
x = np.linspace(1600, 2500, 400)

# Compute theoretical Normal distribution
cdf_theor_low = scipy.stats.norm.cdf(x, loc=np.mean(data_low),
                                scale=np.std(data_low))
cdf_theor_high = scipy.stats.norm.cdf(x, loc=np.mean(data_high),
                                scale=np.std(data_high))

x_low = bootcamp_utils.ecdf(data_low)[0]
y_low = bootcamp_utils.ecdf(data_low)[1]
x_high = bootcamp_utils.ecdf(data_high)[0]
y_high = bootcamp_utils.ecdf(data_high)[1]

# Build figure
fig, ax = plt.subplots(1, 1)
_ = ax.set_xlabel('Cross sectional area (µm$^2$)')
_ = ax.set_ylabel('ECDF')

#paint out plot
low = ax.plot(x_low, y_low)
high = ax.plot(x_high, y_high)
theory_low = ax.plot(x, cdf_theor_low, color='gray')
theory_high = ax.plot(x,cdf_theor_high, color='gray')
_ = ax.legend(labels=('low', 'high', 'theory_low', 'theory_high'),
loc='lower right')

plt.show()
