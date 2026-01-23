
#################################################################################
#
#   Function Name : Pattern
#   Description   : prints pattern
#   Input         : A Number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def Pattern(No1):
    
    for i in range(No1):
        print("* ", end = '')


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

    Pattern(Value)


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input : 12                        Output: * * * * * * * * * * * * 

#################################################################################