
import Arithmetic

#################################################################################
#
#   Function Name : Operations
#   Description   : Performs arithmetic operations
#   Input         : every function have two number as input
#   Output        : operation perfromed ans
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################
def Operations(no1 , no2):

    Add = Arithmetic.Addition(no1 ,no2)
    print("Addition :- ",Add)

    Sub = Arithmetic.Subtraction(no1 ,no2)
    print("Subtraction :- ",Sub)
    
    multi = Arithmetic.Multiplication(no1 ,no2)
    print("Multiplication :- ",multi)
    
    div = Arithmetic.Division(no1 ,no2)
    print("Division :- ",div)

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

    Value1 = 0
    Value2 = 0
    Ret = 0
    print("Enter first Number :-")
    Value1 = int(input())

    print("Enter second Number :-")
    Value2 = int(input())

    Operations(Value1 , Value2)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input : 5                       Output: 120
#    Input : 3                       Output : 6
#
#################################################################################