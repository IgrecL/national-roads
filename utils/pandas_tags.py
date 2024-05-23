import pandas as pd
import json
import matplotlib.pyplot as plt

df = pd.read_json('data/ncn_ways.json')

with open('data/ncn_ways.json') as file:
    data = json.load(file)
for element in data:
    element['tags'] = [element['tags']]
tags_df = pd.json_normalize(data, record_path=['tags'], meta=['id'])

categories = tags_df.columns

for category in categories:
    if category == 'id':
        continue  # Skip 'id' column
    tag_counts = tags_df[category].value_counts().head(10)
    
    plt.figure(figsize=(10, 6))
    tag_counts.plot(kind='bar')
    plt.title(f'Top 10 Most Common Tags - {category}')
    plt.xlabel('Tag')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()