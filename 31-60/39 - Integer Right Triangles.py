"""
Problem 39 - Integer Right Triangles
-------------------------------------------------------------------------------
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly
three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import math

MAX_P = 1000
solutions = {}
for p in range(MAX_P + 1):
    solutions[p] = 0

solutions[p] = 0

for left_side in range(1, MAX_P + 1):
    for bottom_side in range(1, left_side):
        hypotenuse = math.sqrt(left_side ** 2 + bottom_side ** 2)

        if hypotenuse != int(hypotenuse):
            continue

        perimeter = bottom_side + left_side + hypotenuse
        if perimeter > MAX_P:
            continue

        solutions[perimeter] += 1
        # print(f'L: {left_side} B: {bottom_side} H:{hypotenuse} ')
        solutions[p] += 1

max = 0
max_key = 0
for key in solutions.keys():
    value = solutions[key]
    if value > max:
        max = value
        max_key = key
        print(f'max {max}')
        print(f'key {max_key}')
