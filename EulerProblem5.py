#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without
#any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#check each number as you increment for being divisible by 1-20 and return the first one that works
#if divisible by 20 then divisible by 2, 4, 5, 10
#Final list of divisors: 20 19 18 17 16 14 13 11                   
def CheckIfDivisible(number):
    number = int(number)
    status = False
    if(number%20 != 0):
        return False
    if(number%19 != 0):
        return False
    if(number%18 != 0):
        return False
    if(number%17 != 0):
        return False
    if(number%16 != 0):
        return False
    if(number%14 != 0):
        return False
    if(number%13 != 0):
        return False
    if(number%11 != 0):
        return False
    else:
        status = True
    return status


#jump in steps of 20 because it must be divisible by 20
#Add a function to check if it's divisible by 20 before iterating through the rest?
for i in range(20, 300000000, 20):
    if(CheckIfDivisible(i) == True):
        print (f"{i}\n")
    else:
        print(f"\rChecking number: {i}", end="")

#Answer after 5 minutes of brute force:
#232792560
    