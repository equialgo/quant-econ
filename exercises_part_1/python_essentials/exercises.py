# coding=utf-8
from exercises_part_1.python_essentials import my_functions as m

__author__ = 'stijn'

#region Exercise 1
print '\nExercise 1_1 - Inner product x_vals, y_vals:'
x_vals = [2, 3]
y_vals = [3, 4]
inner_prod = sum(x*y for x, y in zip(x_vals, y_vals))
print 'The inner product of x_vals = {0} and y_vals = {1} is {2}.'.format(x_vals, y_vals, inner_prod)
num_even = sum([num % 2 == 0 for num in range(100)])
print '\nExercise 1_2 - The number of even numbers in 0,...,99 is {0}.'.format(num_even)
pairs = ((2, 5), (4, 2), (9, 8), (12, 10))
even_pairs = sum([a % 2 == 0 and b % 2 == 0 for a, b in pairs])
print '\nExercise 1_2 - The number of pairs with even numbers in {0} is {1}.'.format(pairs, even_pairs)
#endregion

#region Exercise 2
print '\nExercise 2 - Polynomial sum coeff_i * x^i:'
coeff = [1, 2, 3]
for x in range(10):
    print 'p(x={0}, coeff={1}) = {2}.'.format(x, coeff, m.p(x, coeff))
#endregion

#region Exercise 3
print '\nExercise 3 - Count number of capitalized chars in string:'
string = "Some chars are in CAMEL CASE!"
print 'The number of caps in "{0}" is {1}'.format(string, m.num_of_caps(string))
#endregion

#region Exercise 4
print '\nExercise 4 - Determine if sequence_a is subset of sequence_b:'
seq_a = 'bla'
seq_b = 'bladiebla'
print 'm.is_subset(seq_a="{0}",seq_b"{1}"): {2}'.format(seq_a, seq_b, m.is_subset(seq_a,seq_b))
#endregion


#region Exercise 5
print '\nExercise 5 - Piecewise linear approximation:'
for n in range(2,11):
    print 'm.linapprox(f=lambda x : x**2, a=2, b=4, n={0}, x=2.7): {1}'.format(n, m.linapprox(lambda x : x**2,
                                                                                           2, 4, n, 2.7))
print 'The true value is: '+str(2.7**2)
#endregion