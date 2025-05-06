import streamlit as st
import pandas as pd
import os

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


# st.write('Current working directory:', os.getcwd())
# st.write('Files in directory:', os.listdir())


