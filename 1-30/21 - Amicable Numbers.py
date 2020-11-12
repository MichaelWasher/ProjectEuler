""" Problem 21 - Amicable numbers"""

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