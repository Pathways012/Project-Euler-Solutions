#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#the square root is 775146.0992245268
#answer should be 6857
def CheckIfPrimeNumber(number):
    for i in range(2, int(number/2)):
        if(number%i == 0):
            return False
    return True

def FindLargestPrimeFactor(number):
    LargestPrime = 1
    for i in range(2, int(775147)):
        print(f"\r\tOn iteration {i}", end="")
        if(number%i == 0):
            if(CheckIfPrimeNumber(i) == True):
                print(f" found a prime factor")
                LargestPrime = i
    return LargestPrime


number = int(600851475143)
number = FindLargestPrimeFactor(number)      
print(f"\nThe largest prime factor is {number}")


