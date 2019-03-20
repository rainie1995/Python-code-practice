import pymysql
import pandas as pd 
import matplotlib.pyplot as plt 
from pyecharts import Geo,Style,Line,Bar,Overlap,Map, Pie


if __name__ == '__main__':
    conn = pymysql.connect(host="localhost",user="root",
    password="mym@1249690440",database="maoyan",port=3306,charset="utf8")
    data = pd.read_sql("select * from moviecomment", conn) # 读取moviecomment中的数据
    cityData = data.groupby(['city']) # 将数据按时间分类
    citydata = cityData["city"].agg(["count"]) # 将分组后的数据聚合
    citydata.reset_index(inplace=True)  # 重置连续的index

    attr = ['北京','天津','上海','江苏','浙江','福建','江西','广西','广东','海南','山东','山西','安徽','湖北','湖南',
    '重庆','云南','贵州','四川','青海','甘肃','宁夏','陕西','河南','河北','内蒙古','黑龙江','吉林','辽宁','新疆','西藏'] # 不同的属性名称，做为折线图的注释
    v1 = [citydata["count"][i] for i in range(0, citydata.shape[0])]
    pie = Pie("评论数量", title_pos='right', width=1000,height=400)
    pie.add("", attr, v1, is_label_show=True, legend_pos='left', label_text_color=None, legend_orient='vertical', radius=[30, 75])
    pie.render("D:\python_code\sample\猫眼\comment_city_count.html")
    conn.commit()
    conn.close()
