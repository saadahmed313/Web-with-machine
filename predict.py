import streamlit as st
import pandas as pd
import pickle
import numpy as np

def show_predict_pag():
    st.write("Software Developer Stroke Prediction")
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)


    with open('preprocessing_pipeline.pkl', 'rb') as file:
        pre = pickle.load(file)



    out = {}
    age=st.text_input("Age")
    if age != "":
        try:
            out['age'] = float(age)   
        except:
            raise("the age must be a number")    
    out['hypertension'] = 1 if st.radio("Hypertension", ["Yes", "NO"]) == "Yes" else 0
    out['heart_disease'] = 1 if st.radio("Heart Disease", ["Yes", "NO"]) == "Yes" else 0

    out['gender']=st.selectbox("Gender", ["Male", "Female"])

    out['ever_married']=st.radio("Ever Married", ["Yes", "NO"])

    work_type = ["children", "Self-employed", "Private", "Govt_job", "Never_worked"]

    out['work_type']=st.selectbox("Work Type", work_type)
    out['Residence_type']=st.radio("Residence Type", ["Urban", "Rural"])

    avg_glucose_level=st.text_input("Avg Glucose Level")
    if avg_glucose_level != "":
        try:
            out['avg_glucose_level'] = float(avg_glucose_level)   
        except:
            raise("the avg glucose level must be a number")   

    bmi=st.text_input("BMI")
    if bmi != "":
        try:
            out['bmi'] = float(bmi)   
        except:
            raise("the bmi glucose level must be a number")   
    smoking_status = ["formerly smoked", "never smoked", "smokes"]          
    out['smoking_status']=st.selectbox("Smoking Status", smoking_status)
    ok = st.button("Predict")
    data = pd.DataFrame([out])
    if ok:
        re = pre.transform(data)
        
        st.write("The predict: " + ("Stroke" if model.predict(re)[0] else "Not Stroke"))