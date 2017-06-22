import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

import bootcamp_utils

#Set up JB's preferred style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

x_1975, y_1975 = bootcamp_utils.ecdf(bd_1975)
x_2012, y_2012 = bootcamp_utils.ecdf(bd_2012)

fig, ax = plt.subplots(1, 1)
_ = ax.set_xlabel('beak depth (mm)')
_ = ax.set_ylabel('ECDF')
_ = ax.plot(x_1975, y_1975, marker='.', linestyle='none',
            label='1975')
_ = ax.plot(x_2012, y_2012, marker='.', linestyle='none',
            label='2012')
ax.legend(loc='lower right')
plt.show()
