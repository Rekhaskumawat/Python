
import os
import sys

def DirctoryScanner(DirName = "Marvellous"):
    
    Ret =True

    Ret = os.path.exists(DirName)

    if(Ret == False):
        print("there is no such dirctory")
        return
    
    Ret = os.path.isdir(DirName)

    if(Ret == False):
        print("It is not a dirctory")
        return
    
    FileCount = 0
    EmptyFileCount = 0

    for FolderName , SubFolder ,FileName in os.walk(DirName):

        for fname in FileName:
            FileCount = FileCount + 1

            fname = os.path.join(FolderName ,fname)
            print(f"FileName :{fname}  , FileSize : {os.path.getsize(fname)}")  

            if(os.path.getsize(fname) == 0):                #Empty file
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fname)

    Border = "-"*50
    print(Border)
    print("------------------Automation Report---------------")
    print("Toatal File Scanned:", FileCount)
    print("Total Empty File Found :",EmptyFileCount)
    print(Border)
                                                         
            
def main():

    Border = "-"*50
    print(Border)
    print("----------Marvellous Directory Automation---------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number of Arguments")
        print("Please specify the name of directory")
        return
    
    DirctoryScanner(sys.argv[1])

    print(Border)
    print("----------Marvellous Directory Automation---------")
    print(Border)


if __name__ == "__main__":
    main()