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
