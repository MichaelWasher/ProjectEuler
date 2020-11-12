""" Problem 38 - Pandigital Multiples """

# N > 1 and N <=9 due to digit limitations
MAX_MULTIPLIER = 9

def getMaxConcatProduct(number):
    concat_product = ""
    products = []
    for multiplier in range(1, MAX_MULTIPLIER + 1): 
        product = str(number * multiplier)
        products.append(product)
        concat_product += product
       
        if len(concat_product) == 9:
            return int(concat_product)

        if len(concat_product) > 9:
            return None
    
    return None



digit_options = ['9','8','7','6','5','4','3','2','1']

def checkMultiples(pandigital):

    for length_of_chars in range(2, len(pandigital)):
        first_num =  int(pandigital[:length_of_chars])
        expected_pandigital = str(getMaxConcatProduct(first_num))

        if expected_pandigital != None and  \
            expected_pandigital == pandigital:
            print(f'Pandigital: {str(pandigital)}')
            print(f'Seed: {str(first_num)}')
            return True

    return False

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
