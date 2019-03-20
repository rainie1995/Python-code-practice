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
            time.sleep(5) # 推迟2秒执行
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
        #print(type(response.text))
        # print(response.read())
        return response.text
    return None


## 获取原始数据
if __name__ == '__main__':
    print("开始")
    movies = {
        "1662856300":u"第23期 邱晨走心讲述抗癌经历 黄执中化身暗黑辩手解读宿命",
        "1629260900":u"第22期 马薇薇飙泪“致离别”"
        # "1629256800":u"第21期 周冬雨爆料马思纯家很有钱 陈铭1v1开杠首次落败",
        # "1596058300":u"第20期 高晓松年轻时像吴亦凡？马薇薇黄执中开杠抱头痛哭",
        # "1596046700":u"第19期 李诞首度下场开杠蔡康永 邱晨自带PPT辩论遭吐槽",
        # "1560634500":u"第18期 马东高晓松开杠互拆套路 李诞“黑粉上位”成主持",
        # "1560624600":u"第17期 蔡康永薛兆丰参战针锋相对 陈铭詹青云学霸大乱斗",
        # "1530507600":u"第16期 董岩磊回忆被骂上热搜",
        # "1530502000":u"第15期 李诞池子爆笑互怼",
        # "1500872700":u"第14期 陈铭放大招引邱晨驳斥",
        # "1500744900":u"第13期 如晶结辩听哭梁洛施",
        # "1467027700":u"第12期 蔡康永薛兆丰挖坑互怼",
        # "1467020800":u"第11期 陈铭灵魂拷问催泪全场",
        # "1447221500":u"第10期 颜如晶首曝暗恋情史",
        # "1443620200":u"第9期 吴谨言尔晴附体掌掴肖骁",
        # "1421444400":u"第8期 肖骁催泪发言感染全场",
        # "1415151600":u"第7期 毛不易为马东包扎遭吐槽",
        # "1398481500":u"第6期 肖骁马薇薇上演教练对决",
        # "1395871500":u"第5期 陈铭花希极限攻防战",
        # "1376903200":u"第4期 臧鸿飞首曝离婚净身出户",
        # "1373596700":u"第3期 如晶走心讲述听哭高晓松",
        # "1355605500":u"第2期 新奇葩剑走偏锋压制如晶",
        # "1352316900":u"第1期 李诞下跪求蔡康永原谅"
    }
    for item in movies:
        saveMoveInfoToFile(item, movies[item], lastId="")