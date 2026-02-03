import os

def main():

    FileName = input("Enter the name of file : ")

    Ret = os.path.isabs(FileName)

    if Ret == True:
        print("It is alsoute path")

    else:
        print("it is relative path")

if __name__ == "__main__":
    main()