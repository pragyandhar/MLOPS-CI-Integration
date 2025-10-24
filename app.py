# app.py

import streamlit as st

st.title("Simple Streamlit App")

num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

operation = st.selectbox("Choose operation", ["Add", "Subtract"])

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    else:
        result = num1 - num2
    st.success(f"Result: {result}")
