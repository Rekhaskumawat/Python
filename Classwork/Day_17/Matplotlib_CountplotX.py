# matplotlib  is used for visualisation

import matplotlib.pyplot as plt
import seaborn as sns

def main():

    sns.countplot(x=['C','C','C++','java','C++','Python','JavaScript','C++','Golang','C'])

    plt.show()

if __name__ == "__main__":
    main()