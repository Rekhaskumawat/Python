# matplotlib  is used for visualisation

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def main():

    dobj = pd.DataFrame(
        {
            "A" : [1,2,3],
            "B" : [4,2,6],
            "C" : [7,8,9]
        }
    )

    print(dobj)
    
    # Feature correlation

    sns.heatmap(dobj.corr() ,annot =True)

    plt.show()

if __name__ == "__main__":
    main()