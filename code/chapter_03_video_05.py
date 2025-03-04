import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

# First, we'll load our level up data.
employees = pd.read_csv('../data/level_up_data.csv')

employee_numeric = employees.select_dtypes(include = np.number)

st.title('Visualizing Employee Data')

st.sidebar.title('Select your visualization variables')

# We will let users select 2 variables to visualize.
viz_variables = st.sidebar.multiselect(
  'Select variables to visualize',
  employee_numeric.columns,
  max_selections = 2
)

color_variables = st.sidebar.selectbox(
  'Select variable for color',
  employee_numeric.columns
)

st.scatter_chart(employee_numeric, x = viz_variables[0], y = viz_variables[1], color=color_variables)