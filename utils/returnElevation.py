import json
import time

def return_elevation(given_datas, input_data):
    entries = []

    for input in input_data:
        for given in given_datas:
            if given[0]['latitude'] <= input['latitude'] and input['latitude'] <= given[-1]['latitude'] and given[0]['longitude'] <= input['longitude'] and input['longitude'] <= given[-1]['longitude']:
                given_data = given
                break

        default = input['latitude'] - given_data[0]['latitude']
        if(default >= 0):
            preliminary = 0
            min = default
            for index in range(150, len(given_data), 150):
                if(min > abs(input['latitude'] - given_data[index]['latitude'])):
                    min =  abs(input['latitude'] - given_data[index]['latitude'])
                    preliminary = index
                else:
                    break
        else:
            preliminary = 0

        default = input['longitude'] - given_data[preliminary]['longitude']
        if(default >= 0):
            min = default
            preliminary_lat = preliminary
            for index in range(preliminary_lat + 1, preliminary_lat + 150):
                if(min > abs(input['longitude'] - given_data[index]['longitude'])):
                    min =  abs(input['longitude'] - given_data[index]['longitude'])
                    preliminary = index
                else:
                    break
        else:
            preliminary = 0
        
        entries.append(
            {
                'elevation':given_data[preliminary]['elevation']
            }
        )
    return entries

        


        


# ↓↓↓↓↓↓ Please change the file name ↓↓↓↓↓↓
given_data_file_path = 'Data/FG-GML-5235-01-00-DEM5A-20200117_output.json'
given_datas = []
# input_data_file_path = 'Data/input_test.json'
input_data_file_path = 'Data/input_test.json'
output_file_path = 'Data/output_elevation.json'

for i in range(3):
    given_data_file_path = 'Data/FG-GML-5235-01-0'+ str(i) + '-DEM5A-20200117_output.json'
    with open(given_data_file_path, 'r', encoding='utf-8') as f:
        given_data = json.load(f)
        given_datas.append(given_data)

with open(input_data_file_path, 'r', encoding='utf-8') as f:
    input_data = json.load(f)


# Write results
with open(output_file_path, 'w', encoding='utf-8') as f:
    start = time.time()
    json.dump(return_elevation(given_datas, input_data), f, ensure_ascii=False, indent=4)
    end = time.time()
    print(end - start)