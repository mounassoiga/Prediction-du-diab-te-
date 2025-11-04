
import streamlit as st
import joblib
import pandas as pd


# Charger le pipeline entraîné
model = joblib.load('Diabétes_pipelines.joblib')

import streamlit as st
import pandas as pd
import joblib

# --- CSS pour personnaliser le style ---
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fa;
    }
    .title {
        font-size: 2em;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 1.2em;
        color: #34495e;
        margin-bottom: 20px;
    }
    .result-good {
        background-color: #e8f5e9;
        padding: 15px;
        border-radius: 10px;
        color: #2e7d32;
        font-weight: bold;
    }
    .result-bad {
        background-color: #fdecea;
        padding: 15px;
        border-radius: 10px;
        color: #c62828;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- Titre principal ---
st.markdown('<div class="title">Prédiction du Diabète Gestationnel</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Veuillez remplir les informations ci-dessous :</div>', unsafe_allow_html=True)



age = st.number_input("Âge", min_value=20, max_value=69, value=30)
bmi = st.number_input("Indice de Masse Corporelle (BMI)", min_value=24.0, max_value=40.0, value=25.0)
fbg = st.number_input("Glycémie à jeun (Fasting Blood Glucose)", min_value=70.0, max_value=200.0, value=90.0)
hba1c = st.number_input(" taux de glucose dans le sang HbA1c (%)", min_value=4.0, max_value=15.0, value=5.5)
bps = st.number_input("Pression artérielle systolique", min_value=90.0, max_value=179.0, value=120.0)
bpd = st.number_input("Pression artérielle diastolique", min_value=60.0, max_value=119.0, value=80.0)
chol = st.number_input("Cholestérol total", min_value=100.0, max_value=400.0, value=180.0)
calories = st.number_input("Apport calorique quotidien", min_value=2129.0, max_value=3399.0, value=2500.0)

# 🟦 Variables catégorielles
ethnicity = st.selectbox("Origine ethnique", ["White", "Black", "Asian", "Hispanic"])
sex = st.selectbox("Sexe", ["female"])  # uniquement femmes
activity = st.selectbox("Niveau d'activité physique", ["Low", "Moderate", "High"])
smoking = st.selectbox("Statut tabagique", ["never", "former", "current"])
alcohol = st.selectbox("Consommation d’alcool", ["Heavy", "Moderate"])
history = st.selectbox("Antécédent familiale de diabète ?", ["no", "yes"])
history_map = {"no": 0, "yes": 1}

# 🔧 Création du DataFrame
input_data = pd.DataFrame({
    'Age': [age],
    'BMI': [bmi],
    'Fasting_Blood_Glucose': [fbg],
    'HbA1c': [hba1c],
    'Blood_Pressure_Systolic': [bps],
    'Blood_Pressure_Diastolic': [bpd],
    'Cholesterol_Total': [chol],
    'Dietary_Intake_Calories': [calories],
    'Ethnicity': [ethnicity],
    'Sex': [sex],
    'Physical_Activity_Level': [activity],
    'Smoking_Status': [smoking],
    'Alcohol_Consumption': [alcohol],
    'Family_History_of_Diabetes':[history_map[history]],
})


# 🔮 Prédiction
if st.button("Prédire"):
    prediction = model.predict(input_data)[0]
    
    st.subheader("Résultat de la prédiction :")
    if prediction == 1:
        st.write("⚠️ Vous présentez un **risque de diabète gestationnel**. Nous vous recommandons de consulter un professionnel de santé.")
    else:
        st.write("✅ Vous **ne présentez pas de risque apparent** de diabète gestationnel selon les informations fournies.")








