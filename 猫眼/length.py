import pandas as pd 
import pymysql
import matplotlib.pyplot as plt 
from pyecharts import Geo,Style,Line,Bar,Overlap,Map, Pie


if __name__ == '__main__':
	conn = pymysql.connect("localhost","root","mym@1249690440","maoyan",3306)
	data = pd.read_sql("select * from moviecomment", conn)
	lengthData = data.groupby(['length'])
	lengthDataCount = lengthData["length"].agg([ "count"])
	lengthDataCount.reset_index(inplace=True)
	# print(lengthDataCount)

	attr = ["20字以内", "20~50字", "50~100字", "100字以上"]
	v1 = [lengthDataCount["count"][i] for i in range(0, lengthDataCount.shape[0])]
	line = Line("评论字数")
	line.add("数量",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
			xaxis_interval=0,is_splitline_show=True,is_label_show=True)
	line.render("D:\python_code\sample\猫眼\comment_length_count.html")
	
	conn.commit()
	conn.close()
