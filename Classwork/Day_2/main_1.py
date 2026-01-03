# way of writting the code

def Multiplication(iValue1 , iValue2):
    iAns = 0                                                         #local Variable of Multiplication
    iAns = iValue1*iValue2
    return iAns

def main():

    iNo1 = 0                                                            # local variable of main
    iNo2 = 0 
    iRet = 0 

    iNo1 = int(input("Enter first number:- "))                         

    iNo2 = int(input("Enter second number:- "))

    iRet = Multiplication(iNo1 , iNo2)                           
    print("Multipication is :-", iRet)

main()                                                                     # call of main function
