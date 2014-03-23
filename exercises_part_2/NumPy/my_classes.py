from __future__ import division
__author__ = 'stijn'
import numpy as np
import matplotlib.pyplot as plt

class DiscreteRV(object):

    def __init__(self, q):
        self._q = np.asarray(q)
        self.Q = np.cumsum(q)

    def draws(self, k=1):
        return self.Q.searchsorted(np.random.rand(k))

    def get_q(self):
        return self._q

    def set_q(self, q):
        self._q = np.array(q)
        self.Q = np.cumsum(q)

    q = property(get_q, set_q)

class Ecdf(object):

    def __init__(self,observations):
        self.observations = np.asarray(observations)

    def __call__(self, x):
        return np.mean(self.observations<=x)

    def plot(self, a=None, b=None):
        if not a:
            a = self.observations.min() - self.observations.std()
        if not b:
            b = self.observations.max() + self.observations.std()

        x = np.linspace(a,b,num=100)
        f = np.vectorize(self.__call__)
        plt.plot(x, f(x))
        plt.show()