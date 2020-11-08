from functools import reduce

# All number where x <= 10; Can be ignored because they are all able to create numbers > 10 < 20
number_range = range(11,20,1)

def divides_correctly(num):
    value = reduce(lambda x,y: x or y ,map(lambda y: num % y , number_range))

    if (value):
        return False
    return True


# count in multiples of the product of the highest relative-primes that I can be bothered working out.
desired_number = 0
while(True):
    desired_number += 6840 # ( 20*19*18 )
    if(divides_correctly(desired_number)):
        break;

print(desired_number)