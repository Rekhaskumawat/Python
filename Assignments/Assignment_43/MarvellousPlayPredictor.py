'''
    Description :- 

        Step 1:

            Get Data
            Load data from MarvellousInfosystems_PlayPredictor.csv file into python application.

        Step 2:

            Clean, Prepare and Manipulate data

            As we want to use the above data into machine learning application we have to prepare it in the format which is accepted by the algorithms.
            As our dataset contains two features as Weather and Temperature, we have to replace each string field into numeric constants by using LabelEncoder from processing module of sklearn.

        Step 3:

            Train Data

            Now we want to train our data. For that we have to select the Machine Learning algorithm.
            For that we select K Nearest Neighbour algorithm.
            Use fit() method for training purpose.
            For training use whole dataset.

        Step 4:

            Test Data

            After successful training now we can test our trained data by passing some value of weather and temperature.
            As we are using KNN algorithm use value of K = 3.
            After providing the values check the result and display on screen.
            Result may be Yes or No.

    Author :- Rekha Shankarlal Kumawat 

    Date   :- 10 / 03 / 2026           
            
'''


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix ,accuracy_score , ConfusionMatrixDisplay , classification_report
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def MarvellousPlayPredict(Dataset):

    Border = "-"*50
    #--------------------------------------------------------------
    # Step 1 : Load Datset
    #--------------------------------------------------------------
    print(Border)
    print("Step 1 : Load Datset")
    print(Border)

    df = pd.read_csv(Dataset)

    print("Data Loaded Successfully..")
    print("Some Records from the Dataset :- ")
    print(df.head())

    #--------------------------------------------------------------
    # Step 2 : Remove the Unwanted Columns
    #--------------------------------------------------------------
    print(Border)
    print("Step  2 : Remove the Unwanted Columns")
    print(Border)

    print("Shape of the Dataset Before the Removal :- " , df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'] , inplace= True)

    print("Shape of Dataset after removal :-  " , df.shape)

    print(Border)
    print("Some Records After Removal :- ")
    print(df.head())
    print(Border)

    #--------------------------------------------------------------
    # Step 3 : Check Missing Values
    #--------------------------------------------------------------
    print(Border)
    print("Step  2 : Check Missing Values")
    print(Border)

    print("Missing Value Count :\n ", df.isnull().sum())

    #--------------------------------------------------------------
    # Step 4 : Split Dataset into Independent and Dependent Variables
    #--------------------------------------------------------------
    print(Border)
    print("Step 4 : Split Dataset into Independent and Dependent Variables")
    print(Border)

    le1 = LabelEncoder()
    le2 = LabelEncoder()
    le3 = LabelEncoder()

    df['Whether'] = le1.fit_transform(df['Whether'])
    df['Temperature'] = le2.fit_transform(df['Temperature'])
    df['Play'] = le3.fit_transform(df['Play'])

    X = df[['Whether' , 'Temperature']]
    Y = df['Play']

    print("Shape of Independent Variable :- ", X.shape)
    print('Shape of Dependent Variables :- ', Y.shape)

    #--------------------------------------------------------------
    # Step 5 : Split Dataset for training and Testing
    #--------------------------------------------------------------
    print(Border)
    print("Step 5 : Split Dataset for training and Testing")
    print(Border)

    X_train , X_test , Y_train , Y_test = train_test_split(X, Y  , random_state= 42)

    print("Shape of X_train :- ", X_train.shape)
    print("Shape of X_test :- ", X_test.shape)
    print("Shape of Y_train :- ", Y_train.shape)
    print("Shape of Y_test :- ", Y_test.shape)

    #--------------------------------------------------------------
    # Step 6 : Select the model
    #--------------------------------------------------------------
    print(Border)
    print("Step 6 : Select the model")
    print(Border)

    model = KNeighborsClassifier(n_neighbors= 3)
    model.fit(X_train , Y_train)

    Y_pred = model.predict(X_test)
    print("Actual Answer :- \n" , Y_test)
    print("Predicted Answer :- \n", Y_pred)

    #--------------------------------------------------------------
    # Step 7 : Calculate final Accuracy
    #--------------------------------------------------------------
    print(Border)
    print("Step 7 : Calculate final Accuracy")
    print(Border)

    accuracy = accuracy_score(Y_test , Y_pred)

    print("Accuracy of Model :- ", accuracy*100)

    #--------------------------------------------------------------
    # Step 8 : Confusion matrix
    #--------------------------------------------------------------
    print(Border)
    print("Step 8 : Confusion matrix")
    print(Border)

    cm = confusion_matrix(Y_test , Y_pred)
    print(cm)

    print("Classification Report :\n " , classification_report(Y_test , Y_pred))

    #--------------------------------------------------------------
    # Step 9 : Plot confusion matrix
    #--------------------------------------------------------------
    print(Border)
    print("Step 9 : plot confusion matrix")
    print(Border)

    Data = ConfusionMatrixDisplay(confusion_matrix= cm , display_labels=model.classes_)

    Data.plot()
    print("Confusion matrix of Marvellous Play Predictor ")
    plt.show()


def main():

    MarvellousPlayPredict("PlayPredictor.csv")

if __name__ == "__main__":
    main()