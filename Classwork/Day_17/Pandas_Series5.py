import pandas as pd

def main():

    # by default indexing is from 0 but we can customize the indexing it can be String

    sobj = pd.Series( [25000,27000,29000,30000], index=["PPA","LB","Python","React"])

    print(sobj)

    print(sobj["Python"])
    
if __name__ == "__main__":
    main()