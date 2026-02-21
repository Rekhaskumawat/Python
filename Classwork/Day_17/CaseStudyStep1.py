
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


