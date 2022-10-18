import requests
import json

wine_category = ['reds', 'whites', 'sparkling']

url = 'https://api.sampleapis.com/wines/'
selected_category = 'reds'
response = requests.get(url + selected_category)
response_json = json.loads(response.text)

print(response_json[0])

selection = {}

selection['winery'] = 'Maselva'
selection['wine'] = 'Emporda 2012'
selection['rating'] = '4.9'
selection['location'] = 'Spain'
selection['image'] = 'fkjervj'
selection['degree'] = '13%'
selection['vintage'] = '2019'

keys = list(selection.keys())
values = list(selection.values())

for i in range(len(selection)):
    print(keys[i], ': ', values[i])