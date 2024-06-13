import json

with open('ncn_kansai/nodes.json') as file:
    data = json.load(file)

tag_statistics = {}

for element in data:
    for tag, value in element['tags'].items():
        tag_statistics[tag] = tag_statistics.get(tag, {})
        tag_statistics[tag][value] = tag_statistics[tag].get(value, 0) + 1

for tag, values in tag_statistics.items():
    print(f'{tag}:')
    for value, count in values.items():
        print(f'  {value}: {count}')