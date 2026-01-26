####################################################################################
#   
#   Description : > Create Prime and NonPrime
#                 > Both Thread should Accept list of elements
#                 > Prime thread should display all prime number from the list
#                 > NonPrime thread should display all non prime number from the list
#                 > Use appropriate thread synchronization
#
#   Author      : Rekha Shankarlal Kumawat 
#
#   Date        : 26 / 10 / 2026
#
###################################################################################

import threading

def Prime(Arr):

    pdata = list()
    for i in range(len(Arr)):

        if Arr[i] <2:
            continue
        
        bflage = True
        for j in range(2 ,Arr[i]):
            if(Arr[i] % j == 0):
                bflage = False
                break

        if(bflage == True):
            pdata.append(Arr[i])

    print("List of prime elements :-",pdata)


def NonPrime(Arr):

    npdata = list()
    for i in range(len(Arr)):

        if Arr[i] <2:
            continue
        
        bflage = True
        for j in range(2 ,Arr[i]):
            if(Arr[i] % j == 0):
                bflage = False
                break

        if(bflage == False):
            npdata.append(Arr[i])

    print("List of Non prime elements :-",npdata)


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

    t1 = threading.Thread(target= Prime , args=(data ,))
    t2 = threading.Thread(target= NonPrime , args=(data ,))


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
#   List of prime elements :- [ 5,7,3]
#   List of non prime elements :- [18,9]
# 
############################################################################
