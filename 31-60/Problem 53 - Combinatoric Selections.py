"""
Problem 53 - Combinatoric selections
-------------------------------------------------------------------------------

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 
.

In general, 
, where , , and .

It is not until , that a value exceeds one-million: .
How many, not necessarily distinct, values of 
 for , are greater than one-million?
"""

import math

# Populate factorial map up to 101
factorial_map = [0]*101
for i in range(101):
    factorial_map[i] = math.factorial(i)

def combinatorics(n, r):
    return int(factorial_map[n] / (factorial_map[r] * factorial_map[n-r]))

sum = 0
for n in range(1, 101):
    for r in range(1, 101):
        if combinatorics(n, r) > 1_000_000:
            print(f'N: {n} R: {r}')
            sum += 1 
print (sum)