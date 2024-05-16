import json

json_files = [
    "data/ncn_ways3.json",
    "data/ncn_ways4.json",
    "data/ncn_ways5.json",
    "data/ncn_ways6.json",
    "data/ncn_ways7.json",
    "data/ncn_ways8.json"]

python_objects = []

for json_file in json_files:
    with open(json_file, "r") as f:
        python_objects.extend(json.load(f))

with open("data/ncn_ways.json", "w") as f:
    json.dump(python_objects, f, indent=4)