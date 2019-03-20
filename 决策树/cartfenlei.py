from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from sklearn.datasets import load_iris
from sklearn.externals.six import StringIO
import pydotplus
dot_data = StringIO() # StringIO:在内存中以 io 流的方式读写str,IO流代表了数据的无结构化传递
# 准备数据集iris
iris=load_iris()
# 获取特征集和分类标识
features = iris.data
labels = iris.target
# 随机抽取 33% 的数据作为测试集，其余为训练集
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=0)
clf = DecisionTreeClassifier(criterion='gini') # 初始化 CART 分类树
clf = clf.fit(train_features, train_labels) # 拟合构造 CART 分类树
export_graphviz(clf, out_file=dot_data) # 将树导出为graphviz格式，写入dot_data
# dot_data.getvalue()：返回对象dot_data中的所有数据
graph = pydotplus.graph_from_dot_data(dot_data.getvalue()) # graph_from_dot_data():转换为DOT格式
graph.write_pdf("iris.pdf") # 用pydotplus生成iris.pdf
# 用 CART 分类树做预测
test_predict = clf.predict(test_features)
# 预测结果与测试集结果作比对
score = accuracy_score(test_labels, test_predict)
print("CART 分类树准确率 %.4lf" % score)
