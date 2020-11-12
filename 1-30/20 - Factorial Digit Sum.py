"""
Problem 20 - Factorial digit sum
-------------------------------------------------------------------------------
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
from functools import reduce
# Factorial digit sum
N = 100

n_factorial = reduce(lambda a, b: a * b, range(1,N+1, 1))
print(f'N Factorial: {n_factorial}')

digit_sum = 0
for c in str(n_factorial):
    digit_sum += int(c)

print(f'Digit Sum: {digit_sum}')