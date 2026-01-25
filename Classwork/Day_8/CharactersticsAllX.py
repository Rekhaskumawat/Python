

class Demo:

    No = 10

    def __init__(self , A , B):
        self.value1 = A
        self.value2 = B
    
print("Class variable No :", Demo.No)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

# print(obj1.No)        Allowed

print("Instance variable of obj1 : ",obj1.value1 , obj1.value2)         #11 21
print("Instance variable of obj2 : ",obj2.value1 , obj2.value2)         # 51 101

obj1.value1 =15

Demo.No = 0
# obj1.No = 11     not a good programming practice

print("Instance variable of obj1 : ",obj1.value1 , obj1.value2)         # 15  21
print("Instance variable of obj2 : ",obj2.value1 , obj2.value2)         # 51 101


print(obj1.No)          # 0       
print(obj2.No)          # 0
