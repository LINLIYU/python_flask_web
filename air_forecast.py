# -*- coding: utf-8 -*-
# author:           inspurer(月小水长)
# pc_type           lenovo
# create_time:      2020/1/4 14:36
# file_name:        air_forecast.py
# github            https://github.com/inspurer
# qq邮箱            2391527690@qq.com
# 微信公众号         月小水长(ID: inspurer)


import requests
import pandas as pd
import csv
import os

file_name = 'air_forecast.csv'
if not os.path.exists(file_name):
    with open(file_name,"w",encoding='utf-8-sig',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['城市','日期','最高温度','最低温度','白天天气状况','晚间天气状况',
                         '风向','风力','风速(公里/小时)','相对湿度','降水量','紫外线强度指数','能见度(公里)'])

data = pd.read_csv('china-city-list.csv')

city_list = data['Admin_ district_CN'].unique()

base_url = 'https://api.heweather.net/s6/weather/forecast?location={}&key=c723f66be3ee4e13b387262f8eb0e8e7'


for city in city_list:
    res = requests.get(url=base_url.format(city)).json()
    print(res)
    data = None
    try:
        data = res['HeWeather6'][0]['daily_forecast']
    except:
        data = res['HeWeather6'][1]['daily_forecast']
    with open(file_name,"a+",encoding='utf-8-sig',newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow([city,row['date'],row['tmp_max'],row['tmp_min'],row['cond_txt_d'],row['cond_txt_n'],
                             row['wind_dir'],row['wind_sc'],row['wind_spd'],row['hum'],row['pcpn'],row['uv_index']
                             ,row['vis']])