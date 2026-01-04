
#types of function argument  (Default)

def EmployeeInfo(Name , Age , Salary , City = "pune"):
    print("Name : ",Name)
    print("Age : " ,Age)
    print("Salary : ",Salary)
    print("City :",City)

def main():

    EmployeeInfo(Age = 26 , Name = "Rahul", Salary= 2700.50)      #correct
    
if __name__ == "__main__":
    main()