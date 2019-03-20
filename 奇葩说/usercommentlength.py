from wordcloud import WordCloud,STOPWORDS
import pandas as pd 
import jieba
import matplotlib.pyplot as plt 
#import seaborn as sns
from pyecharts import Geo,Style,Line,Bar,Overlap,Map, Pie
import io
import pymysql


if __name__ == '__main__':
	conn = pymysql.connect("localhost","root","mym@1249690440","i_can_i_bibi",3306)
	# conn.text_factory = str
	data = pd.read_sql("select * from orgdata", conn)
	lengthData = data.groupby(['length'])
	lengthDataCount = lengthData["movieId"].agg([ "count"])
	lengthDataCount.reset_index(inplace=True)
	print(lengthDataCount)

	attr = ["20字以内", "20~50字", "50~100字", "100字以上"]
	v1 = [lengthDataCount["count"][i] for i in range(0, lengthDataCount.shape[0])]
	bar = Line("评论字数")
	bar.add("数量",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
			xaxis_interval=0,is_splitline_show=True,is_label_show=True)
	bar.render("D:\python_code\pictures\comment_word_count.html")
	
	conn.commit()
	conn.close()
