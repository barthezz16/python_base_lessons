import json
from pprint import pprint

with open('rpg.json', 'r', encoding='utf8') as file_with_data:
    data = json.load(file_with_data)
pprint(data["Location_0_tm0"]
       [1]['Location_1_tm1040']
       [-1]['Location_3_tm33000']
       [-1]['Location_7_tm33300']
       [-1]['Location_10_tm55100']
       [-1]['Location_12_tm0.0987654320'][0])
