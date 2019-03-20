from wordcloud import WordCloud,STOPWORDS
import pandas as pd 
from PIL import Image
import numpy as np
import jieba
import matplotlib.pyplot as plt 
#import seaborn as sns
from pyecharts import Geo,Style,Line,Bar,Overlap,Map
import io, pymysql
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import copy



if __name__ == '__main__':
	conn = pymysql.connect("localhost","root","mym@1249690440","i_can_i_bibi",3306)
	# conn.text_factory = str
	data = pd.read_sql("select * from orgdata", conn)
	jieba.add_word("马薇薇", freq = 20000, tag = None) # 动态修改词典，add_word保证添加的词语不会被cut掉
	comment = jieba.cut(str(data["content"]),cut_all=False) # 对data["content"]内容进行分词，不采用全模式 
	wl_space_split = " ".join(comment) # 连接字符串数组（以""内指定的字符连接）
	backgroudImage = np.array(Image.open("D:\qipashuo.jpg"))
	stopword = STOPWORDS.copy() # stopwprd初始值定义为STOPWORDS词库中的词(英文)
	stopword.add(u"奇葩") # 添加其他停用词
	stopword.add(u"一部")
	stopword.add(u"第一")
	stopword.add(u"现在")
	stopword.add(u"只有")
	stopword.add(u"这个")
	stopword.add(u"选手")
	stopword.add(u"前排")
	stopword.add(u"一个")
	stopword.add(u"没有")
	stopword.add(u"什么")
	stopword.add(u"有点")
	stopword.add(u"感觉")
	stopword.add(u"无名之辈")
	stopword.add(u"就是")
	stopword.add(u"觉得")
	stopword.add(u"真的")
	stopword.add(u"知道")
	stopword.add(u"但是")
	stopword.add(u"已经")
	stopword.add(u"不能")
	stopword.add(u"其实")
	stopword.add(u"那个")
	stopword.add(u"所以")
	stopword.add(u"不是")
#	.add('一部').add('一个').add('没有').add('什么').add('有点').add('感觉').add('无名之辈').add('就是').add('觉得')
	wc = WordCloud(width=1920,height=1080,background_color='white', # 背景色
		mask=backgroudImage, # 背景图形，如果想根据图片绘制，则需要设置
		font_path="C:\Windows\Fonts\simhei.ttf", # 字体路径，英文不用设置路径，中文需要，否则无法正确显示图形,必须选择支持中文的字体
		stopwords=stopword,max_font_size=400,
		random_state=50)
	wc.generate_from_text(wl_space_split) # 显示图像
	plt.imshow(wc) # 用plt显示图片
	plt.axis("off") # 不显示坐标轴
	wc.to_file(r'D:\python_code\pictures\unknown_word_cloud.png') # 保存图片
	
	
	conn.commit()
	conn.close()
	# recolor wordcloud and show
	# we could also give color_func=image_colors directly in the constructor
	# 我们还可以直接在构造函数中直接给颜色
	# 通过这种方式词云将会按照给定的图片颜色布局生成字体颜色策略
#	plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
#	plt.axis("off")
#	plt.figure()
#	plt.imshow(backgroud_Image, cmap=plt.cm.gray, interpolation="bilinear")
#	plt.axis("off")
#	plt.show()
		
	#
#	wc.generate_from_text(wl_space_split)
#	plt.imshow(wc)
#	plt.axis('off')#不显示坐标轴  
#	plt.show()
#	wc.to_file(r'laji.jpg')