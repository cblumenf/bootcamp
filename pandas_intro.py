import pandas as pd

# Dictionary of top men's World Cup scorers and how many goals
wc_dict = {'Klose': 16,
           'Ronaldo': 15,
           'Muller': 14,
           'Fontaine': 13,
           'Pele': 12,
           'Kocsis': 11,
           'Klinsmann': 11}

# Dictionary of nations
nation_dict = {'Klose': 'Germany',
               'Ronaldo': 'Brazil',
               'Muller': 'Germany',
               'Fontaine': 'France',
               'Pele': 'Brazil',
               'Kocsis': 'Hungary',
               'Klinsmann': 'Germany'}

# Create a Series from the dictionary
s_goals = pd.Series(wc_dict)
s_nation = pd.Series(nation_dict)

#
df_wc = pd.DataFrame({'nation': s_nation, 'goals': s_goals})
