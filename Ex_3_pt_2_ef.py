import numpy as np

# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

#Load in the data
wt_lac = np.loadtxt('data/wt_lac.csv', delimiter=',', skiprows=3)
q18m_lac = np.loadtxt('data/q18m_lac.csv', delimiter=',', skiprows=3)
q18a_lac = np.loadtxt('data/q18a_lac.csv', delimiter=',', skiprows=3)

#Concentrations
wt_lac_conc = wt_lac[:, 0]
q18m_lac_conc = q18m_lac[:, 0]
q18a_lac_conc = q18a_lac[:, 0]

#theoretical Concentrations
theory_conc = np.logspace(-5, 2, 100000)

#bohr values
bohr_x = np.logspace(-6, 6, 100000)



#Fold Changes
wt_lac_fc = wt_lac[:, 1]
q18m_lac_fc = q18m_lac[:, 1]
q18a_lac_fc = q18a_lac[:, 1]

def fold_change(conc, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):

    num = RK * (1 + (conc/KdA))**2
    den = ((1 + conc/KdA)**2 + (Kswitch * (1 + conc/KdI)**2))
    fc = (1 + (num/den))**-1
    return fc

def bohr_parameter(conc, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    num = (1 + (conc/KdA))**2
    den = ((1 + conc/KdA)**2 + (Kswitch * (1 + conc/KdI)**2))
    bp = -np.log(RK) - np.log(num/den)
    return bp

def fold_change_bohr(bohr_parameter):
    fcb = 1 / (1 + np.exp(-bohr_parameter))
    return fcb

#bohr paramters
bohr_wt = bohr_parameter(bohr_x, 141.5)

#Build figure
fig, ax = plt.subplots(1, 1)
_ = ax.set_xlabel('Concentration (mM)')
_ = ax.set_ylabel('Fold Change')
_ = ax.set_xscale('log')

#plot
wt_lac_plot = ax.plot(wt_lac_conc, wt_lac_fc)
q18m_lac_plot = ax.plot(q18m_lac_conc, q18m_lac_fc)
q18a_lac_plot = ax.plot(q18a_lac_conc, q18a_lac_fc)
wt_theory = ax.plot(theory_conc, fold_change(theory_conc, 141.5))
q18m_theory = ax.plot(theory_conc, fold_change(theory_conc, 1332))
q18a_theory = ax.plot(theory_conc, fold_change(theory_conc, 16.56))
wt_bohr = ax.plot(bohr_x, fold_change_bohr(bohr_wt), color='gray')

_ = ax.legend(labels=('wt', 'q18m', 'q18a'), loc='lower right')


plt.show()










# # Constants:
#
# kda = 0.017 #(mM^-1)
# kdi = 0.002 #(mM^-1)
# kswtich = 5.8
#
#
# fold_change = (1 + (num/den))**-1
# num = RK * (1 + (conc/kda))**2
# den = ((1 + conc/kda)**2 + (kswitch * (1 + c/kdi)**2))
#
# def fold_change(mutant ,RK=141.5,KdA=):
# """
# this function determines the fold change as a function of concentration
# """
#
#
#
#     if mutant is wt_lac:
#         conc = wt_lac_conc
#     elif mutant is q18m_lac:
#         conc = q18m_lac_conc
#     elif mutant is q18a_lac:
#         conc = q18a_lac_conc
