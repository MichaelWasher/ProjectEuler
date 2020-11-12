"""
Problem 14 - Longest Collatz sequence
-------------------------------------------------------------------------------
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""
# Variables --------------------------------
MAX_NUMBER = 1_000_000
collatz_length = {}

# Helper Functions --------------------------------
def generateCollatz(i):
    if i == 1:
        return 1

    # Memoize completed answers
    if i in collatz_length:
        return collatz_length[i]

    if i % 2 == 0:
        length = generateCollatz(i/2)
    else:
        length = generateCollatz(3*i + 1)
    
    # Store Result
    collatz_length[i] = length + 1

    return collatz_length[i]

# Main Script --------------------------------
max_length = 0
max_starter = 0
for i in range(1, MAX_NUMBER+1):
    length = generateCollatz(i)
    
    if length > max_length:
        max_length = length
        max_starter = i

print(f'Max Started: {str(max_starter)}')
print(f'Max Length: {str(max_length)}')

