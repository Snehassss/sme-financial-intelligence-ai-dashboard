# sme-financial-intelligence-ai-dashboard

 FinSight AI  
 AI-Powered Financial Intelligence Dashboard for SMEs (UPI + Cash Analytics)

---

 Overview

FinSight AI is an intelligent financial analytics system designed for Small and Medium Enterprises (SMEs).  
It analyzes both **UPI (digital)** and **cash transactions** to provide actionable insights, anomaly detection, and future revenue forecasting.

---

 Problem Statement

Small businesses often struggle to:
- Track income vs expenses
- Detect unusual transactions
- Understand financial trends
- Make data-driven decisions

---

 Solution

We built an **AI-powered dashboard** that:

- Analyzes financial transactions
- Detects anomalies using Machine Learning
- Forecasts future revenue trends
- Generates smart financial insights
- Allows interactive exploration of data

---

 Features

- **KPI Dashboard** (Income, Expense, Transactions)
- **Revenue Trend Analysis**
- **Category-wise Spending Insights**
- **UPI vs Cash Analysis**
- **Anomaly Detection (Isolation Forest)**
- **Forecasting using Regression**
- **AI-Based Financial Insights**
- **Interactive Filters (Date, Category, Payment Mode)**

---

Machine Learning Models Used

- **Isolation Forest** → Detect unusual transactions
- **Linear Regression** → Forecast revenue trends

---

 Dataset

- Retail transaction dataset
- Includes:
  - Date
  - Amount
  - Category
  - Payment Mode (UPI/Cash)
- Enhanced with:
  - Simulated expenses
  - Engineered financial features

---

 Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Streamlit**
- **Matplotlib**

---

project-folder
│
├── app.py # Streamlit dashboard
├── final_data.csv # Processed dataset
├── Cleaned_Retail_Store_Data.csv
├── notebook.ipynb # Data processing + ML
└── README.md

---

How to Run

1. Clone the repository
```bash
git clone https://github.com/your-username/repo-name.git
cd repo-name

2. Install dependencies
pip install -r requirements.txt

3. Run the app
streamlit run app.py
