from functools import reduce
# Factorial digit sum
N = 100

n_factorial = reduce(lambda a, b: a * b, range(1,N+1, 1))
print(f'N Factorial: {n_factorial}')

digit_sum = 0
for c in str(n_factorial):
    digit_sum += int(c)

print(f'Digit Sum: {digit_sum}')