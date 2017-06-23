import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Make a GroupBy object
gb = df.groupby('ID')

# Apply the np.mean function to the grouped object
df_mean = gb.apply(np.mean)
df_std = gb.apply(np.std)




#Either of the following two work
df_std_impf = df_std.loc[:, ['impact force (mN)']]
df_std['impact force (mN)']


def coeff_of_var(data):
    return np.std(data)/np.abs(np.mean(data))

cof_impf_adf = gb.apply(coeff_of_var)[['impact force (mN)',
                                    'adhesive force (mN)']]

df_comp = gb.agg([np.mean, np.median, np.std, coeff_of_var])[['impact force (mN)',
                    'adhesive force (mN)']]
