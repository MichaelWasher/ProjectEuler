"""
Problem 40 - Champernowne's Constant
-------------------------------------------------------------------------------
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

# TODO Rewrite this to not require storing of all the digits and just add digits as they are divisible at index 10^n?
from functools import reduce
digits = []
MAX = 1_000_000

# Store all Digits
long_num = ""
digit_count= 0
for i in range(MAX+1):
    str_num = str(i)
    digit_count += len(str_num)
    digits.append(str_num)
    long_num += str_num


# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
i = 1
sum = 1
while(i < MAX):
    print(i)
    sum *= int(long_num[i])
    i *= 10

print(sum)