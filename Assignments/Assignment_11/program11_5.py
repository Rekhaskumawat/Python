
#################################################################################
#
#   Function Name : Palindrome
#   Description   : Checks number is palindrome or not
#   Input         : A Number
#   Output        : Return Reverse number
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 18 / 01 / 2026
#
#################################################################################

def Palindrome(No1):

    Digit = 0
    Rev = 0
    while(No1 != 0):
        Digit = No1 % 10
        No1 = No1 // 10
        Rev = Rev*10 + Digit
    
    return Rev
    

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
    Ret = 0
    print("Enter number:-")
    iValue1 = int(input())
    
    Ret = Palindrome(iValue1)

    if Ret == iValue1:
        print("Number is Palindrome")
    else:
        print("Number is not a palindrome")


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 121           Ouput : Number is Palindrome
#   Input1: 143435        Ouput : Number is not a Palindrome 
#7
#################################################################################