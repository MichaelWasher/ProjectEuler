"""
Problem 6 - Sum square difference
-------------------------------------------------------------------------------
TODO REPLACE this with real comment
The sum of the squares of the first ten natural numbers is,
The square of the sum of the first ten natural numbers is,
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
from functools import reduce

COUNT = 100

def squareOfSums():
    return reduce(lambda a, b: a + b, range(0,COUNT+1,1)) ** 2

def sumOfSquares():
    sum = 0
    for i in range(0,COUNT+1,1):
        sum += i**2
    return sum


sumSquares = sumOfSquares()
squareSums = squareOfSums()

print("Sum of Squares: " + str(sumSquares))
print("Square of Sums: " + str(squareSums))

print("Difference: " + str(squareSums - sumSquares))