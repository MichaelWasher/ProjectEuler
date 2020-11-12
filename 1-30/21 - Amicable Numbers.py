"""
Problem 21 - Amicable numbers
-------------------------------------------------------------------------------
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

MAX_NUMBER = 30_000
# All numbers are marked with 0 divisors
number_of_divisors = [0 for i in range(0, MAX_NUMBER+1)]
divisor_chains = [[] for i in range(0, MAX_NUMBER+1)]
divisor_sums = [0 for i in range(0, MAX_NUMBER+1)]

# Build Block of all divisors
for num in range(1, MAX_NUMBER+1):
    # Clear all future numbers from being Prime
    for j in range(num*2, MAX_NUMBER+1, num):
        number_of_divisors[j] += 1
        divisor_chains[j].append(num)
        divisor_sums[j] += num

amicable_numbers = {}
for i in range(10_000+1):
    amicable_item_1 = i
    amicable_item_2 = divisor_sums[i]

    if divisor_sums[amicable_item_2] == amicable_item_1 and amicable_item_1 != amicable_item_2:
        amicable_numbers[amicable_item_1] = True
        amicable_numbers[amicable_item_2] = True

sum = 0
for key in amicable_numbers.keys():
    sum += key
print(amicable_numbers)
print(sum)