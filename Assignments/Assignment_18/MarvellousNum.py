# module file for program18_5.py

#################################################################################
#
#   Module Name   : MarvellousNum
#   Description   : contains functions :-
#                                    ChkPrime()
#                                    append prime numbers into list
#   Input         : list of numbers
#   Output        : list of prime numbers
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 24 / 01 / 2026
#
#################################################################################

def ChkPrime(Arr):

    prime = list()

    for i in range(len(Arr)):

        if Arr[i] < 2:
            continue

        bFlage = True
        for j in range(2 , Arr[i]):
            if(Arr[i] % j == 0):
               bFlage = False
               break
        
        if(bFlage == True):
            prime.append(Arr[i])

    return prime