# Filter Mapp Reduce through lambda function

from functools import reduce                            # for reduce function

CheckEven = lambda No : ((No % 2) == 0)

Increament = lambda No: (No+1)

Add = lambda No1 , No2: (No1+No2)

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