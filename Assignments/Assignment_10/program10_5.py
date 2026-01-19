
#################################################################################
#
#   Function Name : DisplayOdd
#   Description   : Display Odd Number till that number
#   Input         : A Number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 18 / 01 / 2026
#
#################################################################################

def DisplayOdd(No1):

    for i in range(1 ,No1+1):

        if ((i % 2) == 1):

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
    
    DisplayOdd(iValue1)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 10        Ouput : 1 3 5 7 9
#   Input1: 6        Ouput : 1 3 5
#7
#################################################################################