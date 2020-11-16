"""
Problem 11 - Largest product in a grid
-------------------------------------------------------------------------------
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
#TODO provided in resources
The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20×20 grid?
"""

from functools import reduce
import numpy as np
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCE_FOLDER = os.path.join(CURRENT_DIR, '../', 'resources')

# Variables
input_file_name = os.path.join(RESOURCE_FOLDER + '/' + '11_number_grid.txt')

grid = []
with open(input_file_name) as number_grid_file:
    while input_line := number_grid_file.readline():
        grid_row = [int(number_string) for number_string in input_line.split(" ")]
        grid.append(grid_row)

np_grid = np.array(grid)
adjacent_length = 4


# Helper functions
def getMaxForArray(number_array):
    local_max_product = 0
    local_max_adjacent_numbers = []
    while (len(number_array) >= adjacent_length):
        adjacent_numbers = number_array[0:adjacent_length]
        product = reduce(lambda a, b: a * b, adjacent_numbers)

        if (product > local_max_product):
            local_max_product = product
            local_max_adjacent_numbers = adjacent_numbers
        del number_array[0]

    return local_max_product


def getDiagonalOptions(local_grid):
    # Diagonal Right
    diagonal_np_grid = []
    for i in range(0, len(local_grid), 1):
        diagonal_np_grid.append(list(np.diag(local_grid[i:, 0:])))
        diagonal_np_grid.append(list(np.diag(local_grid[0:, i:])))

    # Drop all diags that are too short
    filtered_array = [diag_line for diag_line in diagonal_np_grid if len(diag_line) > adjacent_length]
    return filtered_array


# Challenge Script --------------------------------------------
# left / Right
max_horizontal_product = max(list(map(getMaxForArray, np_grid.tolist())))

# # Up/Down
# # Transpose the grid then use the same process
reverse_np_grid = np.array(grid).copy().transpose().tolist()
max_vertical_product = max(list(map(getMaxForArray, reverse_np_grid)))

# Get forward diagonal
diagonal_forard_np_grid = getDiagonalOptions(np_grid)
diagonal_forward_products = list(map(getMaxForArray, diagonal_forard_np_grid))
max_diagonal_forward_product = max(diagonal_forward_products)

# Get reverse diagonal by flipping x axis
reverse_np_grid = np.flip(np.array(grid).copy(), axis=1)
diagonal_reverse_np_grid = getDiagonalOptions(reverse_np_grid)
diagonal_reverse_products = list(map(getMaxForArray, diagonal_reverse_np_grid))
max_diagonal_reverse_product = max(diagonal_reverse_products)

# Print results for each.
print(f'Max Horizontal Product: {max_horizontal_product}')
print(f'Max Vertical Product: {max_vertical_product}')
print(f'Max Forward Diagonal Product: {max_diagonal_forward_product}')
print(f'Max Reverse Diagonal Product: {max_diagonal_reverse_product}')

max_adjacent_product = max(
    [max_horizontal_product, max_vertical_product, max_diagonal_forward_product, max_diagonal_reverse_product])
print(f'Max Adjacent Product: {max_adjacent_product}')
