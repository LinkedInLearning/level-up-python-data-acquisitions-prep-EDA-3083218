import pandas as pd
import requests

link = "https://3083218.youcanlearnit.net/dataTable.html"

response = requests.get("https://3083218.youcanlearnit.net/rank.json?_=1662342121475")

state_data = pd.read_json(response.content)

state_data = pd.DataFrame(state_data['data'].to_list(), columns = ['rank', 'state', 'rainfall'])
