"""
Problem 1 - Multiples of 3 and 5
-------------------------------------------------------------------------------
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import functools

sum3 = functools.reduce(lambda a,b: a + b, range(0, 1000, 3))
sum5 = functools.reduce(lambda a,b: a + b, range(0, 1000, 5))
sum15 = functools.reduce(lambda a,b: a + b, range(0, 1000, 15))
print("Result: " + str(sum3 + sum5 - sum15))