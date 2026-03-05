'''
    Description :write the program which accept two file names through command line arguments
                 and compare the contents of both files.

                    -> if both files contents the same contents , display Success
                    -> otherwise display failure

    Input       : ABC.txt Demo.txt

    Expected output : Success OR Failure

    Author  : Rekha Shankarlal kumawat

    Date : 26 / 02 / 2026

'''
import sys
import os
import hashlib

def CompareContent(FileName1 , FileName2):

    Ret1 = False

    Ret1 = os.path.exists(FileName1)

    Ret2 = os.path.exists(FileName2)

    if((Ret1 and Ret2) == False):
        print("there is no such file in directory")
        return
    
    Ret1 = os.path.isfile(FileName1)

    Ret2 = os.path.isfile(FileName2)

    if((Ret1 and Ret2) == False):
        print("Its not a file")
        return
    
    fobj1 = open(FileName1 , 'rb')
    hobj1 = hashlib.md5()


    Buffer = fobj1.read(1000)

    while(len(Buffer) > 0):
        hobj1.update(Buffer)
        Buffer = fobj1.read(1000)

    fobj2 = open(FileName2 , 'rb')
    hobj2 = hashlib.md5()

    Buffer = fobj2.read(1000)

    while(len(Buffer) > 0):
        hobj2.update(Buffer)
        Buffer = fobj2.read(1000)

    if(hobj1.hexdigest() == hobj2.hexdigest()):
        print("Success :Content of both the file is same")

    else:
        print("Failure : Content of both the file is not same")

        fobj2.close()
        fobj1.close()


    fobj2.close()
    fobj1.close()
    

def main():
    
    Border = "-"*40
    
    print(Border)

    if(len(sys.argv) == 2):

        if((sys.argv[1]) == "--h" or (sys.argv[1]) == "--H"):
            print("This application is used to compare the content")

        elif((sys.argv[1]) == "--u" or (sys.argv[1]) == "--U"):
            print("use the given script as")
            print("ScriptName.py Argument1 Argument2")
            print("Argument1 : file1")
            print("Argument2 : filetocomparewith")

        else:
            print("Use the given flags as:")
            print("--u : Usd to display the usage")
            print("--h : Used to display the help")

    elif(len(sys.argv) == 3):

        CompareContent(sys.argv[1] , sys.argv[2] )
        print(Border)

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as:")
        print("--u : Usd to display the usage")
        print("--h : Used to display the help")

if __name__ =="__main__":
    main()