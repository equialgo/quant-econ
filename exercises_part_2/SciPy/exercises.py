# coding=utf-8
import my_functions as mf
import numpy as np


__author__ = 'stijn'

#region Exercise 1
print '\nExercise 1 - recursive bisection algorithm:'
f = lambda x: np.sin(4 * (x - 0.25)) + x + x**20 - 1
print "The root of np.sin(4 * (x - 0.25)) + x + x**20 - 1 for x in [0 ,1] is " + \
      str(mf.bisect(f, 0, 1))
#endregion

