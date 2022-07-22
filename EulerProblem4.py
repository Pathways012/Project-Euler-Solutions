#A palindromic number reads the same both ways. The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 * 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

ForwardList = list()
BackwardList = list()

def CheckIfPalindrome(number):
    #Typecast the input to a string
    number = str(number)
    #Then use a list comprehension to turn it into two identical lists of integers
    ForwardList = [int(i) for i in number]
    BackwardList = [int(i) for i in number]
    #Reverse the second list
    BackwardList.reverse()
    #Compare the lists to see if they match
    if(ForwardList == BackwardList):
        print(f"The number {number} is a palindromic number.")
        #Clear both lists for reuse in subsequent runs
        ForwardList.clear()
        BackwardList.clear()
        return True
    ForwardList.clear()    
    BackwardList.clear()    
    return False

def DoMultiplications():
    FinalAnswer = 0
    Factor1 = 0
    Factor2 = 0
    #nested for loop to do the multiplications
    for i in range(100, 999):
        for n in range(100, 999):
            CurrentResult = i * n
            #If the current result is a palindrome and bigger than the last palindrome,
            #store the current result and its factors
            if(CheckIfPalindrome(CurrentResult) == True):
                if(CurrentResult > FinalAnswer):
                    FinalAnswer = CurrentResult
                    Factor1 = int(i)
                    Factor2 = int(n)
    #Return the biggest palindromic number and its factors as a tuple            
    return FinalAnswer, Factor1, Factor2


FinalAnswerTuple = (DoMultiplications())
print(f"The largest palindromic number is {FinalAnswerTuple[0]} from factors {FinalAnswerTuple[1]} and {FinalAnswerTuple[2]}.")
