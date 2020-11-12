""" Problem 42 - Coded Triangle Numbers"""
import os
import re

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCE_FOLDER = os.path.join(CURRENT_DIR, '../', 'resources')
input_file = os.path.join(RESOURCE_FOLDER, '42_words.txt')

def getCharacterValue(input_string):
    sum = 0
    # ASCII Offset
    offset = -1 * ord('A') + 1
    for c in input_string:
        sum += ord(c) + offset
    return sum

# Injest the WordList from Resources
# Keep length of longest word
pattern = re.compile('\"([A-Z]*)\"')
with open(input_file, 'r') as f:
    input_data = f.readline()
    words = pattern.findall(input_data)
    max_word_length = max([len(word) for word in words])

print(words)

# Max Triangle Number Required will be 26 * length_of_word; Due to Alpha -> Number conversion
max_triangle_number = 26 * max_word_length
triangle_numbers = {}
#tn = ½n(n+1)
for i in range(1, max_triangle_number +1):
    tn = (i * 0.5 ) * (i +1)
    triangle_numbers[int(tn)] = True

print(triangle_numbers)
triangle_words_count = 0
# For each word calculate the word_value
for word in words:
    character_value = getCharacterValue(word)
    # Check if is traingle_number in hashmap
    if character_value in triangle_numbers:
        triangle_words_count += 1

print(triangle_words_count)