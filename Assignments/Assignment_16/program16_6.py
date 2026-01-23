
#################################################################################
#
#   Function Name : ChkNum
#   Description   : checks number is positive , negative or zero
#   Input         : A Number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def ChkNum(No1):
    
    if(No1 > 0):
        print("Positive number")
    elif(No1 < 0):
        print("Negative number")
    else:
        print("Zero")


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

    Value = 0
    print("Enter the Number :-")
    Value = int(input())

    ChkNum(Value)


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input : 12                        Output: Positive Number
#    Input : -11                       Output: Negative Number
#    Input : 0                         Output: Zero
#
#################################################################################