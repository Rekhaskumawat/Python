
#################################################################################
#
#   Function Name : DivisibleBy5
#   Description   : Number is Divisible By 5
#   Input         : A number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 21 / 01 / 2026
#
#################################################################################

DivisibleBy5 = lambda No1 : No1 % 5 == 0


#################################################################################
#
#   Function Name : main()
#   Description   : call another function (like an entry point function)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 21 / 01 / 2026
#
#################################################################################

def main():

    value1= 0
    Ret = 0
    print("Enter a Number:-")
    value1 = int(input())

    Ret = DivisibleBy5(value1 )

    if(Ret == True):
        print("Number is Divisible by 5")
    else:
        print("Number is not Divisible by 5")

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 50                     Output : Number is Divisible by 5
#   Input1: 6                     Output : Number is not Divisible by 5
#7
#################################################################################