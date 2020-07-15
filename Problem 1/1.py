import functools 
sum3 = functools.reduce(lambda a,b: a + b, range(0, 1000, 3))
sum5 = functools.reduce(lambda a,b: a + b, range(0, 1000, 5))
sum15 = functools.reduce(lambda a,b: a + b, range(0, 1000, 15))
print("Result: " + str(sum3 + sum5 - sum15))