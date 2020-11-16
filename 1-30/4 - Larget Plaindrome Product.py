"""
Problem 4 - Largest palindrome product
-------------------------------------------------------------------------------
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def checkPalindrome(value):
    string_value = str(value)
    for i in range(0, int((len(string_value) + 1) / 2)):
        if string_value[i] != string_value[(i + 1) * -1]:
            return False

    return True


def findFactorsOfPalindrome():
    max = 0
    max_x = 0
    max_y = 0
    for x in range(999, 0, -1):
        for y in range(x, 999, 1):
            result = checkPalindrome(x * y)
            if result:
                if x * y > max:
                    max = x * y
                    max_x = x
                    max_y = y
    return max, max_x, max_y


palindrome, x, y = findFactorsOfPalindrome()
print("X = " + str(x))
print("Y = " + str(y))
print("Palindrome = " + str(palindrome))
