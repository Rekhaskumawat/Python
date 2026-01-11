# Filter Mapp Reduce

from functools import reduce                            # for reduce function

def CheckEven(No):
    return (No % 2 == 0)

def Increament(No):
    return No+1

def Add(No1 , No2):
    return No1+No2

def main():

    Data = [11,10,15,20,22,27,30]
    print("Actual Data is :", Data)

    fData = list(filter(CheckEven , Data))
    print("Data After filter is :", fData)

    mData = list(map(Increament ,fData))
    print("Data after mapping is :", mData)
    
    rData = reduce(Add , mData)
    print("Data after reduce is :", rData)


if __name__ == "__main__":
    main()