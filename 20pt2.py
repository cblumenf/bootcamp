import numpy as np

# Load in data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')


def xa_to_diameter(xa):
    """
    Convert an array of cross-sectional areas
    to diameters with commensurate units.
    """

    # Compute diameter from area
    diameter = np.sqrt(4*xa/np.pi)

    return diameter
