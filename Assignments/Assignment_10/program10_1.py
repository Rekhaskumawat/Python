
#################################################################################
#
#   Function Name : MultiplicationTable
#   Description   : multiplication table of a number
#   Input         : A Number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 17 / 01 / 2026
#
#################################################################################

def MultiplicationTable(No1):

    for i in range(1 ,11):
        print(No1 ,"*",i,"=",No1*i)


#################################################################################
#
#   Function Name : main()
#   Description   : call another function (like an entry point function)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 17 / 01 / 2026
#
#################################################################################

def main():

    iValue1 = 0

    print("Enter number:-")
    iValue1 = int(input())
    
    MultiplicationTable(iValue1)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 3        Ouput : 3 6 9 12 15 18 21 24 27 30
#   Input1: 6        Ouput : 6 12 18 24 30 36 42 48 54 60
#
#################################################################################