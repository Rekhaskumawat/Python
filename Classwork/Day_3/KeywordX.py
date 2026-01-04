
#types of function argument  (Keyword)

def EmployeeInfo(Name , Age , Salary , City):
    print("Name : ",Name)
    print("Age : " ,Age)
    print("Salary : ",Salary)
    print("City :",City)

def main():

    # Kerword arguments

    EmployeeInfo(Age = 26 , Name = "Rahul", City= "Pune", Salary= 2700.50)      #correct

    EmployeeInfo(Age = 26 , Name = "Rahul", City= "Pune", Salary= None)
    
if __name__ == "__main__":
    main()