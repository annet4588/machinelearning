import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This is a machine learning app')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://github.com/dataprofessor/data/blob/master/penguins_cleaned.csv')
