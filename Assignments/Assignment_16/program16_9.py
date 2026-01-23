
#################################################################################
#
#   Function Name : DisplayEven
#   Description   : Display first 10 Even Number
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def DisplayEven():
    
    for i in range(2 ,22 ,2):
        print(i ,'', end = '')


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

    DisplayEven()


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Output: 2 4 6 8 10 12 14 16 18 20

#################################################################################