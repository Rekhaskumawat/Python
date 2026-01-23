
#################################################################################
#
#   Function Name : Add
#   Description   : Addition of two number
#   Input         : A Number
#   Output        : return sum
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def Add(No1 , No2):
    
    sum = 0
    sum = No1+No2
    return sum


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

    Value1 = 0
    Value2 = 0
    Ret = False
    print("Enter first Number :-")
    Value1 = int(input())

    print("Enter second Number :-")
    Value2 = int(input())

    Ret = Add(Value1 , Value2)

    print("Addition is:- ", Ret)


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input1 : 12          Input2 : 12             Output:24
#    Input1 : 11          Input2 : 23             Output:34
#
#################################################################################