## Python期末项目总结

### 项目合作人：17级苏衍中 18级苏健星 18级林立宇

本项目主要是探讨恶劣天气的分布、空气质量的分布状况、温度、风速、降水方面，来对应相应的地区空气污染情况，实时反馈天气状况 并以散点图的形式来展现中国各大城市的空气质量情况

#### 项目分工
* 由17级苏衍中负责提供数据和对数据故事具有表现力的地图等，包含三份数据，五份实现交互的图表，还提供了py文档
* 由18级苏健星和我共同部署网页，我通过掌握到的python知识，比如**条件判断、推导式、循环遍历等，实现了dash可视化界面，并获取点击的城市分析该城市的数据，实现了具有交互功能的html页面，比如下拉框和数据表格交互，下拉框和条形图交互，编写了网页基本的css样式、html等**，最后将网页部署到Pythonanywhere，但可能由于不能跨域，导致pythonanywhere不能实现交互，我已经将本地录屏上传到github上。

* [Pythonanywhere URL](http://linlyu01.pythonanywhere.com)：linlyu01.pythonanywhere.com
* [Github URL](https://github.com/LINLIYU/python_flask_web)：https://github.com/LINLIYU/python_flask_web


* 页面内分别有2个url
1.空气质量报告：该页面主要展示国内城市空气质量预报，包括api指数、首要污染物、空气质量
2.天气数据可视化：该页面展示了北京的最高和最低温度、紫外线强度、相对湿度、能见度、风速随时间变化而变化和对应时间的空气质量