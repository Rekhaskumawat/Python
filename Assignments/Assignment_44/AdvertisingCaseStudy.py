'''
  Description :- 

    Step 1:
      Get Data

      Load data from MarvellousAdvertising.csv file into python application.
    
    Step 2:
      Clean, Prepare and Manipulate data

      As we want to use the above data into machine learning application we have to prepare that in the format which is accepted by the algorithms.
    
    Step 3:
      Train Data

      Now we want to train our data for that we have to select the Machine learning algorithm.
      For that we select Linear Regression algorithm from scikit-learn library.
      For training purpose divide the dataset into half part.
      Use train method to train our dataset.
    
    Step 4:
    
      Test the data
      
      Test data by passing the remaining half part of the dataset.
      
    Step 5:
      Display predicted values of Linear Regression algorithms as well as expected values which are provided by the dataset.

  Author :- Rekha Shankarlal Kumawat

  Date :- 10 / 03/ 2026
'''



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score

def MarvellousAdvertise(DataPath):

  Border = "_"*40
  #----------------------------------------------------------------------
  #  Step1: Load DataSet
  #----------------------------------------------------------------------
  print(Border)
  print("Step 1 : Load Dataset")
  print(Border)
  df = pd.read_csv("Advertising.csv")

  print("Few records from the Datasets :")
  print(df.head())

  #----------------------------------------------------------------------
  #  Step2: Remove Unwanted columns
  #----------------------------------------------------------------------

  print(Border)
  print("Step2 : Remove Unwanted columns")
  print(Border)

  print("Shape of dataset before removal : " , df.shape)

  if 'Unnamed: 0' in df.columns:
      df.drop(columns=['Unnamed: 0'] , inplace=True)
  
  print("Shape of dataset after removal : " , df.shape)

  print(Border)
  print("Clean Data Set Is :")
  print(Border)

  print(df.head())

  #----------------------------------------------------------------------
  #  Step3: Check Missing Values
  #----------------------------------------------------------------------
  
  print(Border)
  print("Step3 : Check Missing Values")
  print(Border)

  print("Missing vlaues count : ", df.isnull().sum())

  #----------------------------------------------------------------------
  #  Step4: Display Ststistical Data
  #----------------------------------------------------------------------
  
  print(Border)
  print("Step4: Display Ststistical Data")
  print(Border)

  print(df.describe())

  #----------------------------------------------------------------------
  #  Step5: Correlation between columns
  #----------------------------------------------------------------------
  
  print(Border)
  print("Step5: Correlation between columns")
  print(Border)

  print("correlation Matrix")
  print(df.corr())

  #----------------------------------------------------------------------
  #  Step6: Split Dataset into independent and dependent variables
  #----------------------------------------------------------------------
  
  print(Border)
  print("Step6: Split Dataset into independent and dependent variable")
  print(Border)

  X = df[['TV' , 'radio' , 'newspaper']]
  Y = df['sales']

  print("Shape of Independent Variable : ",X.shape)
  print("Shape of Dependent Variable : ", Y.shape)

  #----------------------------------------------------------------------
  #  Step7: split dataset for training and testing
  #----------------------------------------------------------------------
  
  print(Border)
  print("Step7:split dataset for training and testing")
  print(Border)

  X_train , X_test , Y_train ,Y_test = train_test_split(X,Y,test_size=0.5 , random_state= 42)

  print("X_train Shape : ", X_train.shape)
  print("X_test Shape : ", X_test.shape)
  print("Y_train Shape : ", Y_train.shape)
  print("Y_test Shape : ", Y_test.shape)

  #----------------------------------------------------------------------
  #  Step8: Create and trian the model
  #----------------------------------------------------------------------
  
  print(Border)
  print("Step8:Create and trian the model")
  print(Border)

  model = LinearRegression()
  model.fit(X_train , Y_train)

  #----------------------------------------------------------------------
  #  Step9: Test the model
  #----------------------------------------------------------------------
  
  print(Border)
  print("Step 9 :Test the model")
  print(Border)

  Y_pred = model.predict(X_test)

  #----------------------------------------------------------------------
  #  Step 10: evaluate the model
  #----------------------------------------------------------------------
  
  print(Border)
  print("Step 10 : Evaluate the model")
  print(Border)

  MSE = mean_squared_error(Y_test , Y_pred)
  RMSE = np.sqrt(MSE)
  R2 = r2_score(Y_test , Y_pred)

  print("Mean Squared Error : ", MSE)
  print("Root Mean Squared Error : " , RMSE)
  print("R Square Value : ",R2)

  #----------------------------------------------------------------------
  #  Step 11: Calculate Model Coefficient
  #----------------------------------------------------------------------
  
  print(Border)
  print("Step 11 : Calculate Model Coefficient")
  print(Border)

  for column , value in zip(X.columns , model.coef_):
    print(f"{column} : {value}")

  print("Intercept :", model.intercept_)

  #----------------------------------------------------------------------
  #  Step 12: Compare the Actual and Predicted Value
  #----------------------------------------------------------------------
  
  print(Border)
  print("Step 12: Compare the Actual and Predicted Value")
  print(Border)

  Result = pd.DataFrame({'Actual Sales  ': Y_test.values,
                        'Predicted sales ' : Y_pred})

  print(Result.head())

  #----------------------------------------------------------------------
  #  Step 13 : Plot Actual VS Predicted
  #----------------------------------------------------------------------
  
  print(Border)
  print("Step 13 : Plot Actual VS Predicted")
  print(Border)

  plt.figure(figsize= (8,5))
  plt.scatter(Y_test , Y_pred)
  plt.xlabel("Actual sales")
  plt.ylabel("Predicted sales")
  plt.title('Actual Sales VS Predicted Sales')
  plt.grid(True)
  plt.show()

def main(): 
  
  MarvellousAdvertise("Advertising.csv")

if __name__ == "__main__":
    main()