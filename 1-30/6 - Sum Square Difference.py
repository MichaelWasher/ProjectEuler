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