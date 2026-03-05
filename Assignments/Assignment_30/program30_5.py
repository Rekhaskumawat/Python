'''
    Description : write the program which accepts an existing file name and one string
                 through command line arguments and check whether that word is present in
                 the file or not

    Input       : ABC.txt   Marvellous

    Expected output : 13

    Author  : Rekha Shankarlal kumawat

    Date : 26 / 02 / 2026

'''
import sys
import os

def StringMatch(fileName , Search):

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

    found = False

    for line_number , line in enumerate(fobj ,1):
        if Search in line:
            found = True
            break 

    fobj.close()

    return found
    

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

        else:
            print("Use the given flags as:")
            print("--u : Usd to display the usage")
            print("--h : Used to display the help")

    elif(len(sys.argv) == 3):

        Ret = StringMatch(sys.argv[1] , sys.argv[2] )
        if Ret == True:
            print("String found")
        else:
            print("String not found")
        print(Border)

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as:")
        print("--u : Usd to display the usage")
        print("--h : Used to display the help")


if __name__ =="__main__":
    main()