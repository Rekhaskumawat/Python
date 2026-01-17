
# Multi threading thread

import threading

def Display():

    for i in range(10):
        print("Inside Display :",threading.get_ident())

def main():
    print("inside main :",threading.get_ident())

    thread1 = threading.Thread(target=Display)
    thread2 = threading.Thread(target=Display)

    thread1.start()
    thread2.start()
    
    thread2.join()
    thread1.join()

    print("End of main")

if __name__ == "__main__":
    main()