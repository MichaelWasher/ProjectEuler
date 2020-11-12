"""
Problem 24 - Lexicographic Permutations
-------------------------------------------------------------------------------
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
# Lexicographic permutations
possible_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutation_count = 0
# Iterate all permutations of input and sort
# recursively use the numbers to maintain state
def createPermutation(input_values, used_values):
    backup_input_values = input_values.copy()
    global permutation_count

    if permutation_count == 1_000_000:    
        return

    if(len(input_values) ==0):
        permutation_count +=1

    if permutation_count == 1_000_000:
        # output the value
        print("".join(map(str, used_values)))
    
    # assumes numerical order of input
    for index in range(len(input_values)):
        used_values.append(input_values.pop(index))
        createPermutation(input_values, used_values)
        used_values.pop()
        input_values = backup_input_values.copy()
        

permutations = []
createPermutation(possible_values, [])