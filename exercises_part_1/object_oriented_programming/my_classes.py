from __future__ import division
__author__ = 'stijn'
import numpy as np


class Ecdf(object):

    def __init__(self, observations):
        self.observations = observations

    def __call__(self, x):
        X = np.array(self.observations)
        return np.sum(X <= x)/X.size


class Polynomial(object):

    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        p_x = 0
        for i,a in enumerate(self.coeff):
            p_x += a*x**i
        return p_x

    def diff(self):
        if len(self.coeff) == 1:
            self.coeff = [0]
        else:
            new_coeff = []
            for i, a in enumerate(self.coeff[1:]):
                new_coeff.append((i+1)*a)
            self.coeff = new_coeff