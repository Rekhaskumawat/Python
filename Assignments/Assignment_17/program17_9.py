
#################################################################################
#
#   Function Name : CountDigits
#   Description   : count Digits of number
#   Input         : A Number
#   Output        :  Number of digits
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def CountDigits(No1):

    count = 0
    while(No1 != 0):
        No1 = No1//10
        count = count +1

    return count

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
    Ret = 0
    print("Enter the Number :-")
    Value = int(input())

    Ret = CountDigits(Value)

    print("Digits in number are :-", Ret)


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input : 1234567                   Output: Digits in number are :- 7
#                                           
#
#################################################################################