def Multiplication(iValue1 , iValue2):
    iAns = 0                                    #local Variable of Multiplication
    iAns = iValue1*iValue2
    return iAns

print("Demo Application")

iNo1 = 10                                       # global variable
iNo2 = 11

iRet = 0

iRet = Multiplication(iNo1 , iNo2)
print("Multipication is :-", iRet)