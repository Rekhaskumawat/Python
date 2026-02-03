
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
    
    for FolderName , SubFolder ,FileName in os.walk(DirName):
        for fname in FileName:
            print(f"FileName :{fname}  , FileSize : {os.path.getsize(fname)}")     #Error 
                                                        # getsize -> path issue
            
def main():

    Border = "-"*40
    print(Border)
    print("----------Marvellous Automation---------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number of Arguments")
        print("Please specify the name of directory")
        return
    
    DirctoryScanner(sys.argv[1])

if __name__ == "__main__":
    main()