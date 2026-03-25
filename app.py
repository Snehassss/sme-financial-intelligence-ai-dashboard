
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
st.title("AI-Powered SME Financial Dashboard")

# ---------------- KPIs ----------------
st.subheader("📌 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

total_income = df_filtered[df_filtered['type'] == 'sale']['amount'].sum()
total_expense = df_filtered[df_filtered['type'] == 'expense']['amount'].sum()
transactions = len(df_filtered)

profit = total_income - total_expense

if total_expense != 0:
    profit_percent = (profit / total_expense) * 100
else:
    profit_percent = 0

col1.metric("💰 Income", f"₹{total_income:,.0f}")
col2.metric("💸 Expense", f"₹{total_expense:,.0f}")
col3.metric("🧾 Transactions", transactions)

if profit > 0:
    col4.metric(
        "📈 Profit %",
        f"{profit_percent:.2f}%",
        delta="Profit"
    )
else:
    col4.metric(
        "📉 Loss %",
        f"{abs(profit_percent):.2f}%",
        delta="Loss"
    )

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
st.subheader("AI Interpretation")

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
