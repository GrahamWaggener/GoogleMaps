import json
if __name__ == '__main__':
    i = 0
    f = open('Records - Copy.json')
    g = open('placesgoneto.csv', 'w', newline='')
    init = 'item,time,long,lat'
    g.write(init)
    data = json.load(f)
    for locations in data['locations']:
        #print(i,":",data['locations'][i]['timestamp'],':',data['locations'][i]['latitudeE7'],':',data['locations'][i]['longitudeE7'])
        iteration = str(i) + ',' + str(data['locations'][i]['timestamp']) + ',' + str(round(data['locations'][i]['latitudeE7']/10000000, 3)) + ',' + str(round(data['locations'][i]['longitudeE7']/10000000, 3))
        g.write('\n')
        g.write(iteration)
        i = i + 1
    f.close()
    g.close()
    print('Done')
