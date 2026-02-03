import os

def main():

    FileName = input("Enter the name of file : ")

    Ret = os.path.exists(FileName)

    if(Ret == True):
        
        fobj = open(FileName , "r")
        print("file get successfully opened")

    else:
        print("there is no such file")

if __name__ == "__main__":
    main()