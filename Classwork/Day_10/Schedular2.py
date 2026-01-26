import time
import datetime
import schedule


def Fun():

    print("Inside fun at :",datetime.datetime.now())


def main():
    print("-------------inside marvellous Automationscript---------------")
    print("------------At: ",datetime.datetime.now(),"---------------------")

    schedule.every(20).seconds.do(Fun)

if __name__ == "__main__":
    main()