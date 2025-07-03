import json
import math
import requests
import pandas as pd

'''
高德地图关键词搜索功能可能存在返回的最大poi数量限制，
因此需要合理控制搜索区域，或使用更加精细的搜索类别以避免无法返回全部数据。
'''


def get_poi(city, type, page):
    parameters = {'key': key, 'types': type, 'city': city, 'page_num': page, 'page_size': 25}
    res = requests.get('https://restapi.amap.com/v3/place/text?', params=parameters)
    json_dict = json.loads(res.text)
    poi_list = json_dict['pois']
    count = json_dict['count']
    for poi in poi_list:
        print(poi)
    return count, poi_list


if __name__ == '__main__':
    key = 'xxxxxx'  # 填写自己的key
    city = 320102  # 填写城市名或城市编码，320102为玄武区
    type = 150500  # 填写poi分类编码，尽量选择细分分类，150500为地铁站

    data_list = []
    count, temp_list = get_poi(city, type, 1)

    for i in range(0, math.ceil(float(count) / 25)):
        temp_count, temp_list = get_poi(city, type, i)
        data_list.extend(temp_list)

    filtered_data = []
    for item in data_list:
        filtered_item = {key: value for key, value in item.items()}
        filtered_data.append(filtered_item)

    df = pd.DataFrame(filtered_data)
    df.to_excel("1 城市poi基础数据.xlsx", index=False)
