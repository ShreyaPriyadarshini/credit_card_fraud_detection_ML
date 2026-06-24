import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_model.pkl")

st.title("💳 Credit Card Fraud Detection")

uploaded_file = st.file_uploader(
    "Upload transaction CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    predictions = model.predict(df)

    df["Prediction"] = predictions

    st.write(df.head())

    fraud_count = sum(predictions)

    st.write(f"Fraud Transactions: {fraud_count}")
    st.write(f"Genuine Transactions: {len(df)-fraud_count}")