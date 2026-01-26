#############################################################################
#   
#   Description : > All thread should Accept a string as input
#                 > the Small thread should count and 
#                       display the number of lowercase chracter
#                 > the Capital thread should count and 
#                       display the number of Uppercase chracter
#                 > the Digit thread should count and 
#                       display the number of numeric Digit
#                 > Each thread must display thread name and thread id
#
#   Author      : Rekha Shankarlal Kumawat 
#
#   Date        : 26 / 10 / 2026
#
############################################################################

import threading

def Small(str):

    print(f"Current thread {threading.current_thread().name} and Thread ID {threading.current_thread().ident}")

    count = 0
    for i in range(len(str)):
        if(str[i] >=  'a' and str[i] <= 'z'):
            count = count+1
        
    print("Number of lowercase characters are:-", count)

def Capital(str):

    print(f"Current thread {threading.current_thread().name} and Thread ID {threading.current_thread().ident}")

    count = 0
    for i in range(len(str)):
        if(str[i] >=  'A' and str[i] <= 'Z'):
            count = count+1
        
    print("Number of Uppercase characters are:-", count)

def Digit(str):

    print(f"Current thread {threading.current_thread().name} and Thread ID {threading.current_thread().ident}")

    count = 0

    for i in range(len(str)):
        if((str[i]) >=  '0' and (str[i]) <= '9'):
            count = count+1
        
    print("Number of Digits are:-", count)

def main():

    data =""
    print("Enter a string:-")

    data = input()

    small = threading.Thread(target= Small, args = (data ,))
    capital = threading.Thread(target= Capital, args= (data ,))
    digit = threading.Thread(target=Digit , args=(data ,))

    small.start()
    capital.start()
    digit.start()

    small.join()
    capital.join()
    digit.join()

    

if __name__ =="__main__":
    main()

############################################################################
#
#   Enter a String :- Marvellous123
#   Current thread Thread-1 (Small) and Thread ID __________________
#   Number of lowercase characters are:- 9
#   Current thread Thread-1 (Capital) and Thread ID __________________
#   Number of Uppercase characters are:- 1
#   Current thread Thread-1 (Digit) and Thread ID __________________
#   Number of Digits are:- 3
#
############################################################################
