import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

employees = pd.read_csv('level_up_data.csv')

data_types = employees.dtypes

numeric_columns = employees.columns[(data_types == 'float64') | (data_types == 'int64')]

numeric_employees = employees[numeric_columns]

numeric_employees = numeric_employees.drop('separated_ny', axis = 1)

employee_correlations = numeric_employees.corr()

print(employee_correlations)
