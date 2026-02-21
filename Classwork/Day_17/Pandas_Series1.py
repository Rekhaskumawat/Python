# Series is like 1D Array in c/c++/java

import pandas as pd

def main():
    
    Data = [11,21,51,101,111]           # stores only homogenious data only

    print(Data)

    sobj = pd.Series(Data)

    print(sobj)

if __name__ == "__main__":
    main()