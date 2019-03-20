from wordcloud import WordCloud,STOPWORDS
import pandas as pd 
from PIL import Image
import numpy as np
import jieba
import io, pymysql
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import copy

if __name__ == '__main__':
	conn = pymysql.connect("localhost","root","mym@1249690440","maoyan",3306)
	data = pd.read_sql("select * from moviecomment", conn)
	comment = jieba.cut(str(data["comment"]),cut_all=False) # 对data["content"]内容进行分词，不采用全模式 
	wl_space_split = " ".join(comment) # 连接字符串数组（以""内指定的字符连接）
	stop_words = [line.strip() for line in io.open(r'D:\python_code\sample\朴素贝叶斯\text_classification\stop\stopword.txt', errors='ignore').readlines()]
	stop_words.append(u"还是")
	stop_words.append(u"差点")
	stop_words.append(u"只能")
	stop_words.append(u"真的")
	stop_words.append(u"这样")
	stop_words.append(u"感觉")
	stop_words.append(u"有些")
	stop_words.append(u"不是")
	stop_words.append(u"没有")
	stop_words.append(u"完全")
	stop_words.append(u"看到")
	stop_words.append(u"来点")
	stop_words.append(u"就是")
	stop_words.append(u"或许")
	stop_words.append(u"东西")
	stop_words.append(u"这次")
	stop_words.append(u"如此")
	stop_words.append(u"来看")
	stop_words.append(u"但是")
	stop_words.append(u"如何")
	stop_words.append(u"那么")
	stop_words.append(u"已经")
	stop_words.append(u"其余")
	stop_words.append(u"部分")
	stop_words.append(u"一个")
	stop_words.append(u"这么")
	stop_words.append(u"已经")
	stop_words.append(u"两个")
	stop_words.append(u"只有")
	stop_words.append(u"虽然")
	stop_words.append(u"我们")
	stop_words.append(u"现在")
	stop_words.append(u"除了")
	stop_words.append(u"接着")
	stop_words.append(u"很多")
	stop_words.append(u"至少")
	stop_words.append(u"从头")
	stop_words.append(u"为了")
	stop_words.append(u"一堆")
	stop_words.append(u"从来")
	stop_words.append(u"一样")
	stop_words.append(u"旁边")
	stop_words.append(u"有点")
	stop_words.append(u"什么")
	stop_words.append(u"之后")
	stop_words.append(u"本来")
	stop_words.append(u"后面")
	stop_words.append(u"觉得")

	wc = WordCloud(width=1920,height=1080,background_color='white', # 背景色
	font_path="C:\Windows\Fonts\simhei.ttf", # 字体路径，英文不用设置路径，中文需要，否则无法正确显示图形,必须选择支持中文的字体
    stopwords=stop_words,max_font_size=400,random_state=50)
	wc.generate_from_text(wl_space_split) # 显示图像
	plt.imshow(wc) # 用plt显示图片
	plt.axis("off") # 不显示坐标轴
	wc.to_file(r'D:\python_code\sample\猫眼\word_cloud.png') # 保存图片
	conn.commit()
	conn.close()