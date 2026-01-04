# function with multiple argumnent and one return value

#   Accept : multiple argument
#   Return:  one value

def Marvellous1(value1 , value2):
    print("Inside marvellous1 function:", value1, value2)
    return 11

def main():
    Ret = None
    Ret = Marvellous1("python" ,21)
    print("Return value is :", Ret)

if __name__ == "__main__":
    main()