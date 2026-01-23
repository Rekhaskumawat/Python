
#################################################################################
#
#   Function Name : ChkNum
#   Description   : checks number is Even or Odd
#   Input         : A Number
#   Output        : return true or false
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def ChkNum(No1):
    
    if(No1 % 2 == 0):
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

    Ret = ChkNum(Value)

    if(Ret == True):
        print("Even Number")
    else:
        print("Odd Number")


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input : 12                       Output: Even Number
#    Input : 11                       Output: Odd Number
#
#################################################################################