import pandas as pd
import requests

base_link = 'https://pixelford.com/api/image/id/'

pixelford_list = []

for i in range(20):
    individual_link = base_link + str(i)
    initial_request = requests.get(individual_link)
    json_results = initial_request.content
    pixelford_list.append(pd.read_json(json_results))

pixelford_list = pd.concat(pixelford_list)
