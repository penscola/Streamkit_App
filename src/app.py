import streamlit as st

st.title("Sales Register")
st.write("Welcome to the Sales Register!")

sepal_height = st.number_input("Enter sepal heigth")
sepal_width = st.number_input("Enter sepal width")

petal_height = st.number_input("Enter petal height")
petal_width = st.number_input("Enter petal width")

if st.button("Predict"):
    st.text(f"The iris has been classified as: '{''}'")