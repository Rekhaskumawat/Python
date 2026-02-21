
# DataFrame is like 2D Array in c/c++/java

import pandas as pd

def main():

    Data = {
            "Name" : ["Sagar","Amit","Pooja"],
            "Age" : [23,26,25],
            "City" :["Pune","Mumbai","Satara"]
        }

    dobj = pd.DataFrame(Data)

    print(dobj.loc[0])          # loc = row fetch specific row data

    
if __name__ == "__main__":
    main()
