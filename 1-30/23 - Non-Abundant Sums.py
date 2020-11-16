"""
Problem 23 - Non-Abundant Sums
-------------------------------------------------------------------------------

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
# NOTE: Needs re-writing. This algorithm will not scale well due to n^2

MAX_NUMBER = 28123
# All numbers are marked with 0 divisors
number_of_divisors = [0 for i in range(0, MAX_NUMBER + 1)]
divisor_chains = [[] for i in range(0, MAX_NUMBER + 1)]
divisor_sums = [0 for i in range(0, MAX_NUMBER + 1)]

# Build Block of all divisors
for num in range(1, MAX_NUMBER + 1):
    for j in range(num * 2, MAX_NUMBER + 1, num):
        number_of_divisors[j] += 1
        divisor_chains[j].append(num)
        divisor_sums[j] += num

deficient_numbers = {}
abundant_numbers = {}
perfect_numbers = {}
for i in range(MAX_NUMBER + 1):
    if i > divisor_sums[i]:
        deficient_numbers[i] = divisor_sums[i]
    if i < divisor_sums[i]:
        abundant_numbers[i] = divisor_sums[i]
    if i == divisor_sums[i]:
        perfect_numbers[i] = divisor_sums[i]


# Find Pair ---------------------------------------
def findPair(test_value):
    for i in range(test_value + 1):
        if i not in abundant_numbers:
            continue

        if (test_value - i) in abundant_numbers:
            # Early Break
            # Pair found
            # return i, test_value-i
            return False
    return True


sum = 0
for i in range(1, MAX_NUMBER + 1):
    if findPair(i):
        sum += i
print(sum)
