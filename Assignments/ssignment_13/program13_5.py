
#################################################################################
#
#   Function Name : Grade
#   Description   : cDisplay grade according to marks
#   Input         : A number
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 18 / 01 / 2026
#
#################################################################################

def Grade(No1):
    
    if(No1 >= 75):
        print("Distinction")
    elif(No1< 75 and No1 >= 60):
        print("first class")
    elif(No1 < 60 and No1 >= 50):
        print("Second class")
    elif(No1 < 50 ):
        print("Fail")
    else:
        print("Incalid input")


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

    value = 0
    print("Enter a Number:-")
    value = int(input())

    Grade(value)

# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 56              Ouput : Second class
#   Input1: 98              Ouput : Distinction
#7
#################################################################################