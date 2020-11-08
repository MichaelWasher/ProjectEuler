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
print("Fib: "  + str(fib_num))

    