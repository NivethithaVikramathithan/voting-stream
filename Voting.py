import streamlit as st



name=st.text_input("Enter your name")
if name:
    st.write(f"Hello,{name}!Great to have you here!!")

age=st.number_input("Enter your age:",min_value=0,max_value=100)
if age >= 18:
    st.success("You can vote 🗳️")
elif age > 0 and age < 18:
    st.error("You are not eligible to vote ❌")