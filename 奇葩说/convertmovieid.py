import random
import json
import io
import datetime,time
import pymysql
import sys


def updateMovieId(): 
    conn = pymysql.connect(host="localhost",user="root",
 	password="mym@1249690440",database="i_can_i_bibi",port=3306,charset="utf8")
    # conn.text_factory = str
    cursor = conn.cursor() # 数据库连接操作
    cursor.execute("select * from orgdata") # 执行数据库操作
    values = cursor.fetchall() # 得到select结果的多行记录，记为values
    cursor.close() # 关闭数据库连接，关闭指针对象
    for item in values:
        sql = "UPDATE orgdata SET movieId=\""+item[0].split("_")[0]+ "\" WHERE id =\"" + item[0] + "\""
        # 以"_"对movieId进行分割
        print(sql)
        cc = conn.cursor()
        cc.execute(sql)
        cc.close()
    conn.commit() # 提交事务
    conn.close() # 关闭数据库连接，关闭连接对象

## 转换数据
if __name__ == '__main__':
	updateMovieId()