""" Problem 7 - 10001st Prime """
MAX_PRIME_INDEX = 10001
PRIME_FACTOR_MAX = 1_000_000

prime_numbers = [2]

# Prep the Boolean list for Sieve of Eratosthenes
prime_num_booleans = [True for i in range(0,PRIME_FACTOR_MAX+1)]
for i in range(2, PRIME_FACTOR_MAX+1, 2):
    prime_num_booleans[i] = False

# Prime Number Sieve
for num in range(3, PRIME_FACTOR_MAX+1, 2):
    if not prime_num_booleans[num]:
        continue

    prime_numbers.append(num)
    
    if(len(prime_numbers) == MAX_PRIME_INDEX):
        break
    
    # Clear all future numbers from being Prime
    for j in range(num*2, PRIME_FACTOR_MAX+1, num):
        prime_num_booleans[j] = False

print(prime_numbers[-1])
   