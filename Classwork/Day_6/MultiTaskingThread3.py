
# Multi threading thread

import threading

def Display():
    print("Inside Display Function :", threading.get_ident())

    for i in range(100):
        print("Inside Display")

def main():
    print("inside main :",threading.get_ident())

    thread = threading.Thread(target=Display)
    thread.start()

    print("End of main")

if __name__ == "__main__":
    main()