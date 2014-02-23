from __future__ import division
# coding=utf-8
__author__ = 'stijn'


def p(x, coeff):
    """
    @param x: x value
    @param coeff: coefficients a_i of polynomial
    @return: sum(a_i*x^i)
    """
    if isinstance(coeff, list):
        return sum([c*x**i for i, c in enumerate(coeff)])
    else:
        return coeff*x


def num_of_caps(string):
    """
    @param string: some string
    @return: number of capitalised characters
    """
    # use lower instead of upper to successfully deal with characters that are not letters!
    return sum([char_normal != char_lower for char_normal, char_lower in zip(string, string.lower())])


def is_subset(seq_a, seq_b):
    """
    @param seq_a: sequence_a
    @param seq_b: sequence_b
    @return: True if sequence_a is subset of sequence_b else False
    """
    return sum([el for el in seq_a if el not in seq_b]) == 0


def linapprox(f, a, b, n, x):
    """
    @param f: function to approximate
    @param x,a,b: scalars evaluating point and end points a<=x<=b
    @param n: integer number of grid points
    @return: A float. The interpolant evaluated at x.
    """
    num_intervals = n - 1
    grid_spacing = (b-a)/num_intervals  # this division requires division from future import!
    point_2 = float(a)
    # point_2 is first grid point larger than x
    while point_2 <= b and point_2 <= x:
        point_2 += grid_spacing
    point_1 = point_2-grid_spacing
    return f(point_1) + (x-point_1)*(f(point_2)-f(point_1))/grid_spacing