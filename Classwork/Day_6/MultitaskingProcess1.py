
# Multi processing

import time
import multiprocessing
import os

def SumEven(No):
    print("PID of SumEven :",os.getpid())               # 51
    print("PPID of SumEven :",os.getppid())             # 21
    sum = 0

    for i in range(2 ,No+1 ,2):
        sum = sum+i

    print("Even Sum is :",sum)

def SumOdd(No):
    print("PID of SumOdd :",os.getpid())                # 101
    print("PPID of SumOdd :",os.getppid())              # 21
    sum = 0

    for i in range(1 ,No+1 ,2):
        sum = sum+i

    print("Odd Sum is :",sum)

def main():
    print("PID of Main :",os.getpid())              # 21
    print("PPID of Main:",os.getppid())             #cmd  11
    start_time = time.time()

    thread1 = multiprocessing.Process(target=SumEven , args=(100000000,))
    thread2 = multiprocessing.Process(target=SumOdd , args=(100000000,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end_time = time.time()

    print("Execution time :",end_time - start_time)
    
if __name__ == "__main__":
    main()