import requests
import random
import json
import io
import datetime,time
import pymysql
import sys
import lxml
import numpy
import pandas
from pandas import Series

def saveMoveInfoToFile(diqubianma, weidu, jingdu):
    for offset in range(0,2400,24):
        url='https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&limit=24&offset={}&terminal=web&'.format(offset)
        params = {
            "geohash": diqubianma,
            "latitude": weidu,
            "longitude": jingdu  
        }
        for item in params:
            url = url + item + "=" + params[item] + "&"
            print(url)
        responseTxt = getinfo(url) 
        # if responseTxt == None:
        #     time.sleep(5)
        #     responseTxt = getinfo(url)
        returnLastId = parseData(responseTxt) # 调用parsedata函数
        if returnLastId == "-1": 
            print("===============")
            time.sleep(5)
            print("isEnd")
        else: 
            time.sleep(5)


# 解析数据
def parseData(htmlContent):
    data = json.loads(htmlContent) # json.loads(): 解码json数据
    # print(data)
    if json.dumps(data) == "[]":  # json.dump(): 将python对象编码成json字符串
        print("爬完了所有的数据")
        result = '-1' # 遇见此标志说明可以终止
        return result
    col = Series(['id', 'name', 'flavors', 'distance',
        'rating','rating_count','recent_order_num','address'])
    for item in data: 
        # for i in range(8):
        #     if col[i] not in item.keys():
        #         break
        col1 = Series([item['id'], item['name'], item['flavors'][0]['name'],
            item['distance'], item['rating'],item['rating_count'],
            item['recent_order_num'],item['address']])
        if col1.isnull().any() == True:
            print('舍弃')
        else:
            saveOriginalDataToDatabase(item['id'], item['name'], item['flavors'][0]['name'],
            item['distance'], item['rating'], item['rating_count'],item['recent_order_num'], item['address'])
            print("成功导入数据库")
            # print(col1)
        result = '1'
    return result

# 数据存入数据库
def saveOriginalDataToDatabase(id, name, classes, distance, rating, rating_count, monthly_sale, address):
    conn = pymysql.connect("localhost","root","mym@1249690440","eleme",3306)
    # conn.text_factory = str
    cursor = conn.cursor()
    ins='insert into nanjinguniversity(id, name, class, distance, rating, rating_count, monthly_sale, address) values (%s, %s, %s, %s, %s, %s, %s, %s)'
    v = (id, name, classes, distance, rating, rating_count, monthly_sale, address)
    cursor.execute(ins, v)
    cursor.close()
    conn.commit()
    conn.close()
    print("存入数据库")

# 通过url获取数据
def getinfo(url):
    headers = {"Host":"www.ele.me",
        "Connection":"keep-alive",
        "upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cookie":"ubt_ssid=dt0siq45l16a6d2m57d89nbe1bl39w7e_2019-01-27; _utrace=9c68b2055acb9dee0e1ae980753dfd8f_2019-01-27; cna=VBCRFOKZISICAdOiUWYtQzeE; UTUSER=1017635562; pizza7567632f76312f72=5eFWeKtCzB8Xq1BRbIlWwmQEk8Tj8uc35UGobBUlPcYlnkFQlmrV4qlty_Bf_IuU; eleme__ele_me=265fe10d957c506bbb583be441b23a09%3A8dcc4b5c03bd23ad9165b2be8211df18a4968b56; track_id=1548574127|56245b84bf99cf3eb468582a94bb949a92dded9022da962643|b4f16fdfcbf5caadce1bee2d82d0363f; USERID=1017635562; SID=hvj6SOuzdM7A6Q7WRmWCj47vtwawaPLcxzFg; isg=BNPTArtHi7e220djKG2cF_emYldRmx-O85C0FYXwq_IpBPemHFpUm211O3Rqlr9C; pizza73686f7070696e67=CPuz42fVoxnRVcVQ1x33ff-cG5MxyH3YL9F8thM7HvtEwg88F0pDOJXunrWc5ega"}
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        print("success!")
        return response.text
    return None

if __name__ == '__main__':
    print("开始")
    saveMoveInfoToFile('wtsqqgktcrfk', '32.055015', '118.77943')