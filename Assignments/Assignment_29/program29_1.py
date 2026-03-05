"""
Description : Program which accepts a file name from the user and checks whether that 
              file exists in the current directory or not

Author      : Rekha Shankarlal Kumawat

Date        :   26 / 02 / 2026

"""

import os

def Chkfile(FileName):
    
    bRet = False

    bRet = os.path.isfile(FileName)

    return bRet
    
def main():
    
    FileName = '\0'
    bRet = False

    print("Enter the file Name :- ")
    FileName = input()

    bRet = Chkfile(FileName)

    if bRet == True:
        print("File Exists")
    
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()