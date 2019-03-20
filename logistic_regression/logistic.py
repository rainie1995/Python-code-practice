# -*- coding:utf-8 -*-
# 使用逻辑回归对信用卡欺诈进行分类
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_recall_curve
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore') # 利用过滤器来实现忽略告警
 
# 混淆矩阵可视化
def plot_confusion_matrix(cm, classes, normalize = False, title = 'Confusion matrix"', cmap = plt.cm.Blues) :
    plt.figure()
    plt.imshow(cm, interpolation = 'nearest', cmap = cmap) # interpolation：设置了边界的模糊度，或者是图片的模糊度
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation = 0) # 第一个参数是你现在绘制的图的刻度点，第二个参数是标示的文字(省略为数字)
    plt.yticks(tick_marks, classes)
 
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])) :
        plt.text(j, i, cm[i, j],
            horizontalalignment = 'center',
            color = 'white' if cm[i, j] > thresh else 'black')
    # plt.text()表示设置文字说明，j,i表示坐标轴上的值，cm[i,j]表示说明文字，horizontalalignment表示水平对齐方式
    plt.tight_layout() # tight_layout会自动调整子图参数，使之填充整个图像区域
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
 
# 显示模型评估结果
def show_metrics():
    tp = cm[1,1]
    fn = cm[1,0]
    fp = cm[0,1]
    tn = cm[0,0]
    print('精确率: {:.3f}'.format(tp/(tp+fp)))
    print('召回率: {:.3f}'.format(tp/(tp+fn)))
    print('F1 值: {:.3f}'.format(2*(((tp/(tp+fp))*(tp/(tp+fn)))/((tp/(tp+fp))+(tp/(tp+fn))))))

# 绘制精确率 - 召回率曲线
def plot_precision_recall():
    # 绘制步阶图where有pre,post,mid三种取值，post指区间[x[i], x[i+1])值为y[i]，pre指区间(x[i-1], x[i]]值为y[i]
    plt.step(recall, precision, color = 'b', alpha = 0.2, where = 'post') 
    plt.fill_between(recall, precision, step ='post', alpha = 0.2, color = 'b') # 填充颜色，alpha:颜色的透明度
    plt.plot(recall, precision, linewidth=2) # linewidth：线宽
    plt.xlim([0.0,1]) # 设置坐标的上下限
    plt.ylim([0.0,1.05])
    plt.xlabel('召回率')
    plt.ylabel('精确率')
    plt.title('精确率 - 召回率 曲线')
    plt.show()
 
# 数据加载
data = pd.read_csv(r'D:\python_code\sample\logistic_regression\creditcard.csv')
# 数据探索
# print(data.describe())
# 设置 plt 正确显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制类别分布
plt.figure()
ax = sns.countplot(x = 'Class', data = data) # 计数图，是一种应用到分类变量的直方图，也可认为它是用以比较类别间计数差
plt.title('类别分布')
plt.show()
# 显示交易笔数，欺诈交易笔数
num = len(data)
num_fraud = len(data[data['Class']==1]) 
print('总交易笔数: ', num)
print('诈骗交易笔数：', num_fraud)
print('诈骗交易比例：{:.6f}'.format(num_fraud/num))
# 欺诈和正常交易可视化
f, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(15,8)) # 2行1个15*8大小的子图，所有子图使用相同的x轴刻度
bins = 50 # 区间数
ax1.hist(data.Time[data.Class == 1], bins = bins, color = 'deeppink')
ax1.set_title('诈骗交易')
ax2.hist(data.Time[data.Class == 0], bins = bins, color = 'deepskyblue')
ax2.set_title('正常交易')
plt.xlabel('时间')
plt.ylabel('交易次数')
plt.show()
# 对 Amount 进行数据规范化
data['Amount_Norm'] = StandardScaler().fit_transform(data['Amount'].values.reshape(-1,1))
# 特征选择
y = np.array(data.Class.tolist())
data = data.drop(['Time','Amount','Class'],axis=1)
X = np.array(data.as_matrix())
# 准备训练集和测试集
train_x, test_x, train_y, test_y = train_test_split (X, y, test_size = 0.1, random_state = 33)
 
# 逻辑回归分类
clf = LogisticRegression()
clf.fit(train_x, train_y)
predict_y = clf.predict(test_x)
# 预测样本的置信分数
score_y = clf.decision_function(test_x)  # decision_function中每一列的值代表距离各类别的距离
print("score_shape:", score_y.shape)
# 计算混淆矩阵，并显示
cm = confusion_matrix(test_y, predict_y)
class_names = [0,1]
# 显示混淆矩阵
plot_confusion_matrix(cm, classes = class_names, title = '逻辑回归 混淆矩阵')
# 显示模型评估分数
show_metrics()
# 计算精确率，召回率，阈值用于可视化
precision, recall, thresholds = precision_recall_curve(test_y, score_y)
# print("thresholds:", thresholds)
# print(thresholds.shape)
plot_precision_recall()