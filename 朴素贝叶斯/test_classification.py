import os
import io
import jieba
import pandas as pd
from pandas import DataFrame
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

# 遍历文件夹中所有的文件
path1 = r'D:\python_code\sample\朴素贝叶斯\text_classification\train\女性'
path2 = r'D:\python_code\sample\朴素贝叶斯\text_classification\train\体育'
path3 = r'D:\python_code\sample\朴素贝叶斯\text_classification\train\文学'
path4 = r'D:\python_code\sample\朴素贝叶斯\text_classification\train\校园'
path5 = r'D:\python_code\sample\朴素贝叶斯\text_classification\test\女性'
path6 = r'D:\python_code\sample\朴素贝叶斯\text_classification\test\体育'
path7 = r'D:\python_code\sample\朴素贝叶斯\text_classification\test\文学'
path8 = r'D:\python_code\sample\朴素贝叶斯\text_classification\test\校园'
train = DataFrame(columns=('train_data','train_labels'))
test = DataFrame(columns=('test_data','test_labels'))
files1= os.listdir(path1)
for file in files1:
    f = open(path1 + '\\' + file, errors='ignore')
    d = f.read()
    f.close() 
    train = train.append(DataFrame({'train_data':[d],'train_labels':['女性']}))
files2= os.listdir(path2)
for file in files2:
    f = open(path2 + '\\' + file, errors='ignore')
    d = f.read()
    f.close() 
    train = train.append(DataFrame({'train_data':[d],'train_labels':['体育']}))
files3= os.listdir(path3)
for file in files3:
    f = open(path3 + '\\' + file, errors='ignore')
    d = f.read()
    f.close() 
    train = train.append(DataFrame({'train_data':[d],'train_labels':['文学']}))
files4= os.listdir(path4)
for file in files4:
    f = open(path4 + '\\' + file, errors='ignore')
    d = f.read()
    f.close() 
    train = train.append(DataFrame({'train_data':[d],'train_labels':['校园']}))
files5= os.listdir(path5)
for file in files5:
    f = open(path5 + '\\' + file, errors='ignore')
    d = f.read()
    f.close() 
    test = test.append(DataFrame({'test_data':[d],'test_labels':['女性']}))
files6= os.listdir(path6)
for file in files6:
    f = open(path6 + '\\' + file, errors='ignore')
    d = f.read()
    f.close() 
    test = test.append(DataFrame({'test_data':[d],'test_labels':['体育']}))
files7= os.listdir(path7)
for file in files7:
    f = open(path7 + '\\' + file, errors='ignore')
    d = f.read()
    f.close() 
    test = test.append(DataFrame({'test_data':[d],'test_labels':['文学']}))
files8= os.listdir(path8)
for file in files8:
    f = open(path8 + '\\' + file, errors='ignore')
    d = f.read()
    f.close() 
    test = test.append(DataFrame({'test_data':[d],'test_labels':['校园']}))
train_labels = train['train_labels']
test_labels = test['test_labels']
l = len(train)
m = len(test)
train_jieba = [] # 创建一个空的list 
test_jieba = []
for i in range(l):
    a = train.iloc[[i],[0]]
    words = jieba.cut(str(a)) ##x填写要分词的内容所在列数-1. str()：把括号中的对象变成一个字符串   content = " ".join(words)
    content = " ".join(words)
    # print(content)
    train_jieba.append(content)
for j in range(m):
    b = train.iloc[[j],[0]]
    words2 = jieba.cut(str(b)) 
    content2 = " ".join(words2)
    # print(content)
    test_jieba.append(content2)


stop_words = [line.strip() for line in io.open(r'D:\python_code\sample\朴素贝叶斯\text_classification\stop\stopword.txt', errors='ignore').readlines()]
# print(stop_words)
tfidf_vec = TfidfVectorizer()
tf = TfidfVectorizer(stop_words=stop_words, max_df = 0.5)
train_features = tf.fit_transform(train_jieba)    # 选出来的分词就是特征，计算这些特征在文档上的特征向量，得到特征空间features
# 多项式贝叶斯分类器
clf = MultinomialNB(alpha=0.001).fit(train_features, train_labels)
train_vocabulary = tf.vocabulary_
# 对测试集进行预测
test_tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5, vocabulary=train_vocabulary)
test_features = test_tf.fit_transform(test_jieba)
predicted_labels = clf.predict(test_features)
print(metrics.accuracy_score(test_labels, predicted_labels))