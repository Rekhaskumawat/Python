####################################################################################
#   
#   Description : > Use a Lock to avoid the race condition
#                 > Each thread should increment the sharedcounter multiple time
#                 > display the final counter value after 
#                                 all thread complete the execution
#
#   Author      : Rekha Shankarlal Kumawat 
#
#   Date        : 26 / 10 / 2026
#
###################################################################################

import threading

Counter = 0

def Update(No):

    global Counter 

    for i in range(No):
        with threading.Lock():
            Counter = Counter+1



def main():

    value = 0
    global Counter 

    print("Enter a number:-")
    value = int(input())

    t1 = threading.Thread(target= Update , args=(value ,))
    t2 = threading.Thread(target= Update , args=(value ,))


    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Value of Counter after all thread complete execution:- ",Counter)

if __name__ =="__main__":
    main()

############################################################################
#
#   Enter a number :- 2000
#   Value of Counter after all thread complete execution:-4000
# 
############################################################################
