import random
import json
import io
import datetime,time
import pymysql
import sys

def updateWeek():
    conn = pymysql.connect("localhost","root","mym@1249690440","i_can_i_bibi",3306)
    # conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute("alter table orgdata add column week varchar(40)")
    cursor.execute("select * from orgdata")
    values = cursor.fetchall()
    cursor.close()
    for item in values:
        realTime = time.localtime(float(item[4]))
        realTime = time.strftime("%A",realTime) # 返回本地完整信息名称
        sql = "UPDATE orgdata SET week =\"" + realTime + "\" WHERE id =\"" + item[0] + "\""
        cc = conn.cursor()
        cc.execute(sql)
        cc.close()

    conn.commit()
    conn.close()
    time.localtime()


## 转换数据
if __name__ == '__main__':
	updateWeek()