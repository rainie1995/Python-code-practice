import numpy as np
import pymysql
import matplotlib.pyplot as plt
from snownlp import SnowNLP
conn = pymysql.connect("localhost","root","mym@1249690440","maoyan",3306)
cursor = conn.cursor()
sql = 'select comment from moviecomment where comment like "%特效%"'
cursor.execute(sql)
values = cursor.fetchall() # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回()
sentimentslist = []
for item in values:
    item = " ".join(item)
    senValue = SnowNLP(item).sentiments
    sentimentslist.append(senValue)

plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor="#4F8CD6") # 直方图
plt.xlabel("Sentiments Probability")
plt.ylabel("Quantity")
plt.title("Analysis of Sentiments for liulangdiqiu_texiao")
plt.show()
cursor.close()