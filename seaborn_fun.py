import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Set up JB's preferred style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

#import frog dat
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

#seaborn works on tidy dataframes
ax = sns.swarmplot(data=df, x='ID', y='impact force (mN)', hue='date')
ax.set_ylabel('impact force (mN)')
ax.set_xlabel('')
ax.legend_.remove()

plt.show()
