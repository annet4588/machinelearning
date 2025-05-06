import streamlit as st
import pandas as pd
import os

# st.write('Current working directory:', os.getcwd())
# st.write('Files in directory:', os.listdir())

st.title('🤖 Machine Learning App')

st.info('This is a machine learning app')

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
