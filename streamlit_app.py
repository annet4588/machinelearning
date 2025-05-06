import streamlit as st
import pandas as pd
import os

st.title('🤖 Machine Learning App')

st.info('This is a machine learning app')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('penguins.csv')


st.write('Current working directory:', os.getcwd())
st.write('Files in directory:', os.listdir())
