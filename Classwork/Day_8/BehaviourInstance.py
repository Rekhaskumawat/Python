

class Demo:

    No = 10

    def __init__(self , A , B):             # special method (constructor)
        self.value1 = A
        self.value2 = B
    
    def Fun(self):                          # inctance Method
        print("Inside Instance Method Fun :", self.value1 , self.value2)

    @classmethod                                # decorator only written on above class method
    def Sun(cls):                               # class Method
        print("Inside Class Method Sun :" , cls.No)


Demo.Sun()
print("Class variable No : ", Demo.No)

obj = Demo(11,21)
obj.Fun()
print("Instance variable :",obj.value1 , obj.value2)