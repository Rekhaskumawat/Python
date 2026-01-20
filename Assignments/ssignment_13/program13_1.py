
#################################################################################
#
#   Function Name : RectangleArea
#   Description   : Calculate Area of rectangle
#   Input         : Length , Breadth of Rectangle
#   Output        : Area
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 18 / 01 / 2026
#
#################################################################################

def RectangleArea(length , breadth):

    Area = 0
    Area = length*breadth
    return Area


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

    length = 0
    breadth = 0
    print("Enter length of rectangle:-")
    length = int(input())
    
    print("Enter breadth of rectangle:-")
    breadth = int(input())

    Ret = RectangleArea(length , breadth)

    print("Area of rectangle :", Ret)


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 12        Input2 :12       Ouput : Area of rectangle :144
#   Input1: 14        Input2 : 2       Ouput : Area of rectangle :28
#7
#################################################################################