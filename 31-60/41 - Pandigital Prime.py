""" 41 - Pandigital Primes"""
import math
# Create Sieve for all Primes up to sqrt(n)
MAX_PANDIGITAL_NUMBER = 987_654_321
MAX_PRIME = int(math.sqrt(MAX_PANDIGITAL_NUMBER)) +1
# Prep the Boolean list for Sieve of Eratosthenes
prime_num_booleans = [True for i in range(0, MAX_PRIME + 1)]
prime_numbers = [2]
digit_options = ['9','8','7','6','5','4','3','2','1']

for i in range(2, MAX_PRIME + 1, 2):
    prime_num_booleans[i] = False

# Prime Number Sieve
for num in range(3, MAX_PRIME + 1, 2):
    if not prime_num_booleans[num]:
        continue

    prime_numbers.append(num)

    # Clear all future numbers from being Prime
    for j in range(num * 2, MAX_PRIME + 1, num):
        prime_num_booleans[j] = False


def isPrime(test_prime):
    for test_prime_factor in prime_numbers:
        if int(test_prime) % int(test_prime_factor) == 0:
            # print(f'{test_prime} % {test_prime_factor} == 0')
            return False
    return True

def getPandigitalNumbers(test_pandigital, digit_options):
    digit_count = len(digit_options)
    # Perform checks on pandigital numbers
    if digit_count == 0:
        # checkMultiples(test_pandigital)
        # print(test_pandigital)
        if isPrime(test_pandigital):
            print(test_pandigital)
        return

    # for each digit recur
    for i in range(digit_count):
        tmp_value = digit_options.pop(i)
        getPandigitalNumbers(test_pandigital + tmp_value, digit_options)
        digit_options.insert(i, tmp_value)

    return


for i in range(1, 10):
    getPandigitalNumbers("", [str(j) for j in range(1, i+1)])
