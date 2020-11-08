from math import sqrt

COUNT = 1000

def calculateABC():

    for a in range(0,int(COUNT/2),1):
        for b in range(a+1,int(COUNT/2),1):
            c_squared = (a**2 + b**2)
            c = sqrt(c_squared)

            if(c.is_integer() and a+b+c == COUNT):
                return int(a), int(b), int(c)
    

a, b, c = calculateABC()

# Print the calculated values
print("A: " + str(a))
print("B: " + str(b))
print("C: " + str(c))
print("Product: " + str(a*b*c))
