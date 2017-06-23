import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Set up JB's preferred style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']


sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})


# def pick_ids(s):
#     if s in ['III','IV']:
#         return True
#     else:
#         return False


df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

df_big_force = df.loc[df['impact force (mN)'] > 2000, 'impact time (ms)']
f2_imp_ad = df.loc[df['ID'] == "II", ['impact force (mN)',
                                    'adhesive force (mN)', 'ID']]
f3_f4_ad_time = df.loc[df['ID'].isin(["III", "IV"]),
                   ['ID', 'time frog pulls on target (ms)',
                   'adhesive force (mN)']]


# #How to use an apply statement (apply is for a series)
# f3_f4_ad_time = df.loc[df['ID'].apply(pick_ids),
#                    ['ID', 'time frog pulls on target (ms)',
#                    'adhesive force (mN)']]
