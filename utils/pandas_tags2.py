import pandas as pd
import json
import matplotlib.pyplot as plt

df = pd.read_json('data/ncn_japan/nodes.json')

with open('data/ncn_japan/nodes.json') as file:
    data = json.load(file)
    
tags_df = pd.json_normalize(data)
nan_count = tags_df.isna().sum().sort_values()

plt.figure(figsize=(10, 6))
nan_count[0:50].plot(kind='bar')
plt.xlabel('Columns')
plt.ylabel('Number of NaN values')
plt.title('Number of NaN Values in Each Column')
plt.tight_layout()
plt.show()
