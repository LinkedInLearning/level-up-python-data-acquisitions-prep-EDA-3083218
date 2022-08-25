import pandas as pd

employees = pd.read_csv('level_up_data.csv')

def z_score_maker(variable):
  variable_mean = variable.mean()
  variable_sd = variable.std()
  z_score = (variable - variable_mean) / variable_sd 
  return z_score
  
z_score_maker(employees['age'])
