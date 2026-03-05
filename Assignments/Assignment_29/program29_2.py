"""
Description : Program which accepts a file name from the user , open that file and display
              the entire contents on the console

Author      : Rekha Shankarlal Kumawat

Date        :   26 / 02 / 2026

"""

import os

def Chkfile(FileName):
    
    bRet = False

    bRet = os.path.isfile(FileName)

    return bRet

def FileContent(FileName):
    
    file = open(FileName , 'r')
    print("Data from file : \n" ,file.read())
    
def main():
    
    FileName = '\0'
    bRet = False

    print("Enter the file Name :- ")
    FileName = input()

    bRet = Chkfile(FileName)

    if bRet == True:
        print("File Exists")
        FileContent(FileName)
    
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()