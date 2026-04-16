'''
    Description : Write a program using LinearRegression to trian a regression model using the dataset below.
    
                StudyHours           Marks
                    1                  50
                    2                  55
                    3                  60   
                    4                  65
                    5                  70
                    
                Your Program Should :
                                -> train the regression model
                                -> print the coefficient
                                -> print the intercept
                                
                Output :- coefficient (m) :  300.0
                            Intercept :  -840.0
                                
    Author :    Rekha Shankarlal Kumawat
    
    Date   :   16 / 04 / 2026
    
'''
import numpy as np

def LinearRegression():
    
    # Load the Dataset 

    X = [1 ,2 ,3 ,4 ,5]
    Y = [50 , 55 , 60 ,65 ,70]

    # mean of the Input And Output 

    x_mean = np.mean(X)
    y_mean = np.mean(Y)

    n = len(X)

    # Calculation for the Coefficient
    # y = mx + c
    # m = (summation((x - x_mean)*(y- y_mean)))/(summation(x-x_mean)**2)

    numerator = 0
    denomenator = 0

    for i in range(n):
        numerator = numerator + ((X[i]- x_mean)*(Y[i]*y_mean))
        denomenator = denomenator + ((X[i]-x_mean)**2)
        
    m = numerator / denomenator

    print("coefficient (m) : " , m)

    # Calculation of the Intercept
    # c = y - mx

    c = y_mean - (m*x_mean)

    print("Intercept (c) : " ,c)

def main():
    LinearRegression()
    
if __name__ == "__main__":
    main()