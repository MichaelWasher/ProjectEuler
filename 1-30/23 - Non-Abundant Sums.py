""" Problem 23 - Non-Abundant Sums"""
# NOTE: Needs re-writing. This algorithm will not scale well due to n^2

MAX_NUMBER = 28123
# All numbers are marked with 0 divisors
number_of_divisors = [0 for i in range(0, MAX_NUMBER+1)]
divisor_chains = [[] for i in range(0, MAX_NUMBER+1)]
divisor_sums = [0 for i in range(0, MAX_NUMBER+1)]

# Build Block of all divisors
for num in range(1, MAX_NUMBER+1):
    for j in range(num*2, MAX_NUMBER+1, num):
        number_of_divisors[j] += 1
        divisor_chains[j].append(num)
        divisor_sums[j] += num

deficient_numbers = {}
abundant_numbers = {}
perfect_numbers = {}
for i in range(MAX_NUMBER+1):
    if i > divisor_sums[i]:
        deficient_numbers[i] = divisor_sums[i]
    if i < divisor_sums[i]:
        abundant_numbers[i] = divisor_sums[i]
    if i == divisor_sums[i]:
        perfect_numbers[i] = divisor_sums[i]

# Find Pair ---------------------------------------
def findPair(test_value):
    for i in range(test_value+1):
        if i not in abundant_numbers:
            continue

        if (test_value - i) in abundant_numbers:
            # Early Break
            # Pair found
            # return i, test_value-i
            return False
    return True


sum = 0
for i in range(1, MAX_NUMBER+1):
    if findPair(i):
        sum += i
print(sum)
