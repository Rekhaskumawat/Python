#####################################################################################
#
#   Description : Instance Variables: 
#                  Radius → stores the radius of the circle
#                  Area → stores the calculated area
#                  Circumference → stores the calculated circumference
#
#                 Class Variable :
#                   PI → a constant shared by all objects, initialized to 3.14
#
#                 Constructor (__init__):
#                   Initializes Radius, Area, and Circumference to 0.0 when an object is created
#
#                 Instance Methods
#                    Accept() → takes the radius input from the user
#                    CalculateArea() → calculates area
#                    CalculateCircumference() → calculates circumference 
#                    Display() → prints the values of Radius, Area, and Circumference
#
#                  Object Creation
#                     You must create multiple objects of the Circle class
#                     Call all methods for each object separately
#
#   Date :   26 / 01 /2026
#
#   Author : Rekha Shankarlal Kumawat
#  
#####################################################################################

class Circle():

    PI = 3.14

    def __init__(self):

        self.Radius = 0
        self.Area= 0
        self.Circumference = 0

    def Accept(self):

        print("Enter the radius of Circle:-")
        self.Radius = int(input())

    def CalculateArea(self):

        self.Area = Circle.PI*self.Radius*self.Radius

    def CalculateCircumference(self):

        self.Circumference = 2*Circle.PI*self.Radius

    def Display(self):

        print("Radius of Circle :-", self.Radius)
        print("Area of circle is :-", self.Area)
        print("Circumference of circle :",self.Circumference)

def main():

    obj1 = Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()


if __name__ == "__main__":
    main()


