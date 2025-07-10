import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Page config
st.set_page_config(page_title="CLV Predictor", layout="centered")

# -------------------------------
# Load model
try:
    with open("clv_model.pkl", "rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.stop()

# -------------------------------
# Title & Description
st.title("🧮 Customer Lifetime Value Prediction")

st.markdown("""
This app predicts **Customer Lifetime Value (CLV)** using:
- 📆 **Recency**: How recently the customer purchased
- 🔁 **Frequency**: How often they purchase

> Fill in the form below to get a CLV prediction.
""")

# -------------------------------
# Input form
with st.form("clv_form"):
    recency = st.number_input("📆 Recency (days since last purchase)", min_value=0)
    frequency = st.number_input("🔁 Frequency (number of purchases)", min_value=0)
    submitted = st.form_submit_button("🚀 Predict CLV")

if submitted:
    try:
        prediction = model.predict([[recency, frequency]])
        st.success(f"💰 Predicted CLV: ₹{prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

# -------------------------------
# Load dataset for visualizations
@st.cache_data
def load_data():
    df = pd.read_excel("online_retail_2009.xlsx")
    df = df[df['Customer ID'].notnull()]
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    snapshot_date = pd.to_datetime("2010-01-01")
    rfm = df.groupby("Customer ID").agg({
        "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
        "Invoice": "nunique"
    }).reset_index()
    rfm.columns = ['Customer ID', 'Recency', 'Frequency']
    return rfm

# -------------------------------
# Visualizations
st.markdown("---")
st.subheader("📊 CLV Visual Insights")

try:
    customer_df = load_data()
    customer_df['Estimated CLV'] = customer_df.apply(
        lambda row: model.predict([[row['Recency'], row['Frequency']]])[0], axis=1
    )

    sns.set_theme(style="whitegrid")

    # --- Top Customers ---
    st.markdown("#### 🔝 Top 10 Customers by Estimated CLV")
    top_customers = customer_df.sort_values(by="Estimated CLV", ascending=False).head(10)
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    sns.barplot(data=top_customers, x="Customer ID", y="Estimated CLV", ax=ax1, palette="viridis")
    ax1.set_ylabel("Estimated CLV (₹)")
    ax1.set_xlabel("Customer ID")
    fig1.tight_layout()
    st.pyplot(fig1)

    # --- Frequency vs CLV ---
    st.markdown("#### 📈 Frequency vs Estimated CLV")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=customer_df, x="Frequency", y="Estimated CLV", hue="Recency", palette="coolwarm", ax=ax2)
    ax2.set_title("Customer Frequency vs Estimated CLV")
    fig2.tight_layout()
    st.pyplot(fig2)

    # --- Recency vs CLV ---
    st.markdown("#### 📉 Recency vs Estimated CLV")
    fig3, ax3 = plt.subplots()
    sns.regplot(data=customer_df, x="Recency", y="Estimated CLV", scatter_kws={'alpha': 0.5}, color="coral", ax=ax3)
    ax3.set_title("Recency Impact on Estimated CLV")
    fig3.tight_layout()
    st.pyplot(fig3)

except Exception as e:
    st.error(f"❌ Visualization Error: {e}")
