import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title and layout
st.set_page_config(page_title="Prediction Dashboard", layout="wide")

# Page title
st.title("Prediction Dashboard")

# Sidebar
st.sidebar.title("User Input")

# Sidebar - Age
age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=30, step=1)

# Sidebar - Gender
gender = st.sidebar.selectbox("Gender", ("Male", "Female"))

# Sidebar - Income
income = st.sidebar.number_input("Income", min_value=0, value=50000, step=1000)

# Generate a random prediction based on inputs
prediction = st.sidebar.button("Predict")

# Display prediction
if prediction:
    # Placeholder logic for prediction
    predicted_value = 0.8 * age + 0.2 * income

    # Display prediction result
    st.success(f"The predicted outcome is: {predicted_value:.2f}")

# Data visualization
st.subheader("Data Visualization")

# Create a sample dataframe
data = pd.DataFrame({"Age": [25, 30, 35, 40, 45],
                     "Income": [50000, 60000, 55000, 70000, 80000]})

# Display the dataframe
st.write(data)

# Create a bar chart
plt.bar(data["Age"], data["Income"])
plt.xlabel("Age")
plt.ylabel("Income")
plt.title("Income by Age")
st.pyplot(plt)
