
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier , plot_tree

import seaborn as sns

from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border ="-"*60

######################################################################################
#
#   Step 1 : Load the Dataset
#
######################################################################################

print(Border)
print("Step1 : Load the Dataset")
print(Border)

DatasetPath ="iris.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded successfully...")
print("Initial entries from the Dataset...")
print(df.head())

######################################################################################
#
#   Step 2 : Data Analysis (EDA)
#
######################################################################################

print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape of Dataset : ",df.shape)
print("Column Names : ",list(df.columns))

print("Missing Values (per Columns) :",df.isnull().sum())

print("Class Distribution (Species count) : ",df["species"].value_counts())

print("Statistical Report of DataSet : ", df.describe())

######################################################################################
#
#   Step 3 : Decide independent and dependent variables 
#
######################################################################################

print(Border)
print("Step 3 : Decide independent and dependent variables")
print(Border)

# X : Independent variables/ Features
# Y : Dependent Variables / Lables

feature_cols = [
                 "sepal length (cm)",
                 "sepal width (cm)",
                 "petal length (cm)",
                 "petal width (cm)"
]

X = df[feature_cols]
Y = df["species"]

print(" X shape : ",X.shape)
print(" Y shape : ",Y.shape)

######################################################################################
#
#   Step 4 : Visualisation of DataSet 
#
######################################################################################

print(Border)
print("Step 4 : Visualisation of DataSet")
print(Border)

# Scatter plot

plt.figure(figsize=(7,5))           

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"] , temp["petal width (cm)"] , label = sp)

plt.title("Iris : Petal length vs Petal width")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()        # for the classification of species for the user
plt.grid(True)
plt.show()

######################################################################################
#
#   Step 5 : Split the Dataset for training and testing 
#
######################################################################################

print(Border)
print("Step 5 : Split the Dataset for training and testing")
print(Border)

# Test size = 20%
# Train size = 80%

X_train , X_test , Y_train , Y_test = train_test_split(
    X,
    Y,
    test_size = 0.5, 
    random_state= 42
)

print("Data spliting activity done : ")

print(" X - Independent : ",X.shape)              #(150 ,4)
print(" Y - Dependent : ",Y.shape)                  #(150 ,)

print(" X_train : ", X_train.shape)             #(120,4)
print(" X_test : ", X_test.shape)               #(30 ,4)

print(" Y_train : ", Y_train.shape)             #(120,)
print(" Y_test : ", Y_test.shape)               #(30,)

######################################################################################
#
#   Step 6 : Build the model 
#
######################################################################################

print(Border)
print("Step 6 : Build the model")
print(Border)


print("We are going to use DecisionTreeClassifier")

model = DecisionTreeClassifier(

        criterion= "gini",
        max_depth= 5,
        random_state= 42                    
)

print("Model Succesfully created : ", model)

######################################################################################
#
#   Step 7 : Train the model 
#
######################################################################################

print(Border)
print("Step 7 : Train the model")
print(Border)

model.fit(X_train , Y_train)
print("Model Training completed")

######################################################################################
#
#   Step 8 : Evaluate the model 
#
######################################################################################

print(Border)
print("Step 8 : Evaluate the model")
print(Border)

Y_pred = model.predict(X_test)


print("Model Evaluation (Testing) complete")

print(Y_pred.shape)

"""print("Expected Answer :")
print(Y_test)"""

print("Predicted Answer :")
print(Y_pred)

######################################################################################
#
#   Step 9 : Evaluate the model performance 
#
######################################################################################

print(Border)
print("Step 9 : Evaluate the model performance")
print(Border)

accuracy = accuracy_score(Y_test , Y_pred)
print("Accuracy of model is : ", accuracy*100)

cm = confusion_matrix(Y_test ,Y_pred) 
print("Confusin matrix :")
print(cm)
print()
#classification report

print("Classification Report ")
print(classification_report(Y_test ,Y_pred))