import pandas as pd

employees = pd.read_csv('level_up_data.csv')

data_types = employees.dtypes

numeric_columns = employees.columns[(data_types == 'float64') | (data_types == 'int64')]

numeric_employees = employees[numeric_columns]

numeric_employees.dtypes 
