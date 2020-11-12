"""
Problem 9 - Special Pythagorean triplet
-------------------------------------------------------------------------------
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from math import sqrt

COUNT = 1000

def calculateABC():

    for a in range(0,int(COUNT/2),1):
        for b in range(a+1,int(COUNT/2),1):
            c_squared = (a**2 + b**2)
            c = sqrt(c_squared)

            if(c.is_integer() and a+b+c == COUNT):
                return int(a), int(b), int(c)
    

a, b, c = calculateABC()

# Print the calculated values
print("A: " + str(a))
print("B: " + str(b))
print("C: " + str(c))
print("Product: " + str(a*b*c))
