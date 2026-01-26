####################################################################################
#   
#   Description : > Thread1 compute the sum of all elements from the list
#                 > Thread2 compute the product of all elements from the list
#                 > return the list to the main thread  and display them
#
#   Author      : Rekha Shankarlal Kumawat 
#
#   Date        : 26 / 10 / 2026
#
###################################################################################

import threading
import queue                        # queue is use to pass data between threads

def Thread1(Arr , result_queue):

    Sum = 0
    for i in range(len(Arr)):
        Sum = Sum + Arr[i]

    result_queue.put(Sum)

def Thread2(Arr , result_queue):

    Prod = 1
    for i in range(len(Arr)):
        Prod = Prod * Arr[i]

    result_queue.put(Prod)


def main():

    size = 0
    value = 0
    data = list()

    q = queue.Queue()

    print("Enter the number of element in list:-")
    size = int(input())

    print("Enter the elements:-")

    for i in range(size):
        value = int(input())
        data.append(value)

    t1 = threading.Thread(target= Thread1 , args=(data ,q))
    t2 = threading.Thread(target= Thread2 , args=(data ,q))


    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Summation of all elemets from the list :-",q.get())
    print("product of all elements from the list :-",q.get())
    

if __name__ =="__main__":
    main()

############################################################################
#
#   Enter the number of element in list:- 5
#   Enter the elements:- 1 2 3 4 5
#   Summation of all elemets from the list :-15
#   Product of all elemets from the list :-120
# 
############################################################################
