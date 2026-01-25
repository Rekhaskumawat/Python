
class Arithmetic:

    def Addition(self,No1 , No2):                       # instance Method
        return No1+No2

    def Subtraction(self,No1 , No2):
        return No1-No2

value1 = 0
value2 = 0
Ans = 0 

value1 = int(input("Enter first number:-"))
value2 = int(input("Enter second number:-"))

obj = Arithmetic()                                  

Ans = obj.Addition(value1 , value2)             
print("Addition is:-", Ans)

Ans = Arithmetic().Subtraction(value1 , value2)
print("Subtraction is :-", Ans)