import streamlit as st
import pandas as pd

st.title("Sales Register")
st.write("Welcome to the Sales Register!")

sepal_height = st.number_input("Enter sepal heigth")
sepal_width = st.number_input("Enter sepal width")

petal_height = st.number_input("Enter petal height")
petal_width = st.number_input("Enter petal width")

if st.button("Predict"):

    df = pd.DataFrame({
        "sepal_height": [sepal_height], "sepal_width": [sepal_width], "petal_height": [petal_height], "petal_width": [petal_width]
    })

    print(f"[Info] Input data as dataframe: \n{df.to_markdown()}")

    st.text(f"The iris has been classified as: '{''}'")