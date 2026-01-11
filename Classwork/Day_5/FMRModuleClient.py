# filter map reduce user defined Module

from MarvellousFMR import filterX , mapX , reduceX

CheckEven = lambda No : ((No % 2) == 0)
Increament = lambda No: (No+1)
Add = lambda No1 , No2: (No1+No2)

def main():

    Data = [11,10,15,20,22,27,30]
    print("Actual Data is :", Data)

    fData = list(filterX(CheckEven , Data))
    print("Data After filter is :", fData)

    mData = list(mapX(Increament ,fData))
    print("Data after mapping is :", mData)
    
    rData = reduceX(Add , mData)
    print("Data after reduce is :", rData)


if __name__ == "__main__":
    main()