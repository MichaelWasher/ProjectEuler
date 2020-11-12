"""
Problem 32 - Pandigital products
-------------------------------------------------------------------------------
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
MAX_MULTIPLIER = 9
# Build factors sieve of numbers up to 100_000
digit_options = ['1','2','3','4','5','6','7','8','9']
product_sum = 0
products = {}
def checkMultiples(pandigital):
    global product_sum
    for i in range(1, 5):
        for j in range(1, 6-i):
            if i + j > 5:
                continue
            tmp_pandigital = pandigital
            # Check multiples now
            multiplicand = int(tmp_pandigital[:i])
            tmp_pandigital = tmp_pandigital[i:]

            multiplier = int(tmp_pandigital[:j])
            tmp_pandigital = tmp_pandigital[j:]

            product = int(tmp_pandigital)
            if multiplicand * multiplier == product:
                products[product] = True
                print(f'{multiplicand} * {multiplier} = {tmp_pandigital}')
                return True
    return False

# test_pandigital = 391867254
# checkMultiples(str(test_pandigital))

#
def getPandigitalNumbers(test_pandigital, digit_options):
    digit_count = len(digit_options)
    # Perform checks on pandigital numbers
    if digit_count == 0:
        checkMultiples(test_pandigital)
        return

    # for each digit recur
    for i in range(digit_count):
        tmp_value = digit_options.pop(i)
        getPandigitalNumbers(test_pandigital + tmp_value, digit_options)
        digit_options.insert(i, tmp_value)

    return

getPandigitalNumbers("", digit_options)

# Remove duplicates with hashmap
for product in products.keys():
    product_sum += product

print(product_sum)