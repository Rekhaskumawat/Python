def Multiplication(iValue1 , iValue2):
    iAns = 0                                                         #local Variable of Multiplication
    iAns = iValue1*iValue2
    return iAns


iNo1 = 0                                                            # global variable
iNo2 = 0 
iRet = 0 

print("-------------------------------------------------------")

iNo1 = int(input("Enter first number:- "))                          #input can  perform both I/O operation

iNo2 = int(input("Enter second number:- "))

iRet = Multiplication(iNo1 , iNo2)                                  # function call
print("Multipication is :-", iRet)


print("-------------------------------------------------------")

iNo1 = int(input("Enter first number:- "))                          

iNo2 = int(input("Enter second number:- "))

iRet = Multiplication(iNo1 , iNo2)                                 
print("Multipication is :-", iRet)

print("-------------------------------------------------------")
