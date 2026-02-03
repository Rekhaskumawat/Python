
import os
import sys
import time

def DirctoryScanner(DirName = "Marvellous"):

    Border = "-"*50
    timestamp = time.ctime()

    LogFileName = "Marvellous%s.log" %(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")
    fobj = open(LogFileName, "w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a Directory Cleaner Script\n")
    fobj.write(Border+"\n")
    
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
            #print(f"FileName :{fname}  , FileSize : {os.path.getsize(fname)}")  

            if(os.path.getsize(fname) == 0):                #Empty file
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fname)

    fobj.write("------------------Automation Report---------------\n")
    fobj.write("Toatal File Scanned: "+str(FileCount)+"\n")
    fobj.write("Total Empty File Found: "+str(EmptyFileCount)+"\n")
    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()                         
            
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