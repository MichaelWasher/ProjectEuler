"""
Problem 22 - Name Scores
-------------------------------------------------------------------------------
Using names.txt [Provided `resources/22_names.txt`], a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import os
import re

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCE_FOLDER = os.path.join(CURRENT_DIR, '../', 'resources')

# Variables
input_file = os.path.join(RESOURCE_FOLDER + '/' + '22_names.txt')
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
    name_scores.append(name_character_values[i] * (i + 1))

# Sum the scores
name_score_sum = sum(name_scores)
print(f'Sum of Name Scores: {name_score_sum}')
