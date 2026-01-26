#############################################################################
#   
#   Description : > Create two separate thread named Even and Odd
#                 > Even Thread should display first 10 Even Numbers
#                 > Odd thread should dispaly first 10 odd Numbers
#
#   Author      : Rekha Shankarlal Kumawat 
#
#   Date        : 26 / 10 / 2026
#
############################################################################

import threading

def EvenNumbers(No):

    print("Even numbers are:-" , end = "")

    for i in range(2 , (2*No + 1) , 2):
        print(i ,end =" ")
    print("")

def OddNumbers(No):

    print("Odd Numbers are :-", end=" ")

    for i in range(1 ,(2*No +1) , 2):
        print(i,end = " ")
    print(" ")

def main():

    No = 0
    print("Enter how many even and odd number to be printed:-")
    No = int(input())

    Even = threading.Thread(target= EvenNumbers , args = (No ,))
    Odd = threading.Thread(target= OddNumbers , args= (No ,))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ =="__main__":
    main()

############################################################################
#
#   Enter how many even and odd numbers to be printed:- 10
#   Even Numbers are :- 2,4,6,8,10,12,14,16,18,20
#   Odd Numbers are :- 1,3,5,7,9,11,13,15,17,19
#
############################################################################
