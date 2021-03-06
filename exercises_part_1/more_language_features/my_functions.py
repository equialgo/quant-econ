# coding=utf-8
__author__ = 'stijn'
from csv import reader


def fib(t):
    if t == 0:
        return 0
    elif t == 1:
        return 1
    else:
        return fib(t - 1) + fib(t - 2)


def column_iterator(target_file, column_number):
    f_handle = open(target_file, 'r')
    data = reader(f_handle)
    for row in data:
        yield row[column_number - 1]
    f_handle.close()


def line_sum(target_file):
    f_handle = open(target_file, 'r')
    line_sum = 0.0
    for line in f_handle:
        try:
            line_sum += float(line)
        except ValueError:
            pass
    f_handle.close()
    return line_sum
