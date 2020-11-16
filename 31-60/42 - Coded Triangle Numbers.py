"""
Problem 42 - Coded Triangle Numbers
-------------------------------------------------------------------------------
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.

Using words.txt [Provided by resources/42_words.txt], a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""
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
# tn = ½n(n+1)
for i in range(1, max_triangle_number + 1):
    tn = (i * 0.5) * (i + 1)
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
