# Truncatable Primes
# Configure Sieve
MAX = 1_000_000
prime_numbers = {
    2: True
}
truncatable_primes ={
}

def pop(str_value):
    # str_value = str(int_value)
    # str_value = str_value[1:]
    # return int(str_value)
    return str_value[1:]

def dequeue(str_value):
    # str_value = str(int_value)
    # str_value = 
    # return int(str_value)
    return str_value[:-1]

def isTruncatable(prime):
    if prime < 10 or prime not in prime_numbers:
        return False
    
    tmp_prime = str(prime)
    while tmp_prime != "":
        if int(tmp_prime) not in prime_numbers:
            return False
        tmp_prime = pop(tmp_prime)

    tmp_prime = str(prime)
    while tmp_prime != "":
        if int(tmp_prime) not in prime_numbers:
            return False
        tmp_prime = dequeue(tmp_prime)

    return True


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


for prime in prime_numbers.keys():
    if isTruncatable(prime):
        truncatable_primes[prime] = True


print(f'Truncatable Primes Found: {truncatable_primes}')
print(f'Sum of primes found: {sum(truncatable_primes.keys())}')

