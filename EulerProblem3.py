#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def CheckIfPrimeNumber(number):
    for i in range(2, int(number/2)):
        if(number%i == 0):
            return False

    return True

def FindLargestPrimeFactor(number):
    LargestPrime = 1
    for i in range(2, int(number/2)):
        if(number%i == 0):
            if(CheckIfPrimeNumber(i) == True):
                #print(i)
                LargestPrime = i

    return LargestPrime

print("Please enter a number: ")
number = input()       
print(f"The largest prime factor is {number}")
#print(FindLargestPrimeFactor(13195))
#print(FindPrimeFactors(600851475143)) TOO BIG; 300 BILLION SOMETHING TESTS TO RUN...
