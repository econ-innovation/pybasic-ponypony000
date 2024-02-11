#1.使用高德API获取985大学地理信息

import requests
import json

#定义一个爬取大学信息的函数
def get_locaiton(university):

    # 构建请求 指定返回的数据格式为JSON
    key = "5ea71aaec2f483badb692869abe47bb9"
    url = f'https://restapi.amap.com/v3/geocode/geo?address={university}&output=JSON&key={key}'
    # 发送请求
    response = requests.get(url)
    # 打印响应结果
    print(response.text)
    # 解析数据
    json_data = json.loads(response.text)
    # 获取地理信息
    geo = json_data["geocodes"][0]["location"]
    #geo_d = json_data["geocodes"][0]["formatted_address"]
    return geo

with open("985university.txt","r",encoding='utf-8') as f:
    for u in f.readlines():
        university = u.strip() # 去除可能的空格和换行符
        location = get_locaiton(u)
        #写入文件
        with open("985location.txt","a",encoding="utf-8") as fs:
            fs.write(f"{university}|{location}\n")




