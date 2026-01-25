Addition = lambda No1,No2 : No1 + No2

Subtraction = lambda No1,No2 : No1 - No2

Value1 = 0
Value2 = 0
Ans = 0

Value1 = int(input("Enter first Number:-"))
Value2 = int(input("Enter second number:-"))

Ans = Addition(Value1 , Value2)
print("Additon is :-", Ans)

Ans = Subtraction(Value1 , Value2)
print("Subtraction is :-", Ans)