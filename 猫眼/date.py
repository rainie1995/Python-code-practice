import pymysql
import pandas as pd 
import matplotlib.pyplot as plt 
from pyecharts import Geo,Style,Line,Bar,Overlap,Map, Pie


if __name__ == '__main__':
    conn = pymysql.connect(host="localhost",user="root",
    password="mym@1249690440",database="maoyan",port=3306,charset="utf8")
    data = pd.read_sql("select * from moviecomment", conn) # 读取moviecomment中的数据
    dateData = data.groupby(['day']) # 将数据按时间分类
    daydata = dateData["day"].agg(["count"]) # 将分组后的数据聚合
    daydata.reset_index(inplace=True)  # 重置连续的index

    attr = ['2.5','2.6','2.7','2.8','2.9','2.10','2.11','2.12'] # 不同的属性名称，做为折线图的注释
    v1 = [daydata["count"][i] for i in range(0, daydata.shape[0])]
    line = Line("每天评论数量")
    # add:添加图表的数据和设置各种配置项 is_label_show：是否显示标签
    line.add("数量",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    xaxis_interval=0,is_splitline_show=True,is_label_show=True)
    # render:默认将会在根目录下生成一个 render.html 的文件，支持 path 参数设置文件保存位置,文件用浏览器打开
    line.render("D:\python_code\sample\猫眼\comment_date_count.html")
    conn.commit()
    conn.close()