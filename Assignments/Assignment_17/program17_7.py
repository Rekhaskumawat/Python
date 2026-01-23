
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

    for i in range(1 , No1+1):
        for j in range(1 , No1+1):
            print(j, end = '')
        print("")

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
    print("Enter the Number :-")
    Value = int(input())

    Pattern(Value)


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input : 5                        Output: 1 2 3 4 5
#                                             1 2 3 4 5
#                                             1 2 3 4 5
#                                             1 2 3 4 5
#
#################################################################################