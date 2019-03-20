import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.metrics import zero_one_loss
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
# 设置 AdaBoost 迭代次数
n_estimators=200
# 使用make_hastie_10_2生成二分类数据
X,y=datasets.make_hastie_10_2(n_samples=12000,random_state=1)
# 从 12000 个数据中取前 2000 行作为测试集，其余作为训练集
test_x, test_y = X[2000:],y[2000:]
train_x, train_y = X[:2000],y[:2000]
# 弱分类器，max_depth：决策树最大深度，min_samples_leaf：叶子节点最少样本数
dt_stump = DecisionTreeClassifier(max_depth=1,min_samples_leaf=1)
dt_stump.fit(train_x, train_y)
dt_stump_err = 1.0 - dt_stump.score(test_x, test_y)
# 决策树分类器
dt = DecisionTreeClassifier()
dt.fit(train_x,  train_y)
dt_err = 1.0 - dt.score(test_x, test_y)
# AdaBoost 分类器，base_estimator：弱分类器，n_estimators：算法的最大迭代次数
ada = AdaBoostClassifier(base_estimator=dt_stump,n_estimators=n_estimators)
ada.fit(train_x,  train_y)
# 三个分类器的错误率可视化
fig = plt.figure()
# 设置 plt 正确显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
ax = fig.add_subplot(111) # 将画布分割成1行1列，图像画在从左到右从上到下的第1块
ax.plot([1,n_estimators],[dt_stump_err]*2, 'k-', label=u'决策树弱分类器 错误率') # 实线，将首尾两点相连
ax.plot([1,n_estimators],[dt_err]*2,'k--', label=u'决策树模型 错误率') # 虚线
ada_err = np.zeros(n_estimators)
# 遍历每次迭代的结果 i 为迭代次数, pred_y 为预测结果
for i,pred_y in enumerate(ada.staged_predict(test_x)):
    # 统计错误率
    ada_err[i]=zero_one_loss(pred_y, test_y)
# 绘制每次迭代的 AdaBoost 错误率 np.arange(n_estimators):n_estimators为终点，起点取默认值0，步长取默认值1
ax.plot(np.arange(n_estimators)+1, ada_err, label='AdaBoost Test 错误率', color='orange')
ax.set_xlabel('迭代次数')
ax.set_ylabel('错误率')
# loc：图例所有figure位置， If True, draw the frame with a round fancybox.
# 控制是否应在构成图例背景的FancyBboxPatch周围启用圆边
leg=ax.legend(loc='upper right',fancybox=True)
plt.show()
