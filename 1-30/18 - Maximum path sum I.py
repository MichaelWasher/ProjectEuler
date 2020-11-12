"""
Problem 18 - Maximum Path Sum I
-------------------------------------------------------------------------------
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top
 to bottom is 23.
[Provided in resources/18_short_input.txt]

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
[Provided in resources/18_long_input.txt]

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
"""
import os

graph = {}

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCE_FOLDER = os.path.join(CURRENT_DIR, "../resources")

# Setup Data Input
short_input = os.path.join(RESOURCE_FOLDER, "18_short_input.txt")
long_input = os.path.join(RESOURCE_FOLDER, "18_long_input.txt")
extra_long_input = os.path.join(RESOURCE_FOLDER, "67_triangle.txt")

input_file = extra_long_input
path = []


def createNode(node_value, left=None, right=None):
    return {'value': int(node_value), 'left': left, 'right': right, 'distance_to_end': None}


# Build the Graph
with open(input_file) as f:
    input_lines = f.readlines()

    for line_index, line in enumerate(input_lines):
        line_items = line.strip().split(" ")

        for item_index, node_value in enumerate(line_items):
            graph[(line_index, item_index)] = createNode(node_value)

            # Root
            if line_index == 0:
                continue

            line_above = line_index - 1
            # !Leftmost
            if item_index != 0:
                parent_node = graph[(line_above, item_index - 1)]
                parent_node['right'] = (line_index, item_index)

            # !Rightmost
            if item_index != len(line_items) - 1:
                parent_node = graph[(line_above, item_index)]
                parent_node['left'] = (line_index, item_index)


def findOptimalPath(node_index):
    node = graph[node_index]

    # Encoutered node before
    if node['distance_to_end'] != None:
        print("Distance Found")
        return node['distance_to_end']

    # Child is Missing ( NOTE: This is intended to drop for missing children )
    if node['left'] == None or node['right'] == None:
        return node['value']

    # Calculate Children
    left_child_dist = findOptimalPath(node['left'])
    right_child_dist = findOptimalPath(node['right'])
    # Get Max
    max_dist = max(left_child_dist, right_child_dist)
    # Memoize
    node['distance_to_end'] = max_dist + node['value']
    return node['distance_to_end']


print(findOptimalPath((0, 0)))
