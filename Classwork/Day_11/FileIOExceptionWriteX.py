def main():

    try:

        fobj = open("Hello.txt" , "w")
        print("File gets succesfully opended")

        fobj.write("Jay Ganesh Marvellous...")

        fobj.close()

    except FileNotFoundError:

        print("Unable ro open file as there is no such file")
    
    finally:

        print("End of application")


if __name__ == "__main__":
    main()