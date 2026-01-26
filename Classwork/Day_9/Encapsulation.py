
# Encapsulation : Binding characterstics and behavours together into a class

class Arithmetic:

    def __init__(self ,A ,B):
        
        self.No1 = A
        self.No2 = B

        print("Object gets created succesfully")

    def Addition(self):

        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self):

        Ans = 0
        Ans = self.No1 - self.No2
        return Ans


obj1 = Arithmetic(11,10)                 # Arithmetic(id(obj1),11,10)   ->  __init__(id(obj1),11,10)
obj2 = Arithmetic(21,20)                 # Arithmetic(id(obj2),21,20)   ->  __init__(id(obj1),21,20)

ret = 0
ret = obj1.Addition()
print("Addition is :- ", ret)

ret =obj2.Substraction()
print("Subtraction is :-",ret)