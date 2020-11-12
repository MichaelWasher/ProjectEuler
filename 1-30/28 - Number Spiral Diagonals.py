"""
Problem 28 - Number Spiral Diagonals
-------------------------------------------------------------------------------
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
# Number spiral diagonals
max_width = 1001

diagonals_sum = 0

for line_width in range(max_width, 1, -2):
    corner_gap = line_width -1

    top_right = line_width ** 2
    top_left = top_right - corner_gap
    bottom_left = top_left - corner_gap
    bottom_right = bottom_left - corner_gap

    # Add all corners to Diagonals
    diagonals_sum += top_right + top_left + bottom_left + bottom_right

# Deal with edge case of width 1
diagonals_sum +=1

print(f'Diagonal Sums: {diagonals_sum}')
