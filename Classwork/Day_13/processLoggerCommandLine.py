
# Command Line input

import psutil
import sys

def main():
    Border = "-"*50
    print (Border)
    print("-----Marvellous Platform Surveillance System -----")
    print(Border)

    if(len(sys.argv) == 2):

        # python3 Demo.py --h

        if((sys.argv[1]) == "--h" or (sys.argv[1])== "--H"):
            print("This script is used to :")
            print("1 : create automatic logs")
            print("2 : Executes periodically")
            print("3 : Sends mail with the log")
            print("4 : Store information about process")
            print("5 : Store information about CPU")
            print("6 : Store information about RAM usages")
            print("7 : Store  information about Secondary Storage")

        # python3 Demo.py --u

        elif((sys.argv[1]) == "--u" or (sys.argv[1])== "--U"):
            print("use the automation script as")
            print("ScritName.py TimeInterval DirectoryName")
            print("TimeInterval : the time in minutes for periodic scheduling")
            print("DirectoryName : Name of Directory to create auto logs")

        # python3 Demo.py --k

        else:
            print("Unable to proceed as there is no such option")
            print("please use --h or --u to get more detail")
    
    #python3 Demo.py 5 log

    elif(len(sys.argv) == 3):
        print("Inside projrct logic")
        print("Time Interval : ",sys.argv[1])
        print("Directory Name : ",sys.argv[2])

    else:

        print("Invalid Number of CommandLine Arguments")
        print("Unable to proceed as there is no such option")
        print("please use --h or --u to get more detail")        


    print(Border)
    print("------- Thank you for using our script -----------")
    print(Border)



if __name__ == "__main__":
    main()