"""
Problem 52 - Permuted multiples
-------------------------------------------------------------------------------
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

# Sort numbers and then compare? O(nlogn)
# i = 125874
# print(sorted(str(i)))
i = 1

def compareNumbers(i, i2):
    str_i = str(i)
    str_i2 = str(i2)
    if len(str_i) != len(str_i2):
        return False
    
    str_i = sorted(str_i)
    str_i2 = sorted(str_i2)
    while len(str_i):
        if str_i.pop() != str_i2.pop():
            return False

    return True



while True:
    # Compare 2x
    if compareNumbers(i, i*2):
        if compareNumbers(i, i*3):
            if compareNumbers(i, i*4):
                print("Made it to 4")
                print(i)
                if compareNumbers(i, i*5):
                    print("Made it to 5")
                    print(i)
                    if compareNumbers(i, i*6):
                        print("Made it to 6")
                        print(i)
                        break
    i +=1
    
print(i)