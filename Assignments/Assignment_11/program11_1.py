
#################################################################################
#
#   Function Name : CheckPrime
#   Description   : checks number is prime or not
#   Input         : A Number
#   Output        : return true or not
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 18 / 01 / 2026
#
#################################################################################

def CheckPrime(No1):

    bflag = True
    for i in range(2 , No1//2):

        if ((No1 % i) == 0):

            bflag = False
            break
    
    if(bflag == True):
        return True
    else:
        return False
    

#################################################################################
#
#   Function Name : main()
#   Description   : call another function (like an entry point function)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 18 / 01 / 2026
#
#################################################################################

def main():

    iValue1 = 0
    Ret = False
    print("Enter number:-")
    iValue1 = int(input())
    
    Ret = CheckPrime(iValue1)

    if Ret == True:
        print(iValue1 ,"is a prime number")
    else:
        print(iValue1 ,"is not a prime number")

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 7        Ouput : 7 is a prime number
#   Input1: 6        Ouput : 6 is not a prime
#7
#################################################################################