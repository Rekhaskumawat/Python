
#types of function argument  (positional)

def Display(A,B,C,D):
    print(A ,B ,C ,D)

def main():
    #Display(10 ,20)                            -> not allowed positional argument Error (less arguments)
    #Display(10 ,20 ,30 ,40 ,50)                -> not allowed positional argument Error (Extra arguments)

    Display(10 ,20 ,30,40)                      # allowed

if __name__ == "__main__":
    main()