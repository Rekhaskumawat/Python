
#types of function argument  (Default)

def EmployeeInfo(Name , Age , Salary , City = "pune"):
    print("Name : ",Name)
    print("Age : " ,Age)
    print("Salary : ",Salary)
    print("City :",City)

def main():

    EmployeeInfo("Rahul", 25 ,2000.50)      #correct
    EmployeeInfo("Rahul", 25 ,2000.50 , "Mumbai")
    
if __name__ == "__main__":
    main()