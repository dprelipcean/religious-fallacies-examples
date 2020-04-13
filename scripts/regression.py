import numpy as np
from scipy.stats import linregress


def regression_points(x, y):
    """Find regression line"""
    gradient, intercept, r_value, p_value, std_err = linregress(x, y)
    print(f'{gradient} {r_value} {p_value}')
    mn = np.min(x)
    mx = np.max(x)
    x1 = np.linspace(mn, mx, 500)
    y1 = gradient * x1 + intercept
    return x1, y1
