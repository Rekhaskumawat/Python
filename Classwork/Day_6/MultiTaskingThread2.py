
# Multi threading thread

import threading

def Display():
    print("Inside Display Function :", threading.get_ident())

def main():
    print("inside main :",threading.get_ident())

    thread = threading.Thread(target=Display)
    thread.start()

    print("End of main")

if __name__ == "__main__":
    main()