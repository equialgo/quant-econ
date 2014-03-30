from __future__ import division
# coding=utf-8
__author__ = 'stijn'
import numpy as np
from scipy.stats import norm


def approx_markov(rho, sigma_u, m=3, n=7):
    """
    Computes the Markov matrix associated with a discretized version of
    the linear Gaussian AR(1) process

        y_{t+1} = rho * y_t + u_{t+1}

    according to Tauchen's method.  Here {u_t} is an iid Gaussian process with
    zero mean.

    Parameters:

        * rho is the correlation coefficient
        * sigma_u is the standard deviation of u
        * m parameterizes the width of the state space
        * n is the number of states

    Returns:

        * x, the state space, as a NumPy array
        * a matrix P, where P[i,j] is the probability of transitioning from
            x[i] to x[j]
    """
    sigma_y = np.sqrt(sigma_u**2/(1-rho**2))
    x_min = -m*sigma_y
    x_max = m*sigma_y
    s = (x_max-x_min)/(n-1)

    x = np.linspace(x_min, x_max, n)
    xj, xi = np.meshgrid(x, x)

    F = norm(loc=0, scale=sigma_u).cdf

    P = np.column_stack((F(x_min-rho*xi[:, 0]+s/2),
                        F(xj[:, 1:-1]-rho*xi[:, 1:-1]+s/2)-F(xj[:, 1:-1]-rho*xi[:, 1:-1]-s/2),
                        1-F(x_max-rho*xi[:, -1]-s/2)))
    return x, P