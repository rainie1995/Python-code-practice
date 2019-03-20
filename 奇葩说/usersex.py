from wordcloud import WordCloud,STOPWORDS
import pandas as pd 
import jieba
import matplotlib.pyplot as plt 
#import seaborn as sns
from pyecharts import Geo,Style,Line,Bar,Overlap,Map, Pie
import io
import pymysql

if __name__ == '__main__':
	conn = pymysql.connect(host="localhost",user="root",
 	password="mym@1249690440",database="i_can_i_bibi",port=3306,charset="utf8")
	# conn.text_factory = str
	data = pd.read_sql("select * from orgdata", conn) # 读取orgdata中数据 
	genderData = data.groupby(['gender']) # 将数据按性别分类
	rateDataCount = genderData["id"].agg(["count"]) # 将分组后的数据聚合
	print(rateDataCount)
	attr = ["女", "男"] # 不同的属性名称，做为饼图每一块的注释
	v1 = [rateDataCount["count"][i] for i in range(0, rateDataCount.shape[0])]
	pie = Pie("性别比例")
	pie.add("", attr, v1, is_label_show=True) # add:添加图表的数据和设置各种配置项 is_label_show：是否显示标签
	pie.render(path = "D:\python_code\pictures\gender.html") # render:默认将会在根目录下生成一个 render.html 的文件，支持 path 参数设置文件保存位置,文件用浏览器打开
	conn.commit()
	conn.close()