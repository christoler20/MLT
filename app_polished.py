import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the Dashboard
st.title("Enterprise Analytics Dashboard")

# Subheader
st.subheader("Key Insights for Senior Leadership")

# Data Loading
@st.cache
def load_data():
    # Simulating data loading
    data = pd.DataFrame({
        'Metric': ['Revenue', 'Cost', 'Profit'],
        'Value': [100000, 80000, 20000]
    })
    return data

df = load_data()

# Display the data in a table
st.write("### Financial Overview")
st.write(df)

# Visualization
fig, ax = plt.subplots()
ax.bar(df['Metric'], df['Value'], color=['green', 'red', 'blue'])
st.write("### Revenue Breakdown")
st.pyplot(fig)

# Insights for Senior Leaders
st.write("#### Insights:")
st.write("- Revenue has increased by 25% from the last quarter.")
st.write("- Cost optimization strategies are yielding positive results.")
st.write("- Ensure to focus on profit margin growth.")