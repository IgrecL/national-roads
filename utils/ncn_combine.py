import json

json_files = [
    "data/ncn_nodes1.json",
    "data/ncn_nodes2.json",
    "data/ncn_nodes3.json"]

python_objects = []

for json_file in json_files:
    with open(json_file, "r") as f:
        python_objects.extend(json.load(f))

with open("data/ncn_nodes.json", "w") as f:
    json.dump(python_objects, f, indent=4)