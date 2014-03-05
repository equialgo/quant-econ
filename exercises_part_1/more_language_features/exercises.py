__author__ = 'stijn'
import my_functions as m

#region Exercise 1
print '\nExercise 1 - First ten terms of fibonacci sequence:'
for i in range(10):
    print 'fib(n=%s) =' % i, m.fib(i)
#endregion

#region Exercise 2
print '\nExercise 2 - CSV column iterator:'
f = m.column_iterator("test_table.csv", 1)
print 'Iterate through date column; f = column_iterator("test_table.csv",1)'
for i in range(10):
    print 'f.next() = '+f.next()
#endregion

#region Exercise 3
print '\nExercise 3 - Sum lines of file:'
print 'Summing over "numbers.txt" results in '+str(m.line_sum('numbers.txt'))
#endregion


