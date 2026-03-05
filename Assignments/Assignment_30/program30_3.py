'''
    Description : write the program which accepts an existing file name and display the
                  contents of the file line by line onthe screen

    Input       : ABC.txt  

    Author  : Rekha Shankarlal kumawat

    Date : 26 / 02 / 2026

'''
import sys
import os

def FileContent(fileName):

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

    for line_number , line in enumerate(fobj ,1):
        print(line) 
    
    fobj.close()
    

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

        elif((sys.argv[1] != "u" or sys.argv[1] != 'U' )):

            FileContent(sys.argv[1] )
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