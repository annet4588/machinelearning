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
  X_raw = df.drop('species', axis=1)
  X_raw
  
  st.write('**y**')
  y_raw = df.species
  y_raw

# Expander 2
with st.expander('Data Visualisation'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')


# Input Features
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
  gender = st.selectbox('Gender', ('male', 'female'))

# Create a Data Frame for the input featues
data = {'island': island,
        'bill_length_mm': bill_length_mm,
        'bill_depth_mm': bill_depth_mm,
        'flipper_length_mm': flipper_length_mm,
        'body_mass_g': body_mass_g,
        'sex': gender}

input_df = pd.DataFrame(data, index=[0])
input_penguins = pd.concat([input_df, X_raw], axis=0)

# Expander 3 - Input features
with st.expander('Input Features'):
  st.write('**Input Penguin**')
  input_df
  st.write('**Combine Penguins Data**')
  input_penguins

# Data Preparation
# Encode X
encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)
input_row = df_penguins[:1]

# Encode y
target_mapper = {'Adelie': 0,
                 'Chinstrap': 1,
                 'Gentoo': 2}

def target_encode(val):
  return target_mapper[val]

y = y_raw.apply(target_encode)

#Expander
with st.expander('Data preparation'):
  st.write('**Encoded X (Input Penguin)**')
  input_row
  st.write('**Encoded y**')
  y


