
#################################################################################
#
#   Function Name : AreaCircle
#   Description   : Calculate Area of circle
#   Input         : radius of circle
#   Output        : Area
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 18 / 01 / 2026
#
#################################################################################

def AreaCircle(radius):

    Area = 0
    Area = 3.14*radius*radius
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

    radius = 0
    print("Enter radius of circle:-")
    radius = int(input())

    Ret = AreaCircle(radius)

    print("Area of circle :", Ret)


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: 3             Ouput : Area of circle :28.25
#   Input1: 14            Ouput : Area of circle :615.44
#7
#################################################################################