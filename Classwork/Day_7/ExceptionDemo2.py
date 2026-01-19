def main():

    Ans = 0
    try:

        print("Inside try block")

        print("Enter first number:")
        No1 = int(input())

        print("Enter Second number:")
        No2 = int(input())

        Ans = No1 / No2

    except:

        print("Inside except block")

    finally:

        print("Inside finally block")

    print("Division is: ",Ans)

if __name__ == "__main__":
    main()