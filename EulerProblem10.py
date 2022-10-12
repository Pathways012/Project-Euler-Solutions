# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import math
import time

def CheckIfPrimeNumber(number):
    for i in range(2, int(math.sqrt(number))+1):
        if(number%i == 0):
            return False
    return True

start_time = time.time()

primes = list()
primes.append(2)
primes.append(3)

i = 5
while(i < 2000000):
    if(CheckIfPrimeNumber(i) == True):
        primes.append(i)

    print(f"\rChecked number {i}...", end="")
    i += 1

#print(primes)
print(sum(primes))

end_time = time.time()
run_time = end_time - start_time
print(f"Ran in {run_time} seconds.")
# 142913828922
# Ran in 145.97119903564453 seconds.
