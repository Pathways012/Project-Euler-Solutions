#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def IsMultipleOfThree(number):
    try:
        number = int(number)
    except:
        print("Please input a number.")

    if number%3 == 0:
        return True
    return False

def IsMultipleOfFive(number):
    try:
        number = int(number)
    except:
        print("Please input a number.")

    if number%5 == 0:
        return True
    return False


answer = 0
#PROBLEM: REPEATED MULTIPLES OF THREE AND FIVE i.e. 15
#solved by iterating in same loop.
for i in range(1000):
    if(IsMultipleOfThree(i) == True or IsMultipleOfFive(i) == True):
        answer = answer + i
    else:
        pass

print(answer)
#Answer should be 233168
#print(bool(3%3)) neat.

#IsMultipleOfThree("Wrench!")
