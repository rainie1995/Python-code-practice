import pymysql, time, datetime

def createOriginalDatabase():
    conn = pymysql.connect(host="localhost",user="root",
 	password="mym@1249690440",database="eleme",port=3306,charset="utf8")
    # conn.text_factory = str
    cursor = conn.cursor()
    # 需要解析的数据表
    # cursor.execute(
        # 'create table comments(id varchar, movieId varchar, name varchar(40), comment TEXT, gender varchar, addTime varchar(20))')
    # 原始数据表
    sql = """create table nanjinguniversity (id varchar(40), name varchar(40), class varchar(40), 
    distance varchar(40), rating varchar(40),
    rating_count varchar(40), monthly_sale varchar(40),  address varchar(100));"""
    cursor.execute(sql)
    cursor.close()
    conn.commit() 
    conn.close()

if __name__ == '__main__':
    # 只能创建一次
    createOriginalDatabase()
    # createDealDatabase()