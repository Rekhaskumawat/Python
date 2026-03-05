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

def FileData(fileName):

    Ret = False

    Ret = os.path.exists(fileName)

    if(Ret == False):
        print("there is no such file in directory")
        return
    
    Ret = os.path.isfile(fileName)

    if(Ret == False):
        print("Its not a file")
        return
    
    ofobj = open(fileName , 'r')

    fobj = open("Demo.txt" , 'w')

    data = ofobj.read()

    fobj.write(data)

    fobj.close()
    ofobj.close()
    

def main():
    
    Border = "-"*40
    
    print(Border)

    if(len(sys.argv) == 2):

        if((sys.argv[1]) == "--u" or (sys.argv[1]) == "--U"):
            print("use the given script as")
            print("ScriptName.py Filename ")

        elif((sys.argv[1] != "u" or sys.argv[1] != 'U' )):

            FileData(sys.argv[1])
            print("Data successfully copied")
            print(Border)

        else:
            print("Use the given flags as:")
            print("--u : Used to display the usage")

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as:")
        print("--u : Usd to display the usage")


if __name__ =="__main__":
    main()