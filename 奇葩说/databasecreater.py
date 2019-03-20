import pymysql, time, datetime

def createOriginalDatabase():
    conn = pymysql.connect(host="localhost",user="root",
 	password="mym@1249690440",database="i_can_i_bibi",port=3306,charset="utf8")
    # conn.text_factory = str
    cursor = conn.cursor()
    # 需要解析的数据表
    # cursor.execute(
        # 'create table comments(id varchar, movieId varchar, name varchar(40), comment TEXT, gender varchar, addTime varchar(20))')
    # 原始数据表
    sql = """create table orgdata (id varchar(40), movieId varchar(40), content varchar(4000), 
    gender varchar(40),addDate varchar(40), uname varchar(40), uid varchar(40), uidType varchar(40), movieName varchar(40));"""
    cursor.execute(sql)
    cursor.close()
    conn.commit() 
    conn.close()

if __name__ == '__main__':
    # 只能创建一次
    createOriginalDatabase()
    # createDealDatabase()

