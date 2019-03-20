import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_digits
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
digits = load_digits()
data = digits['data']
# 创建 SVM 分类器
svm = svm.SVC()
train_x, test_x, train_y, test_y = train_test_split(data, digits['target'], test_size=0.25, random_state=33)
ss = preprocessing.StandardScaler()
train_ss_x = ss.fit_transform(train_x)
test_ss_x = ss.transform(test_x)
svm.fit(train_ss_x, train_y)
predict_y=svm.predict(test_ss_x)
print('SVM 准确率: %0.4lf' % accuracy_score(predict_y, test_y))
# 采用 Min-Max 规范化
mm = preprocessing.MinMaxScaler()
train_mm_x = mm.fit_transform(train_x)
test_mm_x = mm.transform(test_x)
# 创建 Naive Bayes 分类器
mnb = MultinomialNB()
mnb.fit(train_ss_x, train_y) 
predict_y = mnb.predict(test_ss_x) 
print(" 多项式朴素贝叶斯准确率: %.4lf" % accuracy_score(predict_y, test_y))
# 创建 CART 决策树分类器
dtc = DecisionTreeClassifier()
dtc.fit(train_ss_x, train_y) 
predict_y = dtc.predict(test_ss_x) 
print("CART 决策树准确率: %.4lf" % accuracy_score(predict_y, test_y))