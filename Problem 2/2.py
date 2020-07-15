# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
import pdb

low_pointer = 1
high_pointer = 2

sum = 0
tmp = 0

while (high_pointer < 4_000_000):

    # Perform Add
    if(high_pointer % 2 == 0):
        sum += high_pointer

    # Next value
    tmp = high_pointer
    high_pointer += low_pointer
    low_pointer = tmp


print(sum)
