"""
Problem 15 - Lattice Paths
-------------------------------------------------------------------------------
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly
6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
GRID_WIDTH = 20
GRID_HEIGHT = 20

grid_path_lengths = {}

def recursivePathFinder(x, y):
    # Memoize - If seen point before, we know how many paths from here to end.
    if (x,y) in grid_path_lengths:
        return grid_path_lengths[(x,y)]

    if x == GRID_WIDTH and y == GRID_HEIGHT:
        return 1

    routes = 0
    if x != GRID_WIDTH: # Go Right
        routes += recursivePathFinder(x+1, y)
    
    if y != GRID_HEIGHT: # Go Down
        routes += recursivePathFinder(x, y+1)
    
    grid_path_lengths[(x,y)] = routes
    return routes

print(recursivePathFinder(0,0))