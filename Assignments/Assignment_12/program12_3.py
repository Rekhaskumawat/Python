
#################################################################################
#
#   Function Name : Arithmetic
#   Description   : perfrom arethmatic operation 
#                   (Addition ,substraction , division , multiplication )
#   Input         : A number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 20 / 01 / 2026
#
#################################################################################

def Arithmatic(No1 , No2):

    Add = No1+No2
    print("Addition is :-",Add)

    sub = No1 - No2
    print("Substraction is :", sub)

    multi = No1*No2
    print("Multiplication is :", multi)

    div = No1/No2
    print("Division is :", div)


#################################################################################
#
#   Function Name : main()
#   Description   : call another function (like an entry point function)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 20 / 01 / 2026
#
#################################################################################

def main():

    value1 = 0
    value2 = 0
    print("Enter first Number:-")
    value1 = int(input())

    print("Enter second Number:-")
    value2 = int(input())

    Arithmatic(value1 , value2)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 3       input2 : 3          Ouput : Addition is :- 6
#                                               Substraction is : 0
#                                               Multiplication is :9
#                                               Division is :1.0
#
#################################################################################