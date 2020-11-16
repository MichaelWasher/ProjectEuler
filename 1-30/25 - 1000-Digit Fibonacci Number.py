"""
Problem 25 - 1000-digit Fibonacci number
-------------------------------------------------------------------------------
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
# 1000-digit Fibonacci number
digit_total = 0

first_num = 1
second_num = 1
fib_num = 0
index = 2

while digit_total < 1000:
    fib_num = first_num + second_num
    second_num = first_num
    first_num = fib_num
    digit_total = len(str(fib_num))
    index += 1

print("Index: " + str(index))
print("Fib: " + str(fib_num))
