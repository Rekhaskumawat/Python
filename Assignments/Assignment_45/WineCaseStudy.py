'''
    Description : 

            Step 1 : Get Data 
            Step 2 : Clean , prepare and Manuplate Data 
            Step 3 : Train Dataset
            Step 4 : Caluculate Accuracy 

    Author : Rekha Shankarlal Kumawat

    Date : 10 / 03 / 2026
    
'''

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix , classification_report , ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler


def MarvellousWineCaseStudy(Dataset):

    Border = "-"*50
    #-------------------------------------------------------------------
    # Step 1 : Load Dataset from CSV file
    #-------------------------------------------------------------------
    print(Border)
    print("Step 1 : Load Dataset from CSV file")
    print(Border)

    df = pd.read_csv(Dataset)
    print("Shape of the Dataset :- ", df.shape)
    print("Some Records from Dataset are :-")
    print(df.head())

    #-------------------------------------------------------------------
    # Step 2 : Clean the data set by removing empty rows
    #-------------------------------------------------------------------
    print(Border)
    print("Step 2 : Clean the data set by removing empty rows")
    print(Border)

    df.dropna(inplace=True)
    print("total Records :- ",df.shape[0])
    print("Toatal Columns :- ", df.shape[1])

    #-------------------------------------------------------------------
    # Step 3 : Split the Independent and Dependent variable
    #-------------------------------------------------------------------
    print(Border)
    print("Step 3 : Split the Independent and Dependent variable")
    print(Border)

    X= df.drop(columns= ['Class'])
    Y = df['Class']

    print("Shape of Independent Variables :- ", X.shape)
    print("Shape of Dependent Variable :- ", Y.shape)

    print(Border)
    print("Input Columns :- \n" , X.columns.tolist())
    print("Output Columns :- Class" )

    #-------------------------------------------------------------------
    # Step 4 : Split the Data for Training and Testing
    #-------------------------------------------------------------------
    print(Border)
    print("Step 4 : Split the Data for Training and Testing")
    print(Border)

    X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size= 0.2 , random_state= 42 , stratify=Y)
    
    print("Information of the Training and Testing Dataset ")
    print("X_train shape :- ", X_train.shape)
    print("X_test shape :- ", X_test.shape)
    print("Y_train shape :- ", Y_train.shape)
    print("Y_test shape :- ", Y_test.shape)

    #-------------------------------------------------------------------
    # Step 5 : Feature Scaling
    #-------------------------------------------------------------------
    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)  

    scaler = StandardScaler()

    #-------------------------------------------------------------------
    # Step 6 : Independent variable Scaling
    #-------------------------------------------------------------------
    print(Border)
    print("Step 6 : Independent variable Scalingg")
    print(Border)  

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    print("feturing Scalling is Done")

    #-------------------------------------------------------------------
    #   step 7 : Explore the Multiple values of K(K = Hyperparameter tuning)
    #-------------------------------------------------------------------
    print(Border)
    print("Step 7 : Explore the Multiple Values of K ")
    print(Border)

    accuracy_scores = []
    K_values = range(1,21)

    for K in K_values:
        model = KNeighborsClassifier(n_neighbors=K)
        model.fit(X_train_scaled , Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test , Y_pred)
        accuracy_scores.append(accuracy)

    print(Border)
    print("Accuracy report of all K values 1 to 20 ")
    for value in accuracy_scores:
        print(value)

    #-------------------------------------------------------------------
    #step 8 : Plot graph of K vs Accuracy
    #-------------------------------------------------------------------

    print(Border)
    print("Step 8 : Plot graph of K vs Accuracy ")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values , accuracy_scores , marker = 'o')
    plt.title(" k value Vs Accuracy")
    plt.xlabel("K_value ")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()

    #-------------------------------------------------------------------
    #step 9 : Find Best Value of K
    #-------------------------------------------------------------------

    print(Border)
    print("Step 9 : Find Best Value of K ")
    print(Border)

    best_k = list(K_values)[accuracy_scores.index(max(accuracy_scores))]
    print("Best Value of K is : ", best_k)

    #-------------------------------------------------------------------
    # step 10 : Build final model using best value of K
    #-------------------------------------------------------------------

    print(Border)
    print("Step 10 : Build final model using best value of K ")
    print(Border)

    final_model = KNeighborsClassifier(n_neighbors=best_k)
    final_model.fit(X_train_scaled , Y_train)

    Y_pred = final_model.predict(X_test_scaled)

    #-------------------------------------------------------------------
    #step 11 : Calculate final Accuracy
    #-------------------------------------------------------------------

    print(Border)
    print("Step 11 : Calculate final Accuracy ")
    print(Border)

    accuracy = accuracy_score(Y_test , Y_pred)

    print("Accurracy of model is : ", accuracy*100)

    #-------------------------------------------------------------------
    #step 12 : Display Confussion Matrix
    #-------------------------------------------------------------------
    print(Border)
    print("Step 12 : Display Confussion Matrix ")
    print(Border)

    cm = confusion_matrix(Y_test , Y_pred)
    print("Confusion Matrix :- \n",cm)

    #-------------------------------------------------------------------
    #step 13 :Display Classification report
    #-------------------------------------------------------------------

    print(Border)
    print("Step 13 :Display Classification report ")
    print(Border)

    print(classification_report(Y_test , Y_pred))
    
def main():

    MarvellousWineCaseStudy("WinePredictor.csv")

if __name__ == "__main__":
    main()