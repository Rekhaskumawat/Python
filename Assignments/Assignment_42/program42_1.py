'''
    Description :- Implement Simple Linear Regression manually without using any ML library

    Dataset :
                X = [1,2,3,4,5]
                Y = [3,4,2,4,5]
    
    Task : 
                1. Mean of X (x_bar)
                2. Mean of Y (y_bar)
                3. Slope (m)
                4. Intercept(c)
    
    Expected Output :-

                mean of X : 3
                mean of Y = 3.6

                slope(m) = 0.4
                Intercept (c) = 2.4

                Regression Equation : Y = 0.4X + 2.4

                Predicted Y for X = 6 : 4.8

    Author :-  Rekha Shankarlal Kumawat

    Date :- 11 /03 / 2026

'''
import numpy as np

def LinearRegressionX():

    #Load dataset
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("Mean of X :- ", mean_x)
    print("Mean of Y :- ", mean_y)

    n = len(X)

    # y = mx + c

    numerator = 0
    denominator = 0

    for i in range(n) :
        numerator = numerator + ((X[i]-mean_x)*(Y[i]-mean_y))
        denominator = denominator + ((X[i]-mean_x)**2)

    m = numerator / denominator

    print("Slope (m) : " , m)

    Intercept = mean_y - (m * mean_x)

    print("Intercept (c) : ", Intercept)

    print("Regrestion Equation : Y = " ,m ,"X + ", Intercept )

    x = int(input("Enter the value of X : "))

    y = m*x + Intercept

    print("Predicted Y for X = " ,x , "is : ", y)


def main():

    LinearRegressionX()

if __name__ == "__main__":
    main()