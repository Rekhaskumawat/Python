'''
    Description :- Implement Simple Linear Regression manually without using any ML library

    Dataset :
                Experience = [1,2,3,4,5]
                Salary = [20000 , 25000 , 30000 , 35000 , 40000]
    
    Task : 
                1. train linear regression 
                2. predict salary for 6 yers of experience
                3. plot regression line using matplotlib


    Author :-  Rekha Shankarlal Kumawat

    Date :- 11 /03 / 2026

'''
import numpy as np
import matplotlib.pyplot as plt

def LinearRegressionX():

    #Load dataset
    Experience = [1,2,3,4,5]
    Salary = [20000 , 25000 , 30000 , 35000 , 40000]
    

    mean_x = np.mean(Experience)
    mean_y = np.mean(Salary)

    print("Mean of X :- ", mean_x)
    print("Mean of Y :- ", mean_y)

    n = len(Experience)

    # y = mx + c

    numerator = 0
    denominator = 0

    for i in range(n) :
        numerator = numerator + ((Experience[i]-mean_x)*(Salary[i]-mean_y))
        denominator = denominator + ((Experience[i]-mean_x)**2)

    m = numerator / denominator

    Intercept = mean_y - (m * mean_x)

    print("Regression Equation : Y = " ,m ,"X + ", Intercept )

    x = int(input("Enter Year of Experience : "))
    y = m*x + Intercept
    print("Predicted Salary for " , x ,"Years Experience : ", y)
    x = np.linspace(1,6,n)
    y = m*x + Intercept


    plt.plot(x,y,color = 'g' , label ="Regression Line")
    plt.scatter(Experience,Salary , color = 'r' , label = "Scatter plot")

    plt.xlabel("Experience : Independent Variable")
    plt.ylabel("Salary : dependent Variable")

    plt.legend()
    plt.show()

    ''' Y_P = []
    for i in range(n):
        y = m * Experience[i] + Intercept
        Y_P.append(y)
 

    for i in range(n):
        numerator = numerator + ((Y_P[i] - mean_y)**2)
        denominator = denominator + ((Salary[i] - mean_y)**2)

    r2 = numerator/ denominator

    print("Value of R^2 Score :- ", r2)

    # MSE = summation((Y - Y_P)**2)/n

    for i in range(n):
        numerator = numerator + ((Y[i] - Y_P[i])**2)

    MSE = numerator/n

    print("Mean Squared Error (MSE) : ", MSE)'''



def main():

    LinearRegressionX()

if __name__ == "__main__":
    main()