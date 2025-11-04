
#  Prédiction du Diabète Gestationnel

## Objectif du projet
Ce projet vise à prédire la probabilité qu’une femme développe un **diabète gestationnel** à partir de données cliniques et comportementales.  
L’objectif est d’utiliser des algorithmes de **Machine Learning** pour identifier les variables les plus influentes et construire un modèle performant d’aide à la décision médicale.
---

##  Description du dataset

Le dataset contient des informations cliniques et comportementales sur des patientes, avec la variable cible :
- `Previous_Gestational_Diabetes` : 1 si la patiente a déjà eu un diabète gestationnel, 0 sinon.

###  Variables principales :
| Type | Variables |
|------|------------|
| **Numériques** | Age, BMI, Fasting_Blood_Glucose, HbA1c, Blood_Pressure_Systolic, Blood_Pressure_Diastolic, Cholesterol_Total, Dietary_Intake_Calories |
| **Catégorielles** | Ethnicity, Sex, Physical_Activity_Level, Smoking_Status, Alcohol_Consumption, Family_History_of_Diabetes |

---

## ⚙️ Étapes du projet

1. **Chargement et exploration des données**
   - Nettoyage des valeurs manquantes
   - Analyse statistique descriptive
   - Visualisation des distributions et corrélations

2. **Prétraitement**
   - Encodage des variables catégorielles  
   - Normalisation des variables numériques  
   - Séparation en ensemble d’entraînement et de test  

3. **Modélisation**
   - Entraînement de plusieurs modèles :
     - Régression logistique  
     - Random Forest  
     - KNN
   - Évaluation via : Accuracy, Precision, Recall, F1-score.

4. **Visualisation et interprétation** 
   - Matrice de confusion

5. **Application interactive**
   - Déploiement d’une interface sur **Streamlit** pour permettre une **prédiction en direct** à partir de valeurs saisies par l’utilisateur.

---

##  Technologies utilisées

| Domaine | Outils |
|----------|--------|
| Langage principal | Python |
| Bibliothèques ML | Scikit-learn|
| Prétraitement | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| Application web | Streamlit |
| Environnement | Jupyter Notebook |

---

## 📊 Résultats principaux

- **Meilleur modèle :** Logistic Regression
- **Accuracy :** ~0.52 
- **F1-score :** ~0.60
- - **Recall :** ~0.72 
- **Variables les plus importantes avec RFE :** Serum_Urate, Family_History_of_Diabete, Ethnicity_Black, Ethnicity_Hispanic,Ethnicity_White,Physical_Activity_Level_Low, Physical_Activity_Level_Moderate, Smoking_Status_Former, Smoking_Status_Never, Alcohol_Consumption_Moderate
  
---
---

## 👩‍💻 Auteur

**Maimouna Oiga**  
Étudiante en Master 2 Sciences et Ingénierie des Données  
📧 maimouna.oiga@gmail.com  

---

. 
