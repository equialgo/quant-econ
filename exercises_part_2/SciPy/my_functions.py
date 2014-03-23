# coding=utf-8
__author__ = 'stijn'


def bisect(f, a, b, tol=10e-5):
    mid = 0.5*(b+a)
    if b-a < tol:
        return mid
    else:
        if f(mid) < 0:
            return bisect(f, mid, b, tol)
        else:
            return bisect(f, a, mid, tol)
