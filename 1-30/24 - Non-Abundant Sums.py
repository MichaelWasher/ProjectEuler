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