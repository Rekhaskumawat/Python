# function with multiple argumnent and multiple return value

#   Accept : multiple argument
#   Return:  multiple value

def Marvellous1(value1 , value2):
    print("Inside marvellous1 function:", value1, value2)
    return 11,21,51

def main():
    Ret1 = None
    Ret2 = None
    Ret3 = None
    Ret1 , Ret2 , Ret3 = Marvellous1("python" ,21)
    print("Return value1 is :", Ret1)
    print("Return value2 is :", Ret2)
    print("Return value3 is :", Ret3)

if __name__ == "__main__":
    main()