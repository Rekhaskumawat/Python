#############################################################################
#   
#   Description : > Create two separate thread named EvenFactor and OddFactor
#                 > EvenFactor Thread should identify the even factor and 
#                               display sum of even factors
#                 > OddFactor Thread should identify the Odd factor and 
#                               display sum of Odd factors
#                 > After both execution main thread should display
#                               "Exit from main thread"
#   Author      : Rekha Shankarlal Kumawat 
#
#   Date        : 26 / 10 / 2026
#
############################################################################

import threading

def EvenFactors(No):

    EvenSum = 0

    for i in range(1,No+1):
        if((No % i == 0) and (i % 2 == 0)):
            EvenSum = EvenSum + i

    print("Sum of Even Factors :- ",EvenSum)

def OddFactors(No):

    
    OddSum = 0

    for i in range(1,No+1):
        if((No % i == 0) and (i % 2 == 1)):
            OddSum = OddSum + i

    print("Sum of Odd Factors :- ",OddSum)

def main():

    No = 0
    print("Enter a Number:-")
    No = int(input())

    Even = threading.Thread(target= EvenFactors, args = (No ,))
    Odd = threading.Thread(target= OddFactors , args= (No ,))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()
    
    print("Exit from main thread")

if __name__ =="__main__":
    main()

############################################################################
#
#   Enter a number :- 12
#   Sum of Even factors = 24
#   Sum of odd Factore = 4
#   Exit from main thread
#
############################################################################
