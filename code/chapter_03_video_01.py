import pandas as pd

pd.set_option('display.max_columns', None)

employees = pd.read_csv('data/level_up_data.csv')

employees.describe(include='all')
