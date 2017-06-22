import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

import bootcamp_utils

#Set up JB's preferred style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})


mu = 10
sigma = 1
x_rnd = np.random.normal(mu, sigma, size=1000000)

#Make ECDF
x, y = bootcamp_utils.ecdf(x_rnd)

#plot ECDF
fig, ax = plt.subplots(1, 1)
#_ = ax.plot(x, y, marker='.', linestyle='none')

#plot hist
_ = ax.hist(x, bins=100)

plt.show()
