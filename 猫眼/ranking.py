import pymysql
import pandas as pd 
import matplotlib.pyplot as plt 
from pyecharts import Geo,Style,Line,Bar,Overlap,Map, Pie


if __name__ == '__main__':
    conn = pymysql.connect(host="localhost",user="root",
    password="mym@1249690440",database="maoyan",port=3306,charset="utf8")
    data = pd.read_sql("select * from moviecomment", conn) # 读取moviecomment中的数据
    rankingData = data.groupby(['ranking']) # 将数据按时间分类
    rankingdata = rankingData["ranking"].agg(["count"]) # 将分组后的数据聚合
    rankingdata.reset_index(inplace=True)  # 重置连续的index

    attr = ['好评','中评','差评'] # 不同的属性名称，做为折线图的注释
    v1 = [rankingdata["count"][i] for i in range(0, rankingdata.shape[0])]
    bar = Bar("评论数量")
    bar.add("数量",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
        xaxis_interval=0,is_splitline_show=True,is_label_show=True)
    bar.render("D:\python_code\sample\猫眼\comment_ranking_count.html")
    conn.commit()
    conn.close()
