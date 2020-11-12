"""
Problem 43 - Sub-String Divisibility
-------------------------------------------------------------------------------
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

digit_options = ['0', '1','2','3','4','5','6','7','8','9']
pandigitals = {}
primes = [2,3,5,7,11,13,17]
substring_length = 3

def getPandigitalNumbers(test_pandigital, digit_options, first):
    digit_count = len(digit_options)
    # Perform checks on pandigital numbers
    if digit_count == 0:
        pandigitals[test_pandigital] = True
        return

    # for each digit recur
    if first:
        skip_zero = 1
    else:
        skip_zero = 0

    for i in range(skip_zero, digit_count):
        tmp_value = digit_options.pop(i)
        getPandigitalNumbers(test_pandigital + tmp_value, digit_options, False)
        digit_options.insert(i, tmp_value)

    return

def getTriplet(i, pandigital):
    tmp = pandigital[i:]
    return int(tmp[:substring_length])

def checkSubStringDivisibility(pandigitial):

    for i in range(len(pandigitial) - substring_length):
        triplet = getTriplet(i+1, pandigitial)
        # print(triplet)
        if triplet % primes[i] != 0:
            return False

    return True

pd_sum = 0
getPandigitalNumbers("", digit_options, True)
for pandigital in pandigitals.keys():
    if checkSubStringDivisibility(pandigital):
        pd_sum += int(pandigital)

print(pd_sum)

