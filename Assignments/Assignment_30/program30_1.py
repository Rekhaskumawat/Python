'''
    Description : writ a program which accept the file name from user and count how many lines
                  are present in the file.

    Input       : ABC.txt 

    Expected output : 13

    Author  : Rekha Shankarlal kumawat

    Date : 26 / 02 / 2026

'''
import sys
import os

def Countline(fileName ):

    Ret = False

    Ret = os.path.exists(fileName)

    if(Ret == False):
        print("there is no such file in directory")
        return
    
    Ret = os.path.isfile(fileName)

    if(Ret == False):
        print("Its not a file")
        return
    
    fobj = open(fileName , 'r')

    lines = fobj.readlines()
    line_count = len(lines)
    
    fobj.close()

    return line_count
    

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
            print("Argument2 : String")

        elif((sys.argv[1]) != '--h' and (sys.argv[1]) != '--u' ):

            Ret = Countline(sys.argv[1] )
            print("Number of lines : ", Ret)
            print(Border)

        else:
            print("Use the given flags as:")
            print("--u : Usd to display the usage")
            print("--h : Used to display the help")

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as:")
        print("--u : Usd to display the usage")
        print("--h : Used to display the help")


if __name__ =="__main__":
    main()