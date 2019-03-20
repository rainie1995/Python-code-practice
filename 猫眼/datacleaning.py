import pymysql
# 对数据库进行操作
conn = pymysql.connect(host="localhost",user="root",
password="mym@1249690440",database="maoyan",port=3306,charset="utf8")
cursor = conn.cursor()
# 将评分改为0、1、2三个数字
sql1 = """update moviecomment set ranking = case 
when ranking = '4' or ranking = '4.5' or ranking = '5' then 0
when ranking = '2.5' or ranking = '3' or ranking = '3.5' then 1
else 2 end;
"""
# 将时间改为0-7
sql2 = """alter table moviecomment add column day int(20) not null
"""
sql3 = """update moviecomment set day = case
when SUBSTRING(time FROM 1 FOR 8) ='2019/2/5'  then 0
when SUBSTRING(time FROM 1 FOR 8) ='2019/2/6'  then 1
when SUBSTRING(time FROM 1 FOR 8) ='2019/2/7'  then 2
when SUBSTRING(time FROM 1 FOR 8) ='2019/2/8'  then 3
when SUBSTRING(time FROM 1 FOR 8) ='2019/2/9'  then 4
when SUBSTRING(time FROM 1 FOR 9) ='2019/2/10'  then 5
when SUBSTRING(time FROM 1 FOR 9) ='2019/2/11'  then 6
else 7 end; 
"""
# 将城市名改为省份名
sql4 = """update moviecomment m 
set city = (select province from cityname c where m.city = c.city);
"""
cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
cursor.close()
conn.commit() 
conn.close()
print("数据清洗完成！")