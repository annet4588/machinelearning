import streamlit as st
import pandas as pd
import os

# st.write('Current working directory:', os.getcwd())
# st.write('Files in directory:', os.listdir())

st.title('🤖 Machine Learning App')

st.info('This is a machine learning app')

# Expander 1
with st.expander('Data'):
  st.write('**Raw Data**')
  
  try:
    df = pd.read_csv('penguins.csv')
    st.write("Data loaded successfully")
    st.dataframe(df)
  except Exception as e:
    st.error(f"Failed to load the file: {e}")


  st.write('**X**')
  X = df.drop('species', axis=1)
  X
  
  st.write('**y**')
  y = df.species
  y

# Expander 2
with st.expander('Data visualisation'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')


# Data Preparation
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  gender = st.selectbox('Gender', ('male', 'female'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
