
import gc

class Demo:

    def __init__(self):                 #constructor

        print("Inside constructor")

    def __del__(self):                      #destructor
        print("Inside Destructor")

obj1 = Demo()
obj2 = Demo()

del obj1
del obj2

gc.collect()                            #garbag collector

print("End of application")