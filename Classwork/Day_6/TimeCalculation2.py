
# calculate the execution time of process

import time

def Factorial(No):

    fact = 1

    for i in range(1,No+1):
        fact = fact*i

    return fact

def main():
    
    value = 0
    Ret = 0
    print("Enter a Number:-")
    value = int(input())

    start_time = time.time()

    Ret = Factorial(value)

    end_time = time.time()

    print("Factorial is :",Ret)

    print("total Execution time is :", end_time - start_time)

if __name__ == "__main__":
    main()