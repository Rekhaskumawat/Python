
# Command Line input

import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):

    Border = "-"*50
    print(Border)

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create the folder")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    
    FileName = os.path.join(FolderName ,"Marvellous_%s.log"%timestamp)
    print("Log file gets created with name :",FileName)

    fobj = open(FileName , "w")

    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Surveillance System -----\n")
    fobj.write("Log Created at :"+ time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("--------------------System Report ---------------\n")

    fobj.write(Border+"\n")

    fobj.write("CPU Usages : %s %% \n"%psutil.cpu_percent())

    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %% \n"%mem.percent)
    
    fobj.write(Border+"\n")

    fobj.write("\n Disk Usage Report \n")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s -> %s %% used\n" %(part.mountpoint , usage.percent))
        except:
            pass
    
    fobj.write(Border+"\n")

    net = psutil.net_io_counters()
    fobj.write("\n Network Usage Report \n")
    fobj.write("Sent : %.2f MB\n" %(net.bytes_sent / (1024*1024)))
    fobj.write("Recieve : %.2f MB\n" %(net.bytes_recv / (1024*1024)))
    fobj.write(Border+"\n")

    # process LOG

    fobj.write(Border+"\n")
    fobj.write("--------------------End of Log File---------------\n")
    fobj.write(Border+"\n")
    
   

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
        
        # Apply the scheduler

        schedule.every(int(sys.argv[1])).minutes.do(CreateLog , sys.argv[2])
        print(" Platform Surveillance System started succesfully")
        print("Directory Created with name : ",sys.argv[2])
        print("Time Interval in minutes : ",sys.argv[1])
        print("Press Ctrl + c to stop the Execution")

        # wait till abort

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:

        print("Invalid Number of CommandLine Arguments")
        print("Unable to proceed as there is no such option")
        print("please use --h or --u to get more detail")        


    print(Border)
    print("------- Thank you for using our script -----------")
    print(Border)



if __name__ == "__main__":
    main()