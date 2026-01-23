
#################################################################################
#
#   Function Name : SumFactor
#   Description   : return sum of factor
#   Input         : A Number
#   Output        : summation
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 23 / 01 / 2026
#
#################################################################################

def Factor(No1):
    
    sum = 0
    for i in range(1 ,No1//2 +1):
        if(No1 % i == 0):
            sum = sum +i

    return sum 

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
    Ret = 0
    print("Enter the Number :-")
    Value = int(input())

    Ret = Factor(Value)
    print("Summation of factor is :-", Ret)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#    Input : 12                       Output: 16
#    Input : 6                       Output : 6
#
#################################################################################