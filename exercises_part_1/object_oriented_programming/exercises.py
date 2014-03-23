# coding=utf-8
from exercises_part_1.object_oriented_programming import my_classes as mc
from random import uniform

__author__ = 'stijn'

#region Exercise 1
print '\nExercise 1 - empirical cumulative distribution function (ecdf):'
samples = [uniform(0, 1) for i in range(10)]
F = mc.Ecdf(samples)
print "ecdf at x = 0.5 for n = 10 is "+str(F(0.5))
F.observations = [uniform(0, 1) for i in range(1000)]
print "ecdf at x = 0.5 for n = 1000 is "+str(F(0.5))
#endregion


#region Exercise 2
print '\nExercise 2 - polynomial class:'
coefficients = [1, 2, 3]
p = mc.Polynomial(coefficients)
print "P(x=2)= 1*2^0 + 2*2^1 + 3*2^2 is "+str(p(2))
p.diff()
print "P'(x=2)= 2*2^0 + 6*2^1 is "+str(p(2))
#endregion