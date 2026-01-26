#####################################################################################
#
#   Description : Instance Variables: 
#                  Value1 → first number
#                  Value2 → second number
#
#                 Constructor (__init__):
#                   nitializes both Value1 and Value2 to 0
#
#                 Instance Methods
#                    Accept() → takes input for Value1 and Value2 from the user
#                    Addition() → returns the sum of Value1 and Value2
#                    Subtraction() → returns the difference of Value1 and Value2
#                    Multiplication() → returns the product of Value1 and Value2
#                    Division() → returns the division result and handles division by zero properly
#
#                  Object Creation
#                     Create multiple objects of the Arithmetic class
#                     Invoke all arithmetic methods using those objects
#
#   Date :   26 / 01 /2026
#
#   Author : Rekha Shankarlal Kumawat
#  
#####################################################################################

class Arithmetic():


    def __init__(self):

        self.Value1 = 0
        self.Value2= 0

    def Accept(self):

        print("Enter first number:-")
        self.Value1 = int(input())

        print("Enter Second number:-")
        self.Value2 = int(input())

    def Addition(self):

        return self.Value1 + self.Value2

    def Subtraction(self):

        return self.Value1 - self.Value2
    
    def multiplication(self):

        return self.Value1 * self.Value2
    
    def Division(self):

        return self.Value1 / self.Value2

def main():

    Ret = 0

    obj1 = Arithmetic()

    obj1.Accept()

    Ret = obj1.Addition()
    print("Addition is :- ",Ret)

    Ret = obj1.Subtraction()
    print("Subtraction is :- ",Ret) 

    Ret = obj1.multiplication()
    print("multiplication is :- ",Ret)

    Ret = obj1.Division()
    print("Division is :- ",Ret)


if __name__ == "__main__":
    main()


