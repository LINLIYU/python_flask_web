# -*- coding: utf-8 -*-
# pc_type           lenovo
# create_time:      2020/1/4 18:47
# file_name:        dash_viewer.py

from flask import Flask,render_template,request
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go

date = '2020-01-05'
city = '北京'
# 加载数据
import pandas as pd

df1 = pd.read_csv('air_forecast.csv')
d1 = df1[df1['城市']==city]

quality_level = ['优','良','轻度污染','中度污染','重度污染']
df2 = pd.read_csv('aqi_forecast.csv')
d2 = df2[df2['日期']==date]
quality_count = [d2[d2['空气质量']==level].shape[0] for level in quality_level]

df3 = pd.read_csv('china-city-list.csv',usecols=['Admin_ district_CN','Latitude','Longitude'])

df3.drop_duplicates(subset=['Admin_ district_CN'],keep='first',inplace=True)
df3.reset_index(drop=True,inplace=True)

texts = []
for i in range(df3.shape[0]):
    ct = df3.at[i,'Admin_ district_CN']
    text = ct+'<br>'
    text += '日期\taqi指数\t首要污染物\t空气质量<br>'
    data = df2[df2['城市']==ct]
    dt = data['日期'].tolist()
    aqi =  data['aqi指数'].tolist()
    main = data['首要污染物'].tolist()
    quality = data['空气质量'].tolist()
    for d,a,m,q in zip(dt,aqi,main,quality):
        text += d+'\t'+str(a)+'\t'+m+'\t'+q+'<br>'
    texts.append(text)
df3['text'] = texts

server = Flask(__name__)

app = dash.Dash(__name__, server=server, url_base_pathname='/dash/')

colors = dict(background = '#ffffff', text = '#7FDBFF')

app.layout = html.Div([
    html.H1(
        children='天气数据可视化',
        style=dict(textAlign='center', color=colors['text'])),
    dcc.Dropdown(
        id='my_dropdown',
        placeholder='请选择图表',
        options=[{'label': '折线图', 'value': '1'},
                 {'label': '条形图', 'value': '2'},
                 {'label': '饼状图', 'value': '3'},
                 {'label': '散点图', 'value': '4'}],
        value='1'),
    dcc.Graph(id='my-graph')
])


@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)
def update_graph(select_index):


    if select_index == '1':
        figure = {
            'data': [
                go.Scatter(
                    x=d1['日期'].tolist(),
                    y=d1[yi].tolist(),
                    mode='lines',
                    name=city+yi
                               ) for yi in ['最高温度','最低温度','紫外线强度指数']
            ],

            'layout': [
                go.Layout(
                    height=350,
                    hovermode='closest',
                    title='折线图'
                )
            ]
        }
        return figure
    elif select_index == '2':
        figure = {
            'data': [
                go.Bar(
                    x=d1['日期'].tolist(),
                    y=d1[yi].tolist(),
                    name=city+yi
                ) for yi in ['相对湿度','能见度(公里)','风速(公里/小时)']],

            'layout': [
                go.Layout(
                    height=350,
                    hovermode='closest',
                    title='条形图',
                )
            ]
        }
        return figure

    elif select_index=='3':
        figure = {
            'data': [
                go.Pie(
                    labels=quality_level,
                    values=quality_count,
                    name='legend'
                )],

            'layout': [
                go.Layout(
                    height=350,
                    hovermode='closest',
                    title='饼状图'
                )
            ]
        }
        return figure

    elif select_index=='4':
        figure = {
            'data': [
                go.Scatter(
                    x=df3['Longitude'].tolist(),
                    y=df3['Latitude'].tolist(),
                    text = df3['text'].tolist(),
                    mode='markers',
                    marker={'size': 15},
                    name='legend'
                )],

            'layout': [
                go.Layout(
                    height=350,
                    hovermode='closest',
                    title ='散点图'
                )
            ]
        }
        return figure

citys = []
for name,aqi,main,quality in zip(d2['城市'].tolist(),d2['aqi指数'].tolist(),d2['首要污染物'].tolist(),d2['空气质量'].tolist()):
    citys.append({
        'name':name,
        'aqi':aqi,
        'main':main,
        'quality': quality
    })

@server.route('/')
def index():
    return render_template('index.html',date=date,citys=citys)

@server.route('/process',methods=['POST'])
def process():
    global d1,city
    city = request.form['city']
    print(city)
    d1 = df1[df1['城市']==city]
    return 'ssss'

if __name__ == '__main__':
    server.run(debug=True,port=8051)
