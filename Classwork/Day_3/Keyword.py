
#types of function argument  (Keyword)

def EmployeeInfo(Name , Age , Salary , City):
    print("Name : ",Name)
    print("Age : " ,Age)
    print("Salary : ",Salary)
    print("City :",City)

def main():

    #positional arguments

    #EmployeeInfo("Rahul",26,2700.50 ,"Pune")            # Correct
    #EmployeeInfo(26,"Rahul","pune",2700.50)             # Wrong

    # Kerword arguments

    EmployeeInfo(Age = 26 , Name = "Rahul", City= "Pune", Salary= 2700.50)      #correct
    
if __name__ == "__main__":
    main()