
#################################################################################
#
#   Function Name : ChkLength
#   Description   : Count the length of string
#   Input         : A String
#   Output        : length
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def ChkLength(name):
    
    return len(name)


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

    stringX = 0
    ret = 0
    print("Enter a string :-")
    stringX = input()

    ret= ChkLength(stringX)
    print("Length of string is:- ", ret)


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input : Marvellous Infosystems                Output: 22
#
#################################################################################