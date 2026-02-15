from sklearn.datasets import load_iris

def main():
    print("Iris Classsification case study")

    Dataset = load_iris()

    #metadata of dataset
    print("Independent variables are :")
    print(Dataset.feature_names)

    print("dependent variables are :")
    print(Dataset.target_names)

if __name__ == "__main__":
    main()