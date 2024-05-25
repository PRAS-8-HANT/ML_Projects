import pandas as pd
import numpy as np
import streamlit as st
import pickle

with open('iris.pkl', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(page_title="Iris Species Predictor",page_icon="🪷",layout="centered")
st.markdown("<div style='background-color:#C40C0C; border-radius:50px; align-items:center; justify-content: center;'><h1 style='text-align:center; color:white;'>✨ Iris Species Predictor ✨ </h1></div>",unsafe_allow_html=True)
#st.markdown("<h4 style='text-align:center; color:black;'>Find the Best Price for Your Laptop</h4>",unsafe_allow_html=True)

sepal_length = st.number_input(label="Enter Sepal Length",placeholder="Enter Sepal Length",value=None,min_value=0.69,max_value=11.1,step=0.1)
sepal_width = st.number_input(label="Enter Sepal Width",placeholder="Enter Sepal Width",value=None,min_value=0.69,max_value=11.1,step=0.1)
petal_length = st.number_input(label="Enter Petal Length",placeholder="Enter Petal Length",value=None,min_value=0.69,max_value=11.1,step=0.1)
petal_width = st.number_input(label="Enter Petal Width",placeholder="Enter Petal Width",value=None,min_value=0.69,max_value=11.1,step=0.1)

pred = st.button("Predict",use_container_width=True)

if pred:
    if any([sepal_length is None, sepal_width is None, petal_length is None, Touchscreen is None,  petal_width  is None]):
        st.error("Please, Select all Inputs before Pressing Predict Button.",icon="📝")
    else:
        prediction = int(model.predict(df))
        if prediction == "":
            st.error("Please select Valid Inputs.", icon="⚠️")
        else:
            st.success(f"The Flower Species is : {prediction}", icon="✅")
