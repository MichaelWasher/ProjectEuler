""" Problem 43 - Sub-String Divisibility """
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

