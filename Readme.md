# 🧮 Customer Lifetime Value Prediction
**Final Internship Project** – Celebal Technologies  
Author: [Sudeshna Pendyala](mailto:sudeshnapendyala11@gmail.com)

---

## 📌 Project Summary

This project predicts the **Customer Lifetime Value (CLV)** of customers based on their **Recency** and **Frequency** using machine learning. It uses a Random Forest model trained on the Online Retail II dataset and is deployed via **Streamlit**. The project also includes beautiful **Tableau dashboards** for interactive business insights.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `celebal final.ipynb` | Jupyter notebook for data cleaning, feature engineering & model training |
| `clv_model.pkl` | Pickled Random Forest model |
| `app.py` | Streamlit web app for CLV prediction |
| `requirements.txt` | All required Python libraries |
| `Final Internship Project Report.pdf` | Final report submitted to Celebal Technologies |
| `CLV Insights Dashboard-Tableau.twbx` | Tableau dashboards for insights |
| `rfm_2009_ready.xlsx` | Cleaned RFM data for Tableau |

---
 Tableau Dashboard:
Explore the interactive dashboard:
🔗 View on Tableau Public

🎯 Model Summary:

Model Used: Random Forest Regressor
Features: Recency, Frequency
Target: Monetary Value (CLV)

Performance:
MSE: ~155,772
R² Score: ~0.576

📚 Dataset:
Source: Kaggle – Online Retail II Dataset
Files used: online_retail_2009.xlsx, online_retail_2010.xlsx
---
## 🚀 Run the App Locally

### 📦 Step 1: Clone the Repo
```bash
git clone https://github.com/sudeshnapendyala09/CLV-Project.git
cd CLV-Project

📦 Step 2: Install Dependencies
bash
pip install -r requirements.txt

🚀 Step 3: Run Streamlit App
bash
streamlit run app.py
