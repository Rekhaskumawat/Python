'''
    Description : write the program which accepts an existing file name through command line
                  arguments , creates a new file named "Demo.txt" , and copies all contents
                  from the given file into Demo.txt

    Input       : ABC.txt

    Expected output : Create Demo.txt and copy contents of ABC.txt into Demo.txt

    Author  : Rekha Shankarlal kumawat

    Date : 26 / 02 / 2026

'''
import sys
import os

def FileData(fileName1 , fileName2):

    Ret1 = False
    Ret2 = False

    Ret1 = os.path.exists(fileName1)

    Ret2 = os.path.exists(fileName2)
    
    if((Ret1 and Ret2) == False):
        fobj2 = open(fileName2 , 'w')
        print("there is no such file in directory")
        return
    
    Ret1 = os.path.isfile(fileName1)
    Ret2 = os.path.isfile(fileName2)


    if((Ret1 and Ret2)  == False):
        print("Its not a file")
        return
    
    fobj1 = open(fileName1 , 'r')

    data = fobj1.read()

    fobj2.write(data)

    fobj2.close()
    fobj1.close()
    

def main():
    
    Border = "-"*40
    
    print(Border)

    if(len(sys.argv) == 2):

        if((sys.argv[1]) == "--u" or (sys.argv[1]) == "--U"):
            print("use the given script as")
            print("ScriptName.py sourceFilename   destinationfilename")

        else:
            print("Use the given flags as:")
            print("--u : Used to display the usage")
        
    elif(len(sys.argv) == 3):

        FileData(sys.argv[1] , sys.argv[2])
        print("Data copied successfully")
        print(Border)

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as:")
        print("--u : Usd to display the usage")


if __name__ =="__main__":
    main()