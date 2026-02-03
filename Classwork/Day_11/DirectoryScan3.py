import os

def DirectoryScanner(DirectoryName = "Marvellous"):

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("there is no such directory ")
        return

    print("Content of the directory are :-")


    for FolderName , SubFolderName , FileName in os.walk(DirectoryName):
        print("FolderName :" , FolderName)
        
        for Subf in SubFolderName:
            print("SubFolderName :",Subf)

        for fname in FileName:
            print("FileName :" , fname)

def main():
    DirectoryName = input("Enter the name of directory:")

    DirectoryScanner(DirectoryName)
    
if __name__ == "__main__":
    main()