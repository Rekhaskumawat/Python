# Filter Mapp Reduce through lambda function

from functools import reduce                            # for reduce function

def main():

    Data = [11,10,15,20,22,27,30]
    print("Actual Data is :", Data)

    fData = list(filter(lambda No : ((No % 2) == 0), Data))
    print("Data After filter is :", fData)

    mData = list(map(lambda No: (No+1),fData))
    print("Data after mapping is :", mData)
    
    rData = reduce(lambda No1 , No2: (No1+No2), mData)
    print("Data after reduce is :", rData)


if __name__ == "__main__":
    main()