import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, len(data)+1)/len(data)

    return (x, y)

def bs_replicate(data, func=np.mean):
    """Compute a boostrap replciate from data."""
    bs_sample = np.random.choice(bd_2012, replace=True, size=len(data))
    return func(bs_sample)

def draw_bs_reps(data, func=np.mean, size=10000):
    """Draw boostrap replicates from 1d data."""
    return: np.array([bs_replicate(data, func=func) for _ in range(size)])
