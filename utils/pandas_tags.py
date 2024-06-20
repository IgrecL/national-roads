import pandas as pd
import json
import matplotlib.pyplot as plt

# Load JSON data into a DataFrame
df = pd.read_json('data/ncn_japan/ways.json')

# Load JSON data into a list
with open('data/ncn_japan/ways.json') as file:
    data = json.load(file)

# Adjust 'tags' field to be a list of lists
for element in data:
    element['tags'] = [element['tags']]

# Normalize JSON data into a DataFrame
tags_df = pd.json_normalize(data, record_path=['tags'], meta=['id'])

# Get list of categories from DataFrame columns
categories = tags_df.columns

# Iterate over each category
for category in categories:
    if category == 'id':
        continue  # Skip 'id' column
    
    # Calculate tag counts and select top 10
    tag_counts = tags_df[category].value_counts().head(10)
    
    # Check if the highest frequency is over 1000
    if tag_counts.max() > 500:
        plt.figure(figsize=(10, 6))
        tag_counts.plot(kind='bar')
        plt.title(f'Top 10 Most Common Tags - {category}')
        plt.xlabel('Tag')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
