import json
import math
import requests
import pandas as pd

'''
高德地图周边搜索功能与多边形搜索功能返回的最大poi数量为200，
因此需要合理控制搜索半径，或使用更加精细的搜索类别以避免过多搜索结果达到上限。
'''

def get_poi_count(location, types, radius):
    for page in range(1, 9):
        parameters = {'key': key, 'types': types, 'location': location, 'radius': radius, 'page_num': page,
                      'page_size': 25}
        res = requests.get('https://restapi.amap.com/v5/place/around?', params=parameters)
        json_dict = json.loads(res.text)
        count = json_dict['count']
        if int(count) < 25:
            return (page - 1) * 25 + int(count)
    return 200


if __name__ == '__main__':
    key = 'xxxxxx'  # 填写自己的key
    class_name = {'050000': '餐饮服务', '060000': '购物服务', '070000': '生活服务', '110000': '风景名胜',
                  '120000': '商务住宅', '170000': '公司企业', }  # 填写需要搜索周边范围内数量的poi类别与名称
    radius = 200  # 填写周边搜索半径（单位：m）

    data_list = []

    df = pd.read_excel('1 城市poi基础数据.xlsx')
    location_data = df['location']
    for class_key in class_name:
        temp_list = []
        for location in location_data:
            temp_list.append(get_poi_count(location, class_key, radius))
            print(location, class_key, 'finish')
        df[class_name[class_key]] = temp_list

    df.to_excel("2 城市poi详细数据.xlsx", index=False)
