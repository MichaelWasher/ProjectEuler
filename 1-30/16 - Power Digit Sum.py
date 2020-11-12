"""
Problem 16 - Power Digit Sum
-------------------------------------------------------------------------------
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
power_number = 2**1000
digit_sum = 0
for c in str(power_number):
    digit_sum += int(c)

print(digit_sum)
