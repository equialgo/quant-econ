# coding=utf-8
__author__ = 'stijn'

import numpy as np


def p(x, coeff):
    c = np.array(coeff)
    xs = np.concatenate(([1], np.cumprod(np.ones(c.size-1)*x)))  # xs = [1, x, x**2, ...]
    return np.dot(xs, c)

