from datetime import datetime
import os, json
import time, re

import requests
import pandas as pd

from conf import *


def time_transfer(arg):
    strftime = arg[:10]+' '+arg[11:13]+':'+arg[14:16]+':'+'00'
    time_format = '%Y-%m-%d %X'
    timestamp = time.mktime(time.strptime(strftime, time_format))
    return datetime.fromtimestamp(timestamp)

    
def url_generator(url):
    for day in range(*day_range):
        day = str(day)
        if len(day) == 1:
            day = '0'+str(day)

        for hour in range(*hour_range):
            hour = str(hour)
            if len(hour) == 1:
                hour = '0'+str(hour)
                
            date_time = (year, month, day, hour, minute)
            yield url.format(*date_time)
            
            
def crawler(url, timeout=20):    
    date_index = re.findall('\d{4}-\d{2}-\d{2}-\d{2}-\d{2}', url)[0]
    counter = 3
    while counter > 0:
        time.sleep(2)
        r = requests.get(
            url, 
            #headers=headers, 
            timeout=timeout,
        )
        if r.status_code == 200:
            d = json.loads(r.text)
            d['time'] = time_transfer(date_index)
            return d
        counter -= 1
    print('status code {}: {}'.format(r.status_code, url))
    
    
def save_info(csv_name):
    info_url = 'http://sq.szmb.gov.cn/city/invoke/getAllMonitorInfo'
    info = crawler(info_url)
    df = pd.read_json(info).T
    csv_path = os.path.abspath(__file__).replace(os.path.basename(__file__), csv_name)
    df.to_csv(csv_path)
    
            
def crawl_data(url_template):
    for url in url_generator(url_template): 
        print(url)
        yield crawler(url)
    
        
def save_data_by_paramter(feature):
    data_url = base_url.replace('feature', features[feature])
    data = list(crawl_data(data_url))
    
    # if feature is wind, transfrom
    if feature == 'wind':
        for d in data:
            for k,v in d.items():
                if k != 'time':
                    ws, wd = v['ws'], v['wd']
                    v = '/'.join([str(ws), str(wd)])
                    d[k] = v
                
    df = pd.DataFrame(data)
    df.index = df.loc[:,'time']
    df.drop(['time'], axis=1, inplace=True)
    short_month = short_months[str(int(month))]
    month_path = os.path.join('csv', short_month)
    if not os.path.exists(month_path):
        os.makedirs(month_path)
    df.to_csv('csv/{0}/sz_{0}_{1}.csv'.format(short_month, feature))
    
    
def main():
    for f in content:
        save_data_by_paramter(f)
    
            
if __name__ == '__main__':
    save_data_by_paramter('wind')
    #save_info('monitor_info.csv')
    #main()
