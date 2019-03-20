import requests
import random
import json
import io
import datetime,time
import pymysql
import sys


def saveMoveInfoToFile(movieId, movieName, lastId):
    url = "https://sns-comment.iqiyi.com/v3/comment/get_comments.action?agent_type=118&agent_version=9.11.5&authcookie=null&business_type=17&"
    # str1 = "last_id=184753506321&page=&page_size=20&types=time"
    # str2 = "content_id=1662861200&hot_size=0"
    params = {
        "content_id": movieId,
        "hot_size": "0",
        "last_id": "",
        "page": "",
        "page_size": "20"  
    }
    if lastId != "":
        params["last_id"] =  lastId
    for item in params:
        url = url + item + "=" + params[item] + "&"
    url = url + "types=time"
    try:
        responseTxt = getMoveinfo(url)
        returnLastId = parseData(movieId, movieName, responseTxt) # 调用parsedata函数
        if returnLastId == "-1": 
            print("===============")
            print(movieName)
            print(url)
            print("===============")
            time.sleep(5)
            print("isEnd")
        else: 
            time.sleep(5) # 推迟5秒执行
            saveMoveInfoToFile(movieId, movieName, returnLastId)
    except Exception as e:
        print("exception")
        saveMoveInfoToFile(movieId, movieName, lastId) # 递归

# 解析数据，无其他作用    
def parseData(movieId, movieName, htmlContent):
    data = json.loads(htmlContent)['data']['comments'] # json.loads(): 解码json数据
    # print(data)
    lastId = "-1"
    if json.dumps(data) == "[]":  # json.dump(): 将python对象编码成json字符串
        print("爬完了%s的评论" % movieName)
        return lastId
    for item in data:
        if "content" not in item.keys():
            continue
        print("进入循环")
        # print(item)
        # originalData = json.dumps(item)
        saveOriginalDataToDatabase(item["id"], movieId, item['content'], item['userInfo']['gender'], item['addTime'], item['userInfo']['uname'], item['userInfo']['uid'], item['userInfo']['uidType'],  movieName)
        print("成功导入数据库")
        lastId = item['id']
    return lastId

# 连接数据库，无其他作用        
def saveOriginalDataToDatabase(msgId, movieId,  content, gender, addTime, uname, uid, uidType, movieName):
    conn = pymysql.connect("localhost","root","mym@1249690440","i_can_i_bibi",3306)
    # conn.text_factory = str
    cursor = conn.cursor()
    ins='insert into orgdata (id, movieId, content, gender, addDate, uname, uid, uidType, movieName) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    v = (movieId+ "_" + msgId, movieId, content, gender, addTime, uname, uid, uidType, movieName)
    cursor.execute(ins, v)
    cursor.close()
    conn.commit()
    conn.close()
    print("存入数据库")

 #主函数，进行网络请求   
def getMoveinfo(url):
    # session = requests.Session()
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    #     "Accept": "application/json",
    #     "Referer": "https://www.iqiyi.com/v_19rqs2dqf0.html",
    #     "Origin": "https://m.iqiyi.com",
    #     "Host": "sns-comment.iqiyi.com",
    #     "Connection": "keep-alive",
    #     "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6",
    #     "Accept-Encoding": "gzip, deflate"
    # }
    response = requests.get(url)
    # response.read().decode('utf8')
    if response.status_code == 200:
        print("success!")
        # print(type(response.text))
        # print(response.read())
        return response.text
    return None


## 获取原始数据
if __name__ == '__main__':
    print("开始")
    movies = {"1662856300":u"第23期 邱晨走心讲述抗癌经历 黄执中化身暗黑辩手解读宿命"}
    for item in movies:
        saveMoveInfoToFile(item, movies[item], lastId="")