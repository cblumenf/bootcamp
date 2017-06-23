import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Set up JB's preferred style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']


sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

df_frog = pd.DataFrame(index=['I', 'II', 'III', 'IV'],
                       data={'age': ['adult', 'adult', 'juvenile', 'juvenile'],
                             'SVL (mm)': [63, 70, 28, 31],
                             'weight (g)': [63.1, 72.7, 12.7, 12.7],
                             'species': ['cross', 'cross', 'cranwelli',
                             'cranwelli']})

final = df.join(df_frog, on='ID')

#database theory: denormalization s
