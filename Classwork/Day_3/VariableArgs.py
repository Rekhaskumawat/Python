
#types of function argument  (Variable no of arguments)

def Addition(*no):
    print(no)
    print(type(no))                 # tuple
    print(len(no))                  # 4

def main():
    Addition(11,21,51,101)
    
    
if __name__ == "__main__":
    main()