"""
Problem 55 - Lychrel numbers
-------------------------------------------------------------------------------
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?
"""
lychrel_map = dict()

def checkPalindrome(value):
    string_value = str(value)
    for i in range(0, int((len(string_value) + 1) / 2)):
        if string_value[i] != string_value[(i + 1) * -1]:
            return False

    return True

def getReversed(num):
    return int(str(num)[::-1])

def checkLychrelNumber(num, depth):
    # Memoize
    if num in lychrel_map:
        return lychrel_map[num]
    
    ## Check Depth
    if depth >= 50:
        return True
    
    # Check Palindrome
    potentialLychrel = num + getReversed(num)
    if not checkPalindrome(potentialLychrel):
        retVal = checkLychrelNumber(potentialLychrel, depth + 1)
        lychrel_map[num] = retVal
        lychrel_map[getReversed(num)] = retVal
        return retVal

    return False
    
sum = 0

for i in range(10, 10_000):
    if checkLychrelNumber(i, 0):
        sum += 1 

print(sum)