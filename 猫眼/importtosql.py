import numpy as np
import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine
f = open("D:\\python_code\\sample\\猫眼\\movieComments.csv",'rb')
data = pd.read_csv(f, names = ['id', 'city', 'comment', 'ranking', 'time'])
df = data.drop_duplicates() # 去掉重复行
df1 = df.dropna(how = 'any', inplace = False) # 去掉有空字段的行
df1 = df1.reset_index(drop = True)
# 选取city一栏中非空不重复的项 
df2 = df1.drop_duplicates(subset = ["city"])
df2['city'].to_csv("D:\\python_code\\sample\\猫眼\\city.csv")
# 将city.csv匹配好对应的省份保存为cityname.csv并写入dataframe
f = open("D:\\python_code\\sample\\猫眼\\cityname.csv",'rb')
citydata = pd.read_csv(f, names = ['city', 'province'])
# 初始化数据库连接，使用pymysql模块
engine = create_engine('mysql+pymysql://root:mym@1249690440@localhost:3306/maoyan')
# 将新建的DataFrame储存为MySQL中的数据表，储存index列
citydata.to_sql('cityname', engine, index=True)
df1.to_sql('moviecomment', engine, index=True)
print('Write to Mysql table successfully!')