#############################################################################
#   
#   Description : > Both thread should accept a list of integer as input
#                 > Create two separate thread named EvenList and OddList
#                 > EvenList should extract Even elements from the list 
#                       and calculate and display the sum of elements   
#                 > OddList should extract odd elements from the list 
#                       and calculate and display the sum of elements
#
#   Author      : Rekha Shankarlal Kumawat 
#
#   Date        : 26 / 10 / 2026
#
############################################################################

import threading

def EvenList(Arr):

    EvenSum = 0

    for i in range(len(Arr)):
        if((Arr[i] % 2 == 0)):
            EvenSum = EvenSum + Arr[i]

    print("Sum of Even elements :- ",EvenSum)

def OddList(Arr):

    OddSum = 0

    for i in range(len(Arr)):
        if((Arr[i] % 2 == 1)):
            OddSum = OddSum + Arr[i]

    print("Sum of Odd elements :- ",OddSum)

def main():

    Size = 0
    elements = 0
    data = list()
    print("Enter Number of elements:-")
    Size = int(input())

    print("enter the Numbers :-")
    for i in range(Size):
        elements = int(input())
        data.append(elements)

    Even = threading.Thread(target= EvenList, args = (data ,))
    Odd = threading.Thread(target= OddList , args= (data ,))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()
    

if __name__ =="__main__":
    main()

############################################################################
#
#   Enter number of elements : 5
#   Enter the elements : 1 2 3 4 5
#   Sum of even elemnets : 6
#   Sum of Odd elements : 9
#
############################################################################
