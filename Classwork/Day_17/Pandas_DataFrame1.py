
# DataFrame is like 2D Array in c/c++/java

import pandas as pd

def main():

    Data = {
            "Name" : ["Sagar","Amit","Pooja"],
            "Age" : [23,26,25],
            "City" :["Pune","Mumbai","Satara"]
        }

    dobj = pd.DataFrame(Data)

    print(dobj)

    
if __name__ == "__main__":
    main()


'''
        Name    Age    City
    
    0   Sagar   23     Pune
    1   Amit    26     Mumbai
    2   Pooja   25     Satara

    
'''