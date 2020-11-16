"""
Problem 30 - Digit fifth powers
-------------------------------------------------------------------------------
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

exponent = 5

# Find maximum search space
number_of_digits = 1
max_digits = 1
while (number_of_digits <= max_digits):
    number_of_digits += 1
    max_number = number_of_digits * (9 ** exponent)
    max_digits = len(str(max_number))

# ----------------------------------------------------------
# Start collecting Power numbers matching digits.
sum_of_all_numbers = 0
for test_number in range(2, int(max_number)):
    sum_of_digits = 0
    for char in str(test_number):
        sum_of_digits += int(char) ** exponent

    # Power number is the sum
    if sum_of_digits == test_number:
        # print(sum_of_digits)
        sum_of_all_numbers += sum_of_digits
        print(sum_of_all_numbers)
