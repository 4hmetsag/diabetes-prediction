# 🩺 Diabetes Prediction App

This app aims to predict whether a person is likely to have diabetes based on medical features such as glucose level, blood pressure, BMI, and age. It was developed using logistic regression.

## 🌐 Deploy Link

https://diabetes-prediction-app-0.streamlit.app/

## 🚀 Getting Started

These instructions will help you set up and run the application on your local machine.

### Prerequisites

- Python 3.10 or later

### How to Run

**1. Install dependencies**
```bash
pip install -r requirements.txt
```
**2. Run the app**
```bash
streamlit run app.py
```

### ▶️ Running with `run_app.bat` (Windows Only)

For convenience, this project includes a run_app.bat file. To run it on Windows, you can simply click the `run_app` file. It will automatically check for the required libraries, install any missing ones, and then launch the Streamlit application.

## 📒 Jupyter Notebook

The notebook `diabetes_analysis_and_model.ipynb` file contains:

- Load and Explore the Data
- Exploratory Data Analysis (EDA)
- Data Cleaning and Preprocessing
- Model Training (Logistic Regression) and Evaluation
- Feature Importance Analysis
- Saving the model and scaler

This file documents the full process of building the machine learning model used in the Streamlit app.

### 📊 Dataset Info

The dataset used in this project is the Pima Indians Diabetes Dataset, which is a well-known dataset in the medical machine learning community.
- **Source:** https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database/data

### 🔍 Model Info

- **Model**: Logistic Regression
- **Scaler**: StandardScaler 
- **Input** Features: Pregnancies , Glucose, BloodPressure, BMI, DiabetesPedigreeFunction, Age
- **Output**: % chance of having diabetes



