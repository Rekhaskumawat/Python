
import hashlib
import os

def CalculateCheckSum(FileName):
    
    fobj = open(FileName ,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName = "Marvellous"):

    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such Directory")
        return
    ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not Directory")
        return

    Duplicate = {}

    for FolderName , SubFolderName ,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName , fname)
            CheckSum =CalculateCheckSum(fname)

            if(CheckSum in Duplicate):
                Duplicate[CheckSum].append(fname)

            else:
                Duplicate[CheckSum] = [fname]

    return Duplicate


def DeleteDuplicate(Path = "Marvellous"):

    MyDict = FindDuplicate(Path)
    result = list(filter(lambda X :len(X) >1 , MyDict.values()))

    count = 0
    iCnt = 0

    for value in result:
        for SubValue in value:
            count = count+1
            if(count >1):
                print("Delete file :", SubValue)
                os.remove(SubValue)
                iCnt = iCnt +1
        count = 0
        
    print("Total delete files :",iCnt)
        

def main():

    DeleteDuplicate()

if __name__ == "__main__":
    main()