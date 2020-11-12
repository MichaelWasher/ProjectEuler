"""
Problem 34 - Digit factorials
-------------------------------------------------------------------------------
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
# Digit factorials
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Helper Functions
def factorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    return factorial

def findMaxSearchSpace():    
    number_of_digits = 1
    max_digits = 1
    while (number_of_digits <= max_digits):
        number_of_digits += 1 
        max_number =  number_of_digits * factorial(9)
        max_digits = len(str(max_number))
    
    return max_number

#----------------- Script Start
# Populate a Factorial Lookup table for better performance
factorial_lookup = {}
for i in range(10):
    factorial_lookup[str(i)] = factorial(i)

# Find the search space
max_number = findMaxSearchSpace()

factorial_sums = 0
numbers_matching_pattern = []
for num in range(3, max_number+1):
    # check that sum of digits factorial
    num_factorial_digit_sum = 0
    for c in str(num):
        num_factorial_digit_sum += factorial_lookup[c]

    if num_factorial_digit_sum == num:
        numbers_matching_pattern.append(num)
        factorial_sums += num


# Output Results
print(f'Numbers matching the pattern:')
print(numbers_matching_pattern)
print("Sum of all numbers: " + str(factorial_sums))