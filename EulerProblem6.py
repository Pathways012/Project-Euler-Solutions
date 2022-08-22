'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025.

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is

3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
'''
import time

def SumOfSquares(number):
    sum = 0
    i = 1
    while(i <= number):
        sum = sum + (i**2)
        i = i + 1
    return sum

def SquareOfSumOfNaturalNumbers(number):
    sum = 0
    i = 1
    while(i <= number):
        sum = sum + i
        i = i + 1
        
    result = (sum**2)
    return result

print("Starting calculations...")
StartTime = time.time()
natural = SquareOfSumOfNaturalNumbers(100)
squares = SumOfSquares(100)
EndTime = time.time()
print("Finished calculating.")
print("The answer is: ", natural - squares)
print("Program ran in ", EndTime - StartTime, "seconds.")
#25164150

