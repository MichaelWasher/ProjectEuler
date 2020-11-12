"""
Problem 27 - Quadratic Primes
-------------------------------------------------------------------------------
Euler discovered the remarkable quadratic formula:

[ TODO Add infromation for images?]
It turns out that the formula will produce 40 primes for the consecutive integer values . However, when  is divisible by 41, and certainly when  is clearly divisible by 41.

The incredible formula  was discovered, which produces 80 primes for the consecutive values . The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
, where  and
where  is the modulus/absolute value of
e.g.  and
Find the product of the coefficients,  and , for the quadratic expression that produces the maximum number of primes for consecutive values of , starting with .
"""
# Quadratic Primes

import pdb
# ------------- Prime Machine
MAX = 50_000
prime_factors = [2]

# Prep the Boolean list for Sieve of Eratosthenes
prime_num_booleans = [True for i in range(0,MAX+1)]
for i in range(2, MAX+1, 2):
    prime_num_booleans[i] = False

# Iterate for Sieve
for num in range(3, MAX+1, 2):
    if not prime_num_booleans[num]:
        continue

    prime_factors.append(num)
        
    # Clear all future numbers of
    for j in range(num*2, MAX+1, num):
        prime_num_booleans[j] = False
# ---------------------------------------

# Check against the primes in prime_num_booleans
max_a, max_b, max_n, max_prime = 0, 0, 0, 0

def updateMax(a, b, n, prime_test):
    global max_a
    global max_b
    global max_n
    global max_prime
    if (n > max_n):
        max_a = a
        max_b = b
        max_n = n
        max_prime = prime_test

# a < 100 and b <= 1000
for a in range(-1000, 1000):
    for b in range(-1001, 1001):
        
        # if b is not prime then n == 0 will always fail
        if not prime_num_booleans[b]:
            continue
            
        n = 0
        prime_run = True
        while(prime_run):
            prime_test = n**2 + a*n + b

            # Check if is actually a prime
            if not prime_num_booleans[prime_test]:
                prime_run = False
                continue
                    
            updateMax(a, b, n, prime_test)
            n += 1


# Output results
print("Most efficient values presented below:")
print(f'a: {str(max_a)}')
print(f'b: {str(max_b)}')
print(f'n: {str(max_n)}')
print(f'Max Prime provided: {str(max_prime)}')
print(f'Equation is: n^2 + {str(max_a)}*n + {str(max_b)} for n < {str(max_n)}')


