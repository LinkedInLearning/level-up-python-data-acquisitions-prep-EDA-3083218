from bs4 import BeautifulSoup
import pandas as pd
import requests

base_link = 'https://hplussport.net/#people'

page_read = requests.get(base_link)

soup = BeautifulSoup(page_read.content)

board_names = soup.select(".card-name")
len(board_names)
board_roles = soup.select(".card-title")
len(board_roles)

results = []

for i in range(len(board_roles)):
  person_name = board_names[i].text
  person_role = board_roles[i].text
  result_df = pd.DataFrame(
    data = [[person_name, person_role]], 
    columns = ['Name', 'Role'])
  results.append(result_df)
  
results = pd.concat(results)
