#find all prime numbers up to the limit
limit = 1000

def CheckIfPrimeNumber(number):
    for i in range(2, int(math.sqrt(number))+1):
        if(number%i == 0):
            return False
    print(number)
    return True

for i in range(1, limit):
    CheckIfPrimeNumber(i)
