import pymysql
import pandas as pd 
import matplotlib.pyplot as plt 
from pyecharts import Geo,Style,Line,Bar,Overlap,Map, Pie


if __name__ == '__main__':
    conn = pymysql.connect(host="localhost",user="root",
    password="mym@1249690440",database="maoyan",port=3306,charset="utf8")
    cursor = conn.cursor()
    sql1 = "alter table moviecomment add column count_city int(40);"
    sql2 = """
    update moviecomment as m1 inner join
    (select city, count(*) as counting from moviecomment group by city) as m2
    on m1.city = m2.city set m1.count_city = m2.counting;
    """
    cursor.execute(sql1)
    cursor.execute(sql2)
    data = pd.read_sql("select * from moviecomment", conn) # 读取moviecomment中的数据
    cursor.close()
    conn.commit() 
    conn.close()
    cityData = data.groupby(['city','ranking','count_city']) # 将数据先按城市分类，再按评分分类
    citydata = cityData["id"].agg(["count"]) # 将分组后的数据的id进行叠加
    citydata.reset_index(inplace=True)  # 重置连续的index
    citydata['praise_rate'] = None
    citydata = citydata[~citydata['ranking'].isin([1.0, 2.0])]
    citydata['praise_rate'] = citydata.apply(lambda x: x['count'] / x['count_city'], axis=1)
    
    bar = Bar("各省好评率对比", width=1000,height=700)
    bar.add("百分比",citydata['city'],citydata['praise_rate'], is_convert=True,is_stack=True,xaxis_rotate=30,
    xaxis_interval=0,is_splitline_show=True,is_label_show=True)
    bar.render("D:\python_code\sample\猫眼\province_ranking.html")