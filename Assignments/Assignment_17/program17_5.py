
#################################################################################
#
#   Function Name : ChkPrime
#   Description   : checks number is prime or not
#   Input         : A Number
#   Output        : return true or false
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def ChkPrime(No1):
    
    bFlag = True

    for i in range(2, No1):

        if(No1 % i == 0):

            bFlag = False
            break

    if(bFlag == True):
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
#   Date          : 23 / 01 / 2026
#
#################################################################################

def main():

    Value = 0
    Ret = False
    print("Enter the Number :-")
    Value = int(input())

    Ret = ChkPrime(Value)

    if(Ret == True):
        print("Number is prime")
    else:
        print("Number is not a prime")

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input : 12                       Output: number is not a prime
#    Input : 5                        Output : number is prime
#
#################################################################################