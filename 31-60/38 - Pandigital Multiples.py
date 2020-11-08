# Pandigital multiples
# N > 1 and N <=9 due to digit limitations
MAX_MULTIPLIER = 9
MAX_NUMBER = 999_999_999

def getMaxConcatProduct(number):
    concat_product = ""
    local_max_multiplier = 0
    products = []
    for multiplier in range(1, MAX_MULTIPLIER + 1): 
        product = str(number * multiplier)
        products.append(product)
        concat_product += product
       
        if len(concat_product) == 9:
            return int(concat_product), products

        if len(concat_product) > 9:
            print(products)
            print(len(concat_product))
            break
    
    return None, None

def isPandigital(str_num):
    str_len = len(str_num)
    if str_len > 9 or str_len < 9:
        return False

    digits = {}

    for c in str_num:
        digits[c] = True

    if len(digits) == 9 and 0 not in digits:
        return True
    else:
        return False


max_concat_product = 0
max_concat_products = []
max_used_number = 0

for number in range(1, MAX_NUMBER):
    concat_product, products = getMaxConcatProduct(number)
    if concat_product is None or not isPandigital(str(concat_product)):
        continue


    if concat_product > max_concat_product:
        max_concat_product = concat_product
        max_used_number = number
        max_concat_products = products

