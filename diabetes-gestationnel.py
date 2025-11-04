# Import des bibliothèques nécessaires
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
# Chargement du dataset
data = pd.read_csv('C:/Users/hp/Desktop/datasets/diabetes_dataset.csv')
# un Aperçu des données
#print("Aperçu des premières lignes :")
#print(data.head())
# la Taille du dataset
#print("\nDimensions du dataset :", data.shape)
#parcourir la dataset
#data.info()
#print(data.describe(include="all"))
#print(data.isnull().sum())
#print("le nombre de duplication:",data.duplicated().sum())
#print(data['Sex'].unique())  # Afficher les valeurs uniques de sex
#flitrage du dataset 
females= data[data['Sex'] == 'Female']
#print(females.iloc[109])#affichage d'une ligne
#print("Aperçu des premières lignes :")
#print(females.head())
#females.info()
#matrice de correlation 
#numeric =females.select_dtypes(include=['number'])
#corr_matrix =numeric.corr()
#plt.figure(figsize=(10, 8))  # Ajustez la taille de l'image selon vos besoins
#sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
#plt.title("Matrice de Corrélation")
#plt.show()
#modification apportées
#females['Alcohol_Consumption'].fillna(females['Alcohol_Consumption'].mode()[0],inplace=True)
#suppression des colonnes
colonne_supprimés =['Unnamed: 0','Cholesterol_LDL','Cholesterol_HDL','Waist_Circumference']
Females=females.drop(columns=colonne_supprimés)
print("\nDimensions du dataset :", Females.shape)
print(Females.head())