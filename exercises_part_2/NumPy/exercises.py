# coding=utf-8
from exercises_part_2.NumPy import my_functions as mf
from exercises_part_2.NumPy import my_classes as mc
import numpy as np

__author__ = 'stijn'

#region Exercise 1
print '\nExercise 1 - polynomial sum:'
print "p(2,[1, 2, 3])= 1*2^0 + 2*2^1 + 3*2^2 is "+str(mf.p(2, [1, 2, 3]))
#endregion

#region Exercise 2
print '\nExercise 2 - Discrete random variable generator:'
RV = mc.DiscreteRV([0.25, 0.50, 0.25])
print 'mean of 100 draws from discrete RV with q = [.25, .50, .25] is '+str(np.mean(RV.draws(100)))
print 'this should be close to expected value of 0.25*0 + 0.50*1 +0.25*2 = 1'
#endregion

#region Exercise 3
print '\nExercise 3 - Cumulative distribution function approximation:'
F = mc.Ecdf(np.random.randn(100))
print 'approximate of F(0) = P(x<=0) for x ~ N(0,1) based on 100 observations is '+str(F(0))
print 'see plot for F(x) for x in [-2,2]'
F.plot(-2, 2)
#region