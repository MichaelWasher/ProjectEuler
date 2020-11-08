# Circular Primes
# Configure Sieve
MAX = 1_000_000
prime_numbers = {
    2: True
}

# Prep the Boolean list for Sieve of Eratosthenes
is_prime = [True for i in range(0,MAX+1)]
# Populate even numbers
for i in range(4, MAX+1, 2):
    is_prime[i] = False

# Populate Odd Numbers
for num in range(3, MAX+1, 2):
    if not is_prime[num]:
        continue

    prime_numbers[num] = True
        
    # Clear all future numbers of sieve
    for j in range(num*2, MAX+1, num):
        is_prime[j] = False


circular_primes = {}

def rotate(num):
    str_num = str(num)
    str_num = str_num[-1] + str_num[:-1]
    return int(str_num)

def isCircularPrime(num):
    global circular_primes
    global prime_numbers

    if num in circular_primes:
        return True

    rotations = {}
    rotation = num
    for i in range(len(str(num))):
        rotation = rotate(rotation)
        rotations[rotation] = True
        
        if rotation not in prime_numbers:
            return False

    for key in rotations.keys():
        circular_primes[key] = True

    return True


for num in range(MAX + 1):
    isCircularPrime(num)

total_primes = 0
for key in circular_primes.keys():
    total_primes += 1
    print(key)

print(f'Total Primes: {total_primes}')
# print(circular_primes)
# print(prime_numbers)
