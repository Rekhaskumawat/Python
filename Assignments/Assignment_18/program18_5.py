
import MarvellousNum
#################################################################################
#
#   Function Name : ListPrime
#   Description   : return the sum of all prime numbers
#   Input         : A list 
#   Output        : Summmation
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 24 / 01 / 2026
#
#################################################################################

def ListPrime(Arr):

    sum = 0
    PrimeNo = list(MarvellousNum.ChkPrime(Arr))

    for i in range(len(PrimeNo)):
        sum = sum +PrimeNo[i]

    return sum




#################################################################################
#
#   Function Name : main()
#   Description   : call another function (like an entry point function)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 24 / 01 / 2026
#
#################################################################################

def main():

    element = 0
    value = 0
    ret = 0

    print("Number of elements:-")
    element = int(input())

    Data = list()

    for i in range(element):

        value = int(input())
        Data.append(value)

    ret = ListPrime(Data)

    print("summation of prime numbers :-",ret)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input : 6        Input2 : 13 5 45 7 4 56    Output : 25
#
#################################################################################