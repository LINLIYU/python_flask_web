# -*- coding: utf-8 -*-
# pc_type           lenovo
# create_time:      2020/1/4 12:13
# file_name:        aqi_forecast.py

import requests
import pandas as pd
import csv
import os

file_name = 'aqi_forecast.csv'
if not os.path.exists(file_name):
    with open(file_name,"w",encoding='utf-8-sig',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['城市','日期','aqi指数','首要污染物','空气质量'])

data = pd.read_csv('china-city-list.csv')

city_list = data['Admin_ district_CN'].unique()

print(len(city_list))

base_url = 'https://api.heweather.net/s6/air/forecast?location={}&key=c723f66be3ee4e13b387262f8eb0e8e7'

for city in city_list:
    res = requests.get(url=base_url.format(city)).json()
    print(res)
    data = None
    try:
        data = res['HeWeather6'][0]['air_forecast']
    except:
        data = res['HeWeather6'][1]['air_forecast']
    with open(file_name,"a+",encoding='utf-8-sig',newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow([city,row['date'],row['aqi'],row['main'],row['qlty']])

