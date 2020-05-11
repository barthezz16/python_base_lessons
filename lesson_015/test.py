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

data = data['Location_0_tm0']
mob_list = []
loc_list = []
# Собираем данные из локации
for index, item in enumerate(data):
    if isinstance(item, str):
        mob_list.append(item)
    elif isinstance(item, dict):
        loc_list.append((list(item.keys())[0], index))
# Переход в нужную локацию
for index, name_loc in enumerate(loc_list):
    print(f'{index + 1}.{name_loc[0]}')

input_user = input('Сделайте выбор!')
print(loc_list[int(input_user) - 1])
key, index = loc_list[int(input_user) - 1]
data = data[int(index)][key]
print(data)
