import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, len(data)+1)/len(data)

    return (x, y)
