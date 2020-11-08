prime_factors = [2, 3]

def checkPrime(num):
    
    for prime in prime_factors:
        if(num % prime == 0):
            return False
    
    return True

prime_index = 10001

x = prime_factors[-1]
while(True):
    x += 2

    if(checkPrime(x)):
        prime_factors.append(x)
    
    if(len(prime_factors) == prime_index):
        break

print(prime_factors[-1])
   