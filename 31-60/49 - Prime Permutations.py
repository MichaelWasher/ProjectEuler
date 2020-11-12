""" Problem 49 - Prime Permutations """
MAX_PRIME_INDEX = 10_000
PRIME_FACTOR_MAX = 10_000
prime_numbers = [2]
# Prep the Boolean list for Sieve of Eratosthenes
prime_num_booleans = [True for i in range(0, PRIME_FACTOR_MAX + 1)]
for i in range(2, PRIME_FACTOR_MAX + 1, 2):
    prime_num_booleans[i] = False

# Prime Number Sieve
for num in range(3, PRIME_FACTOR_MAX + 1, 2):
    if not prime_num_booleans[num]:
        continue

    prime_numbers.append(num)

    if (len(prime_numbers) == MAX_PRIME_INDEX):
        break

    # Clear all future numbers from being Prime
    for j in range(num * 2, PRIME_FACTOR_MAX + 1, num):
        prime_num_booleans[j] = False


def isPermutation(input1, input2):
    # assumes numerical order of input
    used_digit = [0 for i in range(10)]

    for digit in str(input1):
        used_digit[int(digit)] +=1

    for digit in str(input2):
        used_digit[int(digit)] -= 1

    return max(used_digit) == 0

# permutations = createPermutations("", ['1','4','8','7'])
# print(permutations)

viable_primes = {}
for prime in prime_numbers:
    if 10_000 > prime > 999:
        viable_primes[prime] = True


for prime in viable_primes.keys():
    # print(prime)
    prime_count = 0
    first_addition = prime+3330
    second_addition = prime + 6660
    if first_addition in viable_primes:
        if second_addition in viable_primes:
            if isPermutation(first_addition, second_addition):
                if isPermutation(first_addition, prime):
                    print("----------------")
                    print(prime)
                    print(first_addition)
                    print(second_addition)
                    print("----------------")
    # permutations = createPermutations("", list(str(prime)))
    # # print(permutations)
    # for perm in permutations:
    #     # print (int(perm))
    #     if int(perm) in viable_primes:
    #         # print(perm)
    #         prime_count += 1
    # if prime_count > 2:
    #     print(prime_count)
# # Check Prime numbers ag
#ainst eachother for permutations
296962999629
