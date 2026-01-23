
#################################################################################
#
#   Function Name : DivisibleBy5
#   Description   : checks number is divisible by 5 or not
#   Input         : A Number
#   Output        : return true or false
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def DivisibleBy5(No1):
    
    if(No1 % 5 == 0):
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

    Ret = DivisibleBy5(Value)

    if(Ret == True):
        print("True")
    else:
        print("False")


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input : 20                       Output: True
#    Input : 11                       Output: False
#
#################################################################################