# Addition of two number 
# by default variable is "str"

print("Enter first number :")
iValue1 = input()

print("Enter Secong Number :")
iValue2 = input()

print(type(iValue1))
print(type(iValue2))

iAns = int(iValue1) + int(iValue2)      #typeCasting

print(type(iValue1))
print(type(iValue2))

print("Addition is :" , iAns)