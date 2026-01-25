
import gc

class Demo:

    # Class Characterstics

    No1 = 10               
    No2 = 11 

    def __init__(self):

        # Instance Characterstics

        self.A = 101
        self.B = 201

        print("Inside constructor")

    def __del__(self):
        print("Inside Destructor")

#print(Demo.A)               #  Error as we are accessing the Instance variable
#print(Demo.B)                  Error

obj = Demo()

print(obj.A)
print(obj.B)

print(Demo.No1)
print(Demo.No2)