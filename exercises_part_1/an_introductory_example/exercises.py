# coding=utf-8
from exercises_part_1.an_introductory_example import my_functions as m

__author__ = 'stijn'

#region Exercise 1
print '\nExercise 1 - factorial:'
for i in range(10):
    print 'factorial(n=%s) =' % i, m.factorial(i)
#endregion

#region Exercise 2
print '\nExercise 2 - binonial random variable:'
for i in range(10):
    p = i/float(10)
    print 'binomial_rv(n=10, p=%.1f' % p, ') = ', m.binomial_rv(10, p)
#endregion

#region Exercise 3
print '\nExercise 3 - Monte Carlo pi approximation:'
for i in range(6):
    n = 10**(i+1)
    print 'pi_mc_approx(n=%s)' % n, m.pi_mc_approx(n)
#endregion

#region Exercise 4
print '\nExercise 4 - Random payoff device:'
for i in range(10):
    m.random_device()
#endregion

#region Exercise 5
print '\nExercise 5 - Correlated time series:'
T = 200
alpha = 0.9
m.correlated_time_series(T, alpha)
#endregion

#region Exercise 6
print '\nExercise 6 - Multiple correlated time series:'
alpha = [0, 0.8, 0.98]
m.correlated_time_series(200, alpha)
#endregion