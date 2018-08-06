year = '2018'
month = '07'
day_range = (1, 31)
hour_range = (0, 24)
minute_list = ('00', '30')

base_url = 'http://weather.szmb.gov.cn/szdcc/api/selectData.do?dataType=json&area=all&datetime={}-{}-{}-{}-{}&qType=feature'

short_months = {
    '1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr', '5': 'May', '6': 'Jun',
    '7': 'Jul', '8': 'Aug', '9': 'Sept', '10': 'Oct', '11': 'Nov', '12': 'Dec',
}


features = {
    'temperature': 'TemperatureM', 'rain': 'RainH01', 'wind': 'WindHmaxS', 
    'humidity': 'HumidityM', 'pressure': 'PressureM', 'visibility': 'VisDmin'
}

content = ['temperature', 'rain', 'wind', 'pressure', 'visibility', 'humidity']


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'http://sq.szmb.gov.cn/city/view/weathermonitor.html',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Host': 'sq.szmb.gov.cn',
    'Connection': 'keep-alive',
}
