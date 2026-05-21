import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

st.title("Bank Marketing - AutoML Model")

test = pd.read_csv("test.csv")

# Modeli yükle
model = load_model("bank_model")

# Tahmin yap
if st.button("Tahminleri Al"):
    predictions = predict_model(model, data=test)
    submission = pd.DataFrame({
        "Term_Deposit_Prediction": predictions["prediction_label"]
    })
    submission.to_csv("submission.csv", index=False)
    st.success("Tahminler tamamlandı.")
    st.download_button("Tahmin Dosyasını İndir", data=open("submission.csv", "rb"),
                       file_name="submission.csv", mime="text/csv")
