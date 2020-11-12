"""Problem 22 - Name Scores"""
import re 
from functools import reduce
import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCE_FOLDER = os.path.join(CURRENT_DIR, '../', 'resources')

# Variables
input_file = os.join(RESOURCE_FOLDER + '/' + '22_names.txt')
names = []
name_character_values = []
name_scores = []

def getNameCharacterValue(str_name):
    sum = 0
    offset = -1 * ord('A') + 1
    for c in str_name:
        sum += ord(c) + offset
    return sum

# Read data and sort
pattern = re.compile('\"([A-Z]*)\"')
with open(input_file, 'r') as f:
    input_data = f.readline()
    names = pattern.findall(input_data)
    names.sort()

# Build the score arrays
for i in range(len(names)):
    name_character_values.append(getNameCharacterValue(names[i]))
    name_scores.append(name_character_values[i] * (i +1))

# Sum the scores
name_score_sum = sum(name_scores)
print(f'Sum of Name Scores: {name_score_sum}')