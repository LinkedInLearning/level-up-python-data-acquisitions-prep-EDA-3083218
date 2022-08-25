import pandas as pd

dollar_values = {'dollar_values': ['$10.00', '$1,00', '$10', '$10.01', '$1,000.01']} 

dollar_data = pd.DataFrame(dollar_values)

dollar_data['dollar_values'].mean()

dollar_data['dollar_values'] = dollar_data['dollar_values'].str.replace('\\$', '')

dollar_data['dollar_values'] = dollar_data['dollar_values'].str.replace(',(?=[0-9]{2}$)', '')

dollar_data['dollar_values'] = dollar_data['dollar_values'].str.replace(',', '')

dollar_data['dollar_values'] = dollar_data['dollar_values'].astype(float)

dollar_data['dollar_values'].mean()
