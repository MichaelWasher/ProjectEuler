""" Problem 12 - Highly divisible triangular number"""
from functools import reduce

PRIME_FACTOR_MAX = 50
DESIRED_DIVISOR_COUNT = 500
prime_factors = [2]

# Find the first 10_000 primes
# Prep the Boolean list for Sieve of Eratosthenes
prime_num_booleans = [True for i in range(0,PRIME_FACTOR_MAX+1)]
for i in range(2, PRIME_FACTOR_MAX+1, 2):
    prime_num_booleans[i] = False

# Prime Number Sieve
for num in range(3, PRIME_FACTOR_MAX+1, 2):
    if not prime_num_booleans[num]:
        continue

    prime_factors.append(num)
        
    # Clear all future numbers from being Prime
    for j in range(num*2, PRIME_FACTOR_MAX+1, num):
        prime_num_booleans[j] = False

# Use prime factorization to work with up to MAX
# Count in Triangle Numbers looking at divisor counts
def calculateDivisors(number):
    if number in prime_factors: 
            return 1
    
    sum_prime_exponents = {}
    
    for prime in prime_factors:
        tmp_number = number

        if prime > tmp_number:
            break

        prime_exponent = 0
        while(tmp_number % prime == 0):
            tmp_number /= prime
            prime_exponent += 1

        sum_prime_exponents[prime] = prime_exponent + 1
        # print(f'Prime: {prime} Exponent: {sum_prime_exponents[prime]}')
        # Chop the numbers with primes
    
    total_divisors = 1
    for key in sum_prime_exponents.keys():
        total_divisors *= sum_prime_exponents[key]

    return total_divisors

# print(calculateDivisors(76576500))
triangle_number = 0
i = 0
while(True):
    i += 1
    triangle_number += i
    if calculateDivisors(triangle_number) >= DESIRED_DIVISOR_COUNT:
        print(triangle_number)
        break
