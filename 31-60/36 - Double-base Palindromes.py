"""
Problem 36 - Double-base palindromes
-------------------------------------------------------------------------------
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
# Double-base palindromes
# Variables ----------------------------
MAX = 1_000_000
double_palindromes = []


# Helper Functions -----------------------------------------
def isPalindromic(string_value):
    for i in range(0, int((len(string_value) + 1) / 2)):
        if string_value[i] != string_value[(i + 1) * -1]:
            return False
    return True


# Script Functions -----------------------------------------
for num in range(MAX + 1):
    if not isPalindromic(str(num)):
        continue
    bin_num = bin(num)
    str_bin_num = str(bin_num)[2:]

    if isPalindromic(str_bin_num):
        double_palindromes.append(num)

print(f'Double Palindromes: {double_palindromes}')

# Calculate Sum
print(f'Sum: {sum(double_palindromes)}')
