## Python期末项目总结

### 项目合作人：17级苏衍中 18级苏健星 18级林立宇

本项目主要是探讨恶劣天气的分布、空气质量的分布状况、温度、风速、降水方面，来对应相应的地区空气污染情况，实时反馈天气状况 并以散点图的形式来展现中国各大城市的空气质量情况

#### 项目分工
* 由17级苏衍中负责提供数据和对数据故事具有表现力的地图等，包含三份数据，五份实现交互的图表，还提供了py文档、以及Flask+dash的交互功能实现的部分代码
* 由18级林立宇和我共同部署网页，我通过掌握到的python知识，比如**条件判断、推导式、循环遍历等，实现了dash可视化界面，并获取点击的城市分析该城市的数据，实现了具有交互功能的html页面，比如下拉框和数据表格交互，下拉框和条形图交互，编写了网页基本的css样式、html等**

* [Pythonanywhere URL](http://linlyu01.pythonanywhere.com)
* [Github URL](https://github.com/LINLIYU/python_flask_web)


* 页面内分别有2个url
1.	空气质量报告：该页面主要展示国内375个城市空气质量预报，包括api指数、首要污染物、空气质量
2.	天气数据可视化：该页面可以呈现某城市的最高和最低温度、紫外线强度、相对湿度、能见度、风速随时间变化而变化和对应时间的空气质量情况

### 空气质量报告
* 首页地图、表格和点击城市交互图表数据、交互功能的部分代码由17级苏衍中提供，呈现跳转界面和交互功能的实现由我和林立宇负责，通过点击所选的城市，实现跳转，清晰地展现饼状图显示近一周该城市的空气质量情况；散点图则根据空气质量数据来可视化的呈现近一周的空气状况是否良好；折现图则展现了当地城市的近期最高气温、最低气温和紫外线情况，充分地体现了近期的温差情况，由此看出近期某城市的天气状况
* 其中选择城市后的选框的删除键，可以返回到首页的空气质量预报情况表，当浏览者希望重新选择城市可视化的看其天气预报情况，便可通过此实现，既方便也省时。
* 首页点击跳转后，上面的四个按钮可以实现页面跳转交互，跳转到相对应的页面呈现不同的类型图表。

### 天气数据可视化
折现图则展现了当地城市的近期最高气温、最低气温和紫外线情况，充分地体现了近期的温差情况，并且可视化地呈现当天的昼夜温差情况，为浏览者提供当天的衣着多少为适合的便利，并且以框选时间的交互来实现当天实时的气温预计情况，在此页面还可实现对当天或近期某时的气温的总览；条形图下呈现以不同的颜色柱状来表示分类，其实可以看出相对湿度与能见度的相关性不大，风速、能见度和相对湿度基本上保持一个稳定值，直观地反映了该城市的天气状况；
* 同时散点图（地图）的页面中也实现了移动到某地城市时，可以可视化的看到当地的	api指数、首要污染物、空气质量，以及近期的空气状况，动态地显示全国某城市的空气质量情况预报，为浏览者提供有效并可观的信息反馈和图表。
