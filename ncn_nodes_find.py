import json

with open('data/ncn_ways.json') as file:
    ncn_ways = json.load(file)

ncn_nodes = []

for w in ncn_ways:
    nodes = w.get('nodes', [])
    
    for node in nodes:
        if node not in ncn_nodes:
            ncn_nodes.append(node)

ncn_nodes.sort()

with open('data/ncn_nodes_indices.json', 'w') as file:
    json.dump(ncn_nodes, file)