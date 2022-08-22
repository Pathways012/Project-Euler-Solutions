'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import time

def CheckIfPrimeNumber(number):
    for i in range(2, int(number/2)):
        if(number%i == 0):
            return False
    return True

StartTime = time.time()
PrimesFound = 0
counter = 2

while(PrimesFound <= 10001):
    if(CheckIfPrimeNumber(counter) == True):
        print(counter, f"is prime number {PrimesFound}.")
        PrimesFound = PrimesFound + 1
    counter = counter + 1

#PrimesFound and counter will both have been incremented one extra time through the loop.
PrimesFound = PrimesFound - 1
counter = counter - 1

print(f"The {PrimesFound}st prime has been found: {counter}")
EndTime = time.time()
print("The program ran in ", EndTime - StartTime, "seconds.")
#104743