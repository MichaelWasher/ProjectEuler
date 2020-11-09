"""Problem 14 - Longest Collatz sequence"""
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

