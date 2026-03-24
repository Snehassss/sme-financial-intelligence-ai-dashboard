# import streamlit as st
# import pandas as pd

# st.set_page_config(page_title="SME AI Dashboard", layout="wide")

# # ---- TITLE ----
# st.title("📊 AI-Powered SME Financial Dashboard")

# # ---- LOAD DATA ----
# df = pd.read_csv("Cleaned_Retail_Store_Data.csv")

# df['date'] = pd.to_datetime(df['Transaction Date'])
# df['amount'] = df['Total Spent']
# df['type'] = 'income'
# df['category'] = df['Category']
# df['payment_mode'] = df['Payment Method']

# st.sidebar.header("🔍 Filters")

# start_date = st.sidebar.date_input("Start Date", df['date'].min())
# end_date = st.sidebar.date_input("End Date", df['date'].max())

# category = st.sidebar.multiselect(
#     "Category",
#     df['category'].unique(),
#     default=df['category'].unique()
# )

# payment = st.sidebar.multiselect(
#     "Payment Mode",
#     df['payment_mode'].unique(),
#     default=df['payment_mode'].unique()
# )

# df_filtered = df[
#     (df['date'] >= pd.to_datetime(start_date)) &
#     (df['date'] <= pd.to_datetime(end_date)) &
#     (df['category'].isin(category)) &
#     (df['payment_mode'].isin(payment))
# ]

# # ---- KPI SECTION ----
# st.subheader("📌 Key Metrics")

# col1, col2, col3 = st.columns(3)

# total_income = df_filtered['amount'].sum()
# total_expense = df_filtered[df_filtered['type'] == 'expense']['amount'].sum()
# avg_income = df_filtered['amount'].mean()
# transactions = len(df_filtered)
# num_anomalies = df_combined[df_combined['anomaly'] == -1].shape[0]

# col1.metric("💰 Total Revenue", f"₹{total_income:,.0f}")
# col2.metric("📊 Avg Transaction", f"₹{avg_income:,.0f}")
# col3.metric("🧾 Transactions", transactions)

# # ---- TREND ----
# st.subheader("📈 Revenue Trend")

# df_daily = df_filtered.groupby('date')['amount'].sum().reset_index()
# st.line_chart(df_daily.set_index('date'))

# # ---- CATEGORY ----
# col1, col2 = st.columns(2)

# with col1:
#     st.subheader("📊 Category Analysis")
#     st.bar_chart(df_filtered.groupby('category')['amount'].sum())

# with col2:
#     st.subheader("💳 Payment Mode")
#     st.bar_chart(df_filtered['payment_mode'].value_counts())
    
# # ---- AI INSIGHTS ----
# st.subheader("🤖 AI Insights")

# if st.button("🔍 Show Detailed Analysis"):

#     st.markdown("## 📊 Detailed Financial Analysis")

#     st.write(f"""
#     💰 Total Income: ₹{total_income:,.0f}  
#     💸 Total Expense: ₹{total_expense:,.0f}  

#     Your business is profitable and stable.

#     🚨 {num_anomalies} unusual transactions detected.
#     """)

#     # Revenue Trend
#     st.subheader("📈 Revenue Trend")
#     df_daily = df_filtered.groupby('date')['amount'].sum().reset_index()
#     st.line_chart(df_daily.set_index('date'))

#     # Category
#     st.subheader("📊 Category Breakdown")
#     st.bar_chart(df_filtered.groupby('category')['amount'].sum())

#     # Payment Mode
#     st.subheader("💳 Payment Mode")
#     st.bar_chart(df_filtered['payment_mode'].value_counts())

#     # Anomalies
#     st.subheader("🚨 Anomalies")
#     st.dataframe(df_combined[df_combined['anomaly'] == -1].head(10))

#     # Interpretation
#     st.subheader("🧠 AI Interpretation")

#     if total_income > total_expense:
#         st.success("✅ Business is healthy and profitable")

#     if num_anomalies > 0:
#         st.warning("⚠️ Monitor unusual transactions")

#     st.info("📊 Revenue trend is stable — good for growth planning")

# # ---- DATA VIEW ----
# st.subheader("📂 Data Preview")
# st.dataframe(df.head(50))

# import streamlit as st
# import pandas as pd
# import numpy as np
# from sklearn.ensemble import IsolationForest

# st.set_page_config(page_title="SME AI Dashboard", layout="wide")

# # ---------------- LOAD DATA ----------------
# df = pd.read_csv("Cleaned_Retail_Store_Data.csv")

# # ---------------- CREATE df_combined ----------------
# df_new = pd.DataFrame()

# df_new['date'] = pd.to_datetime(df['Transaction Date'])
# df_new['amount'] = df['Total Spent']
# df_new['type'] = 'expense'
# df_new['category'] = df['Category']
# df_new['payment_mode'] = df['Payment Method']
# df_new['payment_mode'] = df_new['payment_mode'].replace({
#     'Digital Wallet': 'UPI'
# })

# # ---- Add expense ----
# expense_rows = int(len(df_new) * 0.3)

# expense_data = pd.DataFrame({
#     'date': np.random.choice(df_new['date'], size=expense_rows),
#     'amount': np.random.randint(200, 2000, size=expense_rows),
#     'type': ['income'] * expense_rows,
#     'category': np.random.choice(['rent','salary','utilities'], size=expense_rows),
#     'payment_mode': np.random.choice(['UPI','Cash'], size=expense_rows)
# })

# # Combine
# df_combined = pd.concat([df_new, expense_data]).sort_values('date').reset_index(drop=True)

# # ---- Anomaly Detection ----
# model = IsolationForest(contamination=0.01, random_state=42)
# df_combined['anomaly'] = model.fit_predict(df_combined[['amount']])

# # ---------------- SIDEBAR FILTERS ----------------
# st.sidebar.header("🔍 Filters")

# start_date = st.sidebar.date_input("Start Date", df_combined['date'].min())
# end_date = st.sidebar.date_input("End Date", df_combined['date'].max())

# category = st.sidebar.multiselect(
#     "Category",
#     df_combined['category'].unique(),
#     default=df_combined['category'].unique()
# )

# payment = st.sidebar.multiselect(
#     "Payment Mode",
#     df_combined['payment_mode'].unique(),
#     default=df_combined['payment_mode'].unique()
# )

# # ---------------- APPLY FILTER ----------------
# df_filtered = df_combined[
#     (df_combined['date'] >= pd.to_datetime(start_date)) &
#     (df_combined['date'] <= pd.to_datetime(end_date)) &
#     (df_combined['category'].isin(category)) &
#     (df_combined['payment_mode'].isin(payment))
# ]

# # ---------------- TITLE ----------------
# st.title("📊 AI-Powered SME Financial Dashboard")

# # ---------------- KPIs ----------------
# st.subheader("📌 Key Metrics")

# col1, col2, col3 = st.columns(3)

# total_income = df_filtered[df_filtered['type'] == 'income']['amount'].sum()
# total_expense = df_filtered[df_filtered['type'] == 'expense']['amount'].sum()
# transactions = len(df_filtered)

# col1.metric("💰 Income", f"₹{total_income:,.0f}")
# col2.metric("💸 Expense", f"₹{total_expense:,.0f}")
# col3.metric("🧾 Transactions", transactions)

# # ---------------- CHARTS ----------------
# st.subheader("📈 Revenue Trend")

# df_daily = df_filtered.groupby('date')['amount'].sum().reset_index()
# st.line_chart(df_daily.set_index('date'))

# col1, col2 = st.columns(2)

# with col1:
#     st.subheader("📊 Category Analysis")
#     st.bar_chart(df_filtered.groupby('category')['amount'].sum())

# with col2:
#     st.subheader("💳 Payment Mode")
#     st.bar_chart(df_filtered['payment_mode'].value_counts())

# # ---------------- ANOMALY COUNT ----------------
# num_anomalies = df_filtered[df_filtered['anomaly'] == -1].shape[0]

# # ---------------- AI INSIGHTS ----------------
# st.subheader("🤖 AI Insights")

# # Interpretation
# st.subheader("🧠 AI Interpretation")

# if total_income > total_expense:
#     st.success("✅ Business is healthy and profitable")

# if num_anomalies > 0:
#     st.warning("⚠️ Monitor unusual transactions")

# st.info("📊 Revenue trend is stable — good for growth planning")


# with st.expander("🔍 Show Detailed Analysis"):

#     st.markdown("## 📊 Detailed Financial Analysis")

#     st.write(f"""
#     💰 Total Income: ₹{total_income:,.0f}  
#     💸 Total Expense: ₹{total_expense:,.0f}  

#     Your business is profitable and stable.

#     🚨 {num_anomalies} unusual transactions detected.
#     """)

#     # Trend
#     st.subheader("📈 Revenue Trend")
#     st.line_chart(df_daily.set_index('date'))

#     # Category
#     st.subheader("📊 Category Breakdown")
#     st.bar_chart(df_filtered.groupby('category')['amount'].sum())

#     # Payment
#     st.subheader("💳 Payment Mode")
#     st.bar_chart(df_filtered['payment_mode'].value_counts())

#     # Anomalies
#     st.subheader("🚨 Anomalies")
#     st.dataframe(df_filtered[df_filtered['anomaly'] == -1].head(10))


# # ---- DATA VIEW ----
# st.subheader("📂 Data Preview")
# st.dataframe(df.head(50))

import streamlit as st
import pandas as pd

st.set_page_config(page_title="SME AI Dashboard", layout="wide")

# ---------------- LOAD FINAL DATA ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("final_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

df_combined = load_data()

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🔍 Filters")

start_date = st.sidebar.date_input("Start Date", df_combined['date'].min())
end_date = st.sidebar.date_input("End Date", df_combined['date'].max())

category = st.sidebar.multiselect(
    "Category",
    df_combined['category'].unique(),
    default=df_combined['category'].unique()
)

payment = st.sidebar.multiselect(
    "Payment Mode",
    df_combined['payment_mode'].unique(),
    default=df_combined['payment_mode'].unique()
)

# ---------------- APPLY FILTER ----------------
df_filtered = df_combined[
    (df_combined['date'] >= pd.to_datetime(start_date)) &
    (df_combined['date'] <= pd.to_datetime(end_date)) &
    (df_combined['category'].isin(category)) &
    (df_combined['payment_mode'].isin(payment))
]

# ---------------- TITLE ----------------
st.title("📊 AI-Powered SME Financial Dashboard")

# ---------------- KPIs ----------------
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

total_income = df_filtered[df_filtered['type'] == 'income']['amount'].sum()
total_expense = df_filtered[df_filtered['type'] == 'expense']['amount'].sum()
transactions = len(df_filtered)

col1.metric("💰 Income", f"₹{total_income:,.0f}")
col2.metric("💸 Expense", f"₹{total_expense:,.0f}")
col3.metric("🧾 Transactions", transactions)

# ---------------- CHARTS ----------------
st.subheader("📈 Revenue Trend")

df_daily = df_filtered.groupby('date')['amount'].sum().reset_index()
st.line_chart(df_daily.set_index('date'))

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Category Analysis")
    st.bar_chart(df_filtered.groupby('category')['amount'].sum())

with col2:
    st.subheader("💳 Payment Mode")
    st.bar_chart(df_filtered['payment_mode'].value_counts())

# ---------------- ANOMALY COUNT ----------------
num_anomalies = df_filtered[df_filtered['anomaly'] == -1].shape[0]

# ---------------- AI INSIGHTS ----------------
st.subheader("🤖 AI Insights")

# ---- Interpretation ----
st.subheader("🧠 AI Interpretation")

if total_income > total_expense:
    st.success("✅ Business is healthy and profitable")
else:
    st.error("⚠️ Business is running at a loss")

if num_anomalies > 0:
    st.warning("⚠️ Monitor unusual transactions")

st.info("📊 Revenue trend is stable — good for growth planning")

# ---------------- EXPANDER ----------------
with st.expander("🔍 Show Detailed Analysis"):

    st.markdown("## 📊 Detailed Financial Analysis")

    st.write(f"""
    💰 Total Income: ₹{total_income:,.0f}  
    💸 Total Expense: ₹{total_expense:,.0f}  
    🚨 {num_anomalies} unusual transactions detected.
    """)

    # Trend
    st.subheader("📈 Revenue Trend")
    st.line_chart(df_daily.set_index('date'))

    # Category
    st.subheader("📊 Category Breakdown")
    st.bar_chart(df_filtered.groupby('category')['amount'].sum())

    # Payment
    st.subheader("💳 Payment Mode")
    st.bar_chart(df_filtered['payment_mode'].value_counts())

    # Anomalies
    st.subheader("🚨 Anomalies")
    st.dataframe(df_filtered[df_filtered['anomaly'] == -1].head(10))

# ---------------- DATA VIEW ----------------
st.subheader("📂 Data Preview")
st.dataframe(df_combined.head(50))
