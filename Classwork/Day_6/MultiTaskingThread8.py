
# Multi threading thread

import threading

def Display(No):
    print("Inside Display :",No)

def main():
    thread = threading.Thread(target=Display ,args=(11,))    # (, )represent you can pass more args
    thread.start()

if __name__ == "__main__":
    main()