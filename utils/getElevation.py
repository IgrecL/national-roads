import xml.etree.ElementTree as ET
import os
import json

# ベースパスとファイル名の共通部分
base_path = 'PackDLMap/FG-GML-5235-12-DEM5A/'
base_filename = 'FG-GML-5235-12-{index:02d}-DEM5A-20200117.xml'
# base_filename = 'FG-GML-5235-12-{index:02d}-DEM5A-20190130.xml'
# base_filename = 'FG-GML-5235-12-{index:02d}-DEM5A-20161001.xml'
# base_filename = 'FG-GML-5235-12-{index:02d}-DEM5A-20231113.xml'


# 名前空間の定義
ns = {'gml': 'http://www.opengis.net/gml/3.2'}

# ファイルを処理する関数
def process_file(file_path, output_path):
    # XMLファイルをパース
    tree = ET.parse(file_path)
    root = tree.getroot()

    # 地理的範囲の取得
    envelope = root.find('.//gml:Envelope', ns)
    lower_corner = envelope.find('gml:lowerCorner', ns).text.split()
    upper_corner = envelope.find('gml:upperCorner', ns).text.split()

    lower_lat, lower_lon = float(lower_corner[0]), float(lower_corner[1])
    upper_lat, upper_lon = float(upper_corner[0]), float(upper_corner[1])

    # グリッドサイズの取得
    grid_limits = root.find('.//gml:Grid/gml:limits/gml:GridEnvelope', ns)
    low = list(map(int, grid_limits.find('gml:low', ns).text.split()))
    high = list(map(int, grid_limits.find('gml:high', ns).text.split()))
    rows, cols = high[0] - low[0] + 1, high[1] - low[1] + 1

    # セルサイズの計算
    lat_step = (upper_lat - lower_lat) / rows
    lon_step = (upper_lon - lower_lon) / cols

    # データポイントの取得
    tuple_list = root.find('.//gml:tupleList', ns).text.strip().split('\n')

    # データポイントの地理的な位置の計算と保存
    data_list = []

    for i, data in enumerate(tuple_list):
        # カンマで分割し、2番目の要素（数値）を抽出
        elevation = data.split(",")[1]
        # 数値部分を浮動小数点数に変換して追加
        try:
            elevation = float(elevation)
            row = i // cols
            col = i % cols
            lat = lower_lat + row * lat_step
            lon = lower_lon + col * lon_step
            data_list.append({
                "elevation": elevation,
                "latitude": lat,
                "longitude": lon
            })
        except ValueError:
            # 数値に変換できない場合はスキップ
            continue

    # JSONファイルに書き込む
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)

    print(f"Data written to {output_path}")

# 00から99までのファイルを処理
for index in range(100):
    file_name = base_filename.format(index=index)
    file_path = os.path.join(base_path, file_name)
    
    if os.path.exists(file_path):
        output_file = os.path.join('dataInJason/FG-GML-5235-12-DEM5A', f'{file_name.replace("20200117.xml", "20200117_output.json")}')
        # output_file = os.path.join('dataInJason/FG-GML-5235-12-DEM5A', f'{file_name.replace("20190130.xml", "20200117_output.json")}')
        # output_file = os.path.join('dataInJason/FG-GML-5235-12-DEM5A', f'{file_name.replace("20161001.xml", "20200117_output.json")}')
        # output_file = os.path.join('dataInJason/FG-GML-5235-12-DEM5A', f'{file_name.replace("20231113.xml", "20200117_output.json")}')

        process_file(file_path, output_file)
    else:
        print(f"File {file_path} does not exist.")
