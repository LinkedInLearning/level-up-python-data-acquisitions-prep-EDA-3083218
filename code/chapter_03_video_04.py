import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

employees = pd.read_csv('level_up_data.csv')

def z_score_maker(variable):
  variable_mean = variable.mean()
  variable_sd = variable.std()
  z_score = (variable - variable_mean) / variable_sd 
  return z_score

viz_variables = ['prior_job_count', 'days_to_separate', 
  'proportion_401K', 'starting_salary']

for i in viz_variables:  
  employees[i] = z_score_maker(employees[i])

employees_melted = employees.melt(id_vars = 'department', 
  value_vars = viz_variables)
  
g = sns.catplot(x="value", y="variable",
                hue="department", 
                data=employees_melted,
                orient="h", height=2, aspect=3, palette="Set3",
                kind="violin", dodge=True, cut=0, bw=.2, sharex=False)

plt.show()

plt.savefig('chapter_03_video_04_end_viz.svg', 
           transparent=True)
