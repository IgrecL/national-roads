start_line = [0, 14000000, 28000001, 42000009, 55999999, 69999999, 83999999, 97999992]
end_line = [14000000, 28000001, 42000009, 55999999, 69999999, 83999999, 97999992, 105425265]

for k in range(8):
    print('Processing split' + str(k+1))
    with open('split/kansai-split' + str(k+1) + '.osm', 'w') as new_file:
        with open('kansai-latest.osm', 'r') as file:
            if k > 0:
                new_file.write('''<?xml version='1.0' encoding='UTF-8'?>\n<osm version="0.6s" generator="Osmosis 0.49.2">''')
            for i, line in enumerate(file):
                if start_line[k] < i and i > end_line[k]:
                    print(str(i)+'M') if i % 1000000 == 0 else None
                    new_file.write(line)
            if k != 7:
                new_file.write('</osm>')


