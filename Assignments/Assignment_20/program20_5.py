#############################################################################
#   
#   Description : > Create Thread1 and Thread2 
#                 > Thread1 should display number from 1 to 50
#                 > Thread2 should display number in reverse from 50 to 1
#                 > Ensure that thread start executing after thread1 complete
#                 > Use appropriate thread synchronization
#
#   Author      : Rekha Shankarlal Kumawat 
#
#   Date        : 26 / 10 / 2026
#
############################################################################

import threading

def Thread1():

    print("Thread1 output :-")
    for i in range(1 ,51):
        print(i , end=" ")

    print("")

def Thread2():

    print("thread 2 output:-")
    for i in range( 50 ,0 ,-1):
        print(i ,end=" ")

    print("")

def main():

    t1 = threading.Thread(target= Thread1)
    t2 = threading.Thread(target= Thread2)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    

if __name__ =="__main__":
    main()

############################################################################
#
#   Thread1 Output:- 1 2 3 4 5 6 7 8 9 10 11 2 ......... 48 49 50
#   Thread2 Output :- 50 49 48 47 46 45 44 ............. 4 3 2 1
#
############################################################################
