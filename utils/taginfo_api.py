import requests
import json

# Example list of keys and possible values
keys_and_values = {
    'surface': ['asphalt', 'concrete', 'paved', 'unpaved', 'grass', 'gravel']
}

# Taginfo API endpoint
base_url = 'https://taginfo.openstreetmap.org/api/4/tag/stats'

# Function to fetch statistics for a key-value pair
def fetch_taginfo_stats(key, value):
    url = f"{base_url}?key={key}&value={value}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for key={key}, value={value}. Status code: {response.status_code}")
        return None

# Iterate over keys and their values
for key, values in keys_and_values.items():
    if len(values) < 10:
        print(f"Statistics for tag: {key}")
        for value in values:
            stats = fetch_taginfo_stats(key, value)
            if stats:
                print("\n" + value)
                print(f" - Fraction in nodes: {stats['data'][1]['count_fraction']}")
                print(f" - Fraction in ways: {stats['data'][2]['count_fraction']}")
                print(f" - Fraction in relations: {stats['data'][3]['count_fraction']}")