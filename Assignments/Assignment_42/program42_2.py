'''
    Description :- Implement Simple Linear Regression manually without using any ML library

    Dataset :
                X = [1,2,3,4,5]
                Y = [3,4,2,4,5]
    
    Task : 
                1. predict all values of Y using regression equation
                2. Calculate:
                            Mean Squared Error
                            R^2 score
                show all intermidate calculation


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

    print("Regression Equation : Y = " ,m ,"X + ", Intercept )

    Y_P = []
    for i in range(n):
        y = m * X[i] + Intercept
        Y_P.append(y)
    
    print("Values of Y_P : ", Y_P)

    for i in range(n):
        numerator = numerator + ((Y_P[i] - mean_y)**2)
        denominator = denominator + ((Y[i] - mean_y)**2)

    r2 = numerator/ denominator

    print("Value of R^2 Score :- ", r2)

    # MSE = summation((Y - Y_P)**2)/n

    for i in range(n):
        numerator = numerator + ((Y[i] - Y_P[i])**2)

    MSE = numerator/n

    print("Mean Squared Error (MSE) : ", MSE)



def main():

    LinearRegressionX()

if __name__ == "__main__":
    main()