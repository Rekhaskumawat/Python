
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

Border ="-"*40

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