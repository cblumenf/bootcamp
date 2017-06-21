import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

sns.set()

#Load in data
xa_low = np.loadtxt('data/xa_low_food.csv', comments="#")
xa_high = np.loadtxt('data/xa_high_food.csv', comments="#")

#Set up nice bin widths
bins = np.arange(1700, 2501, 50)

#Set up plot
fig, ax = plt.subplots(1, 1)
_ = ax.set_xlabel('Cross-sectional area (µm$^2$)')
_ = ax.set_ylabel('count')

# Paint the data!
_ = ax.hist(xa_low, bins=bins)
