""" Problem 47 - Distinct Primes Factors """
MAX = 1_000_000
DESIRED_PRIME_COUNT = 4

# Prep the Boolean list for Sieve of Eratosthenes
number_of_prime_factors = [0 for i in range(0,MAX+1)]
numbers_matching_desired_count = {}

# Iterate for Sieve
for num in range(2, MAX+1):
    if number_of_prime_factors[num] != 0:
        # Add number with matching primecount to hashmap
        if number_of_prime_factors[num] == DESIRED_PRIME_COUNT:
            numbers_matching_desired_count[num] = True

        continue
        
    # Clear all future numbers of
    for j in range(num*2, MAX+1, num):
        number_of_prime_factors[j] += 1


# look for consecutive numbers
for matching_num in numbers_matching_desired_count.keys():
    found = True
    for i in range(1, DESIRED_PRIME_COUNT):
       if (matching_num + i) not in numbers_matching_desired_count:
            found = False
            break
    
    if found: 
        print(matching_num)
        break
