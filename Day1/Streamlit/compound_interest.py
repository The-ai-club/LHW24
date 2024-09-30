import streamlit as st
import pandas as pd

def compound_interest(principal, rate, time, n):
    amount = principal * (1 + (rate / (n * 100))) ** (n * time)
    ci = amount - principal
    return ci, amount

def payment_schedule(principal, rate, time, n):
    schedule = []
    for year in range(1, time + 1):
        amount = principal * (1 + (rate / (n * 100))) ** (n * year)
        ci = amount - principal
        schedule.append({"Year": year, "Amount": amount, "Interest": ci})
    return pd.DataFrame(schedule)

st.title("Compound Interest Calculator")

principal = st.number_input("Principal Amount", min_value=0.0, value=1000.0, step=100.0)
rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=5.0, step=0.1)
time = st.number_input("Time (Years)", min_value=1, value=5, step=1)
n = st.number_input("Number of times interest applied per time period", min_value=1, value=4, step=1)

if st.button("Calculate"):
    ci, total_amount = compound_interest(principal, rate, time, n)
    st.metric(f"Compound Interest", value=f"${ci:.2f}")
    st.metric(f"Total Amount", value = f"${total_amount:.2f}")
 
    st.subheader("Payment Schedule")
    schedule_df = payment_schedule(principal, rate, time, n)
    st.write(schedule_df)
 
    st.subheader("Payment Schedule Graph")
    st.line_chart(schedule_df)
