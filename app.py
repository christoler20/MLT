# Importing Libraries
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Helper Functions
@st.cache_data
def load_data(url):
    data = pd.read_csv(url)
    return data

@st.cache_data
def preprocess_data(data):
    # Assuming the last column is the target
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    return X, y

# Model Training Function
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return model, accuracy

# Streamlit UI
st.title('Enterprise Streamlit Dashboard')
url = st.text_input('Enter CSV URL')
if url:
    data = load_data(url)
    X, y = preprocess_data(data)
    model, accuracy = train_model(X, y)
    st.write(f'Accuracy: {accuracy:.2f}')
    st.subheader('Model Prediction')
    # Assuming binary classification
    input_data = [st.number_input('Feature 1'), st.number_input('Feature 2')]
    if st.button('Predict'):
        prediction = model.predict([input_data])
        st.write(f'Prediction: {prediction[0]}')
