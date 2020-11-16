"""
Problem 3 - Largest Prime Factors
-------------------------------------------------------------------------------
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import math


def getPrimeFactors(number):
    prime_numbers = []
    # Ignore even numbers
    while (number % 2 == 0):
        prime_numbers.append(number)
        number = number / 2

    # Every composite number has a proper factor less than or equal to its square root
    # http://sites.millersville.edu/bikenaga/number-theory/primes/primes.html
    for i in range(3, math.ceil(math.sqrt(number)), 2):

        # If n can be divided by i; i is a prime factor
        while number % i == 0:
            prime_numbers.append(i)
            number = number / i

    if number > 2:
        prime_numbers.append(2)

    return prime_numbers


number = 600851475143
print(max(getPrimeFactors(number)))
