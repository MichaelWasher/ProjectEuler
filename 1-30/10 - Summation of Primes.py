"""
Problem 10 - Summation of primes
-------------------------------------------------------------------------------
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from functools import reduce

MAX = 2_000_000
prime_factors = [2]

# Prep the Boolean list for Sieve of Eratosthenes
prime_num_booleans = [True for i in range(0, MAX + 1)]
for i in range(2, MAX + 1, 2):
    prime_num_booleans[i] = False

# Iterate for Sieve
for num in range(3, MAX + 1, 2):
    if not prime_num_booleans[num]:
        continue

    prime_factors.append(num)

    # Clear all future numbers of
    for j in range(num * 2, MAX + 1, num):
        prime_num_booleans[j] = False

sum_of_primes = reduce(lambda x, y: x + y, prime_factors)
print("Primes: " + str(prime_factors))
print("Sum of Primes: " + str(sum_of_primes))
