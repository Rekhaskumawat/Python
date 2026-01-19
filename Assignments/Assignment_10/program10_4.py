
#################################################################################
#
#   Function Name : DisplayEven
#   Description   : Display Even Number till that number
#   Input         : A Number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 18 / 01 / 2026
#
#################################################################################

def DisplayEven(No1):

    for i in range(1 ,No1+1):

        if ((i % 2) == 0):

            print(i)
    

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
    print("Enter number:-")
    iValue1 = int(input())
    
    DisplayEven(iValue1)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 10        Ouput : 2 4 6 8 10
#   Input1: 6        Ouput : 2 4 6
#7
#################################################################################