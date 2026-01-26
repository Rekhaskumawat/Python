####################################################################################
#   
#   Description : > Thread1 should display Maximum number from the same list
#                 > Thread2 should Display Minimum Number from the same list
#                 > The list should be accepted from user
#
#   Author      : Rekha Shankarlal Kumawat 
#
#   Date        : 26 / 10 / 2026
#
###################################################################################

import threading

def Thread1(Arr):

    Max = Arr[0]
    for i in range(len(Arr)):
        if(Arr[i] > Max):
            Max = Arr[i]

    print("Maximum element from list is :-", Max)


def Thread2(Arr):

    Min = Arr[0]
    for i in range(len(Arr)):
        if(Arr[i] < Min):
            Min = Arr[i]

    print("Minimum element from list is :-", Min)


def main():

    size = 0
    value = 0
    data = list()

    print("Enter the number of element in list:-")
    size = int(input())

    print("Enter the elements:-")

    for i in range(size):
        value = int(input())
        data.append(value)

    t1 = threading.Thread(target= Thread1 , args=(data ,))
    t2 = threading.Thread(target= Thread2 , args=(data ,))


    t1.start()
    t2.start()

    t1.join()
    t2.join()

    

if __name__ =="__main__":
    main()

############################################################################
#
#   Enter the number of element in list:- 5
#   Enter the elements:- 5 7 18 9 3
#   Maximum number from the list :- 18
#   Minimum number from the list :- 3
# 
############################################################################
