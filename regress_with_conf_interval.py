import numpy as np
from scipy import polyval, polyfit, sqrt, stats
# * Based on https://scipy-cookbook.readthedocs.io/items/LinearRegression.html

def regress_with_conf_interval(time, x, confidential_interval):
    n = int(len(time) * confidential_interval)
    t = time[:n]
    xn = x[:n]
    
    assert len(t) == len(xn)
    # parameters    
    # add some noise
    # xn = x + randn(n)

    (ar, br) = polyfit(t, xn, 1)
    xr = polyval([ar, br], t)
    err = sqrt(sum((xr - xn)**2)/n)
    (slope, intercept, r_value, p_value, std_err) = stats.linregress(t, xn)

    return slope, t, xr
