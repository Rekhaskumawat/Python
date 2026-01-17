
#################################################################################
#
#   Function Name : Divisible
#   Description   : check wheather number is Divisible by 3 and 5
#   Input         : A Number
#   Output        : return true or false
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 17 / 01 / 2026
#
#################################################################################

def Divisible(No1):

    if((No1% 3 == 0) and (No1%5 == 0)):

        return True


#################################################################################
#
#   Function Name : main()
#   Description   : call another function (like an entry point function)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 17 / 01 / 2026
#
#################################################################################

def main():

    iValue1 = 0
    iRet = 0

    print("Enter number:-")
    iValue1 = int(input())
    
    iRet = Divisible(iValue1)

    if(iRet == True):
       print(iValue1,"is Divisible by 3 and 5")

    else:
       print(iValue1 ,"is not Divisible by 3 and 5")       

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 15        Ouput : 15 is Divisible by 3 and 5
#   Input1:  6        Ouput : 6 is not Divisible by 3 and 5
#
#################################################################################