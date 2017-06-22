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

bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))

bs_replicate = np.mean(bs_sample)

#generate lots of replicates
n_reps = 100000

#Initialize the replicates array
bs_reps_2012 = np.empty(n_reps)

#compute replicates
for i in range(n_reps):
    bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
    bs_reps_2012[i] = np.std(bs_sample)

# x_bs, y_bs = bootcamp_utils.ecdf(bs_sample)
#
# fig, ax = plt.subplots(1, 1)
# _ = ax.set_xlabel('beak depth (mm)')
# _ = ax.set_ylabel('ECDF')
# _ = ax.plot(x_bs, y_bs, marker='.', linestyle='none',
#             label='bs sample')
# _ = ax.plot(x_2012, y_2012, marker='.', linestyle='none',
#             label='2012')
#
# ax.legend(loc='lower right')
# plt.show()
