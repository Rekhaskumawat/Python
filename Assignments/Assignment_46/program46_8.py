'''
    Description : Write a program using LinearRegression to trian a regression model using the dataset below.
    
                StudyHours    SleepHours       Marks
                    1            7              50
                    2            6              55
                    3            7              60   
                    4            6              65
                    5            8              70
                    
                Your Program Should :
                                -> train the regression model using this dataset
                                -> print the coefficient for both features
                                -> print the intercept
                                
    Output : coefficient (m1) :  300.0
             coefficient (m2) :  214.28571428571558
             Intercept (c) :  -2297.142857142866
                                
    Author :    Rekha Shankarlal Kumawat
    
    Date   :   16 / 04 / 2026
    
'''
import numpy as np

# Load the Dataset 

X1 = [1 ,2 ,3 ,4 ,5]
X2 = [7 ,6 ,7 ,6 ,8]
Y = [50 , 55 , 60 ,65 ,70]

# mean of the Input And Output 

x1_mean = np.mean(X1)
x2_mean = np.mean(X2)
y_mean = np.mean(Y)

n = len(X1)

# Calculation for the Coefficient
# y = m1x1 + m2x2 + c
# m = (summation((x - x_mean)*(y- y_mean)))/(summation(x-x_mean)**2)

numerator1 = 0
denomenator1 = 0

numerator2 = 0
denomenator2 = 0

for i1 in range(n):
    numerator1 = numerator1 + ((X1[i1]- x1_mean)*(Y[i1]*y_mean))
    denomenator1 = denomenator1 + ((X1[i1]-x1_mean)**2)
    
for i2 in range(n):
    numerator2 = numerator2 + ((X2[i2]- x2_mean)*(Y[i2]*y_mean))
    denomenator2 = denomenator2 + ((X2[i2]-x2_mean)**2)
    
m1 = numerator1 / denomenator1
m2 = numerator2 / denomenator2

print("coefficient (m1) : " , m1)
print("coefficient (m2) : ", m2)

# Calculation of the Intercept
# c = y - m1x1 + m2x2

c = y_mean - (m1*x1_mean) - m2*x2_mean

print("Intercept (c) : " ,c)
