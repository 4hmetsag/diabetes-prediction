import streamlit as st
import numpy as np
import pandas as pd
import joblib

def set_background(image_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({image_path});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def load_model_and_scaler():
    
    #load model, scaler and column names
    model = joblib.load("models/loj_final_model.pkl")
    scaler, columns = joblib.load("models/scaler_with_columns.pkl")  
    return model, scaler, columns

def predict(model, scaler, columns, input_data):
    
    #scale and predict data
    input_data_df = pd.DataFrame((input_data), columns = columns)
    scaled_input_data_df = pd.DataFrame(scaler.transform(input_data_df), columns = columns)
    diabetes_pred_rate = round(model.predict_proba(scaled_input_data_df)[:,1][0] * 100, 2)
    return diabetes_pred_rate

def main():

    model, scaler, columns = load_model_and_scaler()    

    st.set_page_config(page_title="Diabetes Prediction", layout="centered")
    
    image_path = "https://img.freepik.com/premium-photo/topographic-map-geographic-mountain-relief-abstract-concept-graphic-element-geography-scheme_1259630-4.jpg?w=1380"
    set_background(image_path)
    
    st.title("🩺 Diabetes Prediction App")
    st.markdown("""
    Estimate your **diabetes risk** based on your clinical data.
    """)    

    #widgets
    glucose = st.number_input("Glucose Level", min_value=40, max_value=250, value=120)
    bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=70.0, value=25.0)
    preg = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=2)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
    age = st.number_input("Age", min_value=10, max_value=120, value=30)
    bp = st.number_input("Blood Pressure", min_value=20, max_value=200, value=70)
    
    input_data = np.array([[preg, glucose, bp, bmi, dpf, age]])
    
    #estimate button
    if st.button("🔍 Estimate"):
        diabetes_pred_rate = predict(model, scaler, columns, input_data)
     
        if diabetes_pred_rate <= 40:
            st.success("✅ Low Risk of Diabetes.")
            st.write("""
            Based on the information provided, your diabetes risk has been assessed as low, 
            with a **{}%** probability. Keep up with your good habits for continued health.
            """.format(diabetes_pred_rate))
        elif diabetes_pred_rate > 40 and diabetes_pred_rate <= 60:
            st.warning("⚠️ Moderate Risk of Diabetes.")
            st.write("""
            Based on the information provided, your diabetes risk has been assessed as moderate, 
            with a **{}%** probability. Track your health more closely and consider lifestyle changes.
            """.format(diabetes_pred_rate))
        else:
            st.error("‼️ High Risk of Diabetes.")
            st.write("""
            Based on the information provided, your diabetes risk has been assessed as high, 
            with a **{}%** probability. We strongly recommend consulting with a healthcare 
            professional for a more detailed evaluation and to discuss preventive measures."
            """.format(diabetes_pred_rate))
    
    #info
    st.markdown("---")
    st.caption("A simple machine learning model to predict diabetes. It was developed by using logistic regression.")

if __name__ == "__main__":
    main()
    
    
    
    
    