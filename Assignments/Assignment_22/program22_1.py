#####################################################################################
#
#   Description : Instance Variables: 
#                  The class should have two instance variables, named no1 and no2.
#                  These variables store values that are different for each object of the class
#
#                 Class Variable:
#                   The class should contain one class variable named Value.
#                   This variable is shared among all objects of the class.
#                 
#                 Constructor (__init__):
#                   The constructor should initialize the instance variables no1 and no2 
#
#                 Instance Methods
#                    Fun() – displays the values of instance variables no1 and no2.
#                   Gun() – also displays the values of instance variables no1 and no2.
#
#                  Object Creation
#                     Obj1 initialized with values (11, 21)
#                     Obj2 initialized with values (51, 101)
#
#   Date :   26 / 01 /2026
#
#   Author : Rekha Shankarlal Kumawat
#  
#####################################################################################

class Demo():

    Value = 0

    def __init__(self ,A,B):

        self.No1 = A
        self.No2 = B

    def Fun(self):

        print("Value of No1 and No2 respectively :- ", self.No1 , self.No2)

    def Gun(self):

        print("Value of No1 and No2 respectively :- ", self.No1 , self.No2)

def main():

    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Fun()

    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()