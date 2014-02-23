# coding=utf-8
__author__ = 'stijn'

import numpy as np
from random import uniform
from pylab import plot, show, legend

def factorial(n):
    """
    @param n:
    @return: factorial(n)
    """
    n = int(n)
    if n < 0:
        return np.nan
    else:
        return np.prod(np.arange(1, n+1))


def binomial_rv(n, p):
    """
    @rtype : int
    @param n: number of trials
    @param p: probability of success
    @return: number of succeeded trials
    """
    return np.sum(np.random.uniform(0, 1, n) < p)


def pi_mc_approx(n):
    """
    @rtype : float
    @param n: number of trials
    @return: Monte Carlo approximation of pi
    """
    x = np.random.uniform(-1, 1, n)  # sample x between -1 and 1
    y = np.random.uniform(-1, 1, n)  # sample y between -1 and 1
    r = np.sqrt(x**2 + y**2)  # absolute distance of point x,y from 0,0
    count_on_circle = np.sum(r <= 1)  # count x,y points that have r smaller or equal to 1 and lie on unit circle
    fraction = np.sum(count_on_circle)/float(n)  # this fraction is approx area_unit_circle/area_sample_space = pi/4
    return fraction*4


def random_device():
    """
    @rtype : int
    @return: if 3 consecutive heads occur one or more times payout is 1 else 0
    """
    sequence = ''
    count = 0
    payoff = 0
    for i in range(10):
        result = 'H' if uniform(0, 1) > 0.5 else 'T'
        sequence += result
        count = count + 1 if result == 'H' else 0
        if count == 3:
            payoff = 1
    print sequence + ' -> ' + ('1 dollar payoff!' if payoff == 1 else 'no payoff!')
    return payoff


def correlated_time_series(T, alpha, x_0=0):
    """
    @param T: time series length
    @param alpha: correlation coefficient
    @param x_0: initial x value
    @return: none
    """
    if not isinstance(alpha, list):
        alpha = [alpha]

    shocks = np.random.normal(size=(T, len(alpha)))
    x_values = np.zeros((T+1, len(alpha)))
    x_values[0] = x_0
    for t in np.arange(1, T+1):
        x_values[t] = alpha*x_values[t-1]+shocks[t-1]
    plot(x_values)
    legend(['alpha = '+str(val) for val in alpha])
    show()