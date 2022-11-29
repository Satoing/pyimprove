import matplotlib
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt
import pandas as pd

# 导入数据并对数据进行简单的统计分析
titanic = pd.read_csv('./data/train.csv')
print(titanic.head(2))  # 查看数据的格式
# 通过head可以看到包含的信息有：
# 社会阶层、姓名、性别、年龄、兄弟姐妹数、父母、船票、船舱、入口
print(titanic.info())  # 查看每一列数据的类型
print(titanic.describe())  # 查看大概的取值（平均数、中位数...)
print(titanic.isnull().sum())  # 统计空字段

# 处理空值，一般用中位数或特殊的0去填充（看情况）
# 取中位数比平均数好，可以减少极端数据的影响
titanic.Age.fillna(titanic.Age.median(), inplace=True)  # 不设置inplace会返回一个新的series
titanic.Fare.fillna(titanic.Fare.median(), inplace=True)
print(titanic.isnull().sum())

# 分析性别和生还的关系
# 目标：绘制柱状图，对比女性的生还率和男性的生还率（注意这里需要进行归一化）
survived = titanic[titanic.Survived==1].Sex.value_counts()  # 只需要统计的数量即可
dead = titanic[titanic.Survived==0].Sex.value_counts()
df = pd.DataFrame([survived, dead], index=['survived', 'dead'])
s_ratio = df.apply(lambda x: x.loc["survived"]/x.sum())  # 对每一列进行操作，计算生存率
d_ratio = df.apply(lambda x: x.loc["dead"]/x.sum())  # 计算死亡率
ratio = pd.DataFrame([s_ratio, d_ratio], index=['survived', 'dead']).T
ratio.plot.bar(stacked=True)
plt.legend(loc=9)
plt.show()
# 从上面绘制的图形可以看出生还与性别相关。

# 分析年龄对生还的影响
# 由于年龄很多，所以应该使用柱状图或密度图
survived = titanic[titanic.Survived==1].Age
dead = titanic[titanic.Survived==0].Age
df = pd.DataFrame([survived, dead], index=['survived', 'dead']).T
# df.plot.hist() 柱状图会产生遮盖，效果不是很好，所以选择密度图
print(df.describe())  # 查看年龄范围，确定横坐标的范围
df.plot.kde(xlim=(0, 80))
plt.show()
# 从上面绘制的图形可以看出0~10岁生还的可能性更大；20~30岁死亡的可能性更大，交点大约在16的位置

# 分析票价对生还的影响，与年龄类似
survived = titanic[titanic.Survived==1].Fare
dead = titanic[titanic.Survived==0].Fare
df = pd.DataFrame([survived, dead], index=['survived', 'dead']).T
# df.plot.hist() 柱状图会产生遮盖，效果不是很好，所以选择密度图
print(df.describe())  # 查看年龄范围，确定横坐标的范围
df.plot.kde(xlim=(0, 512))
plt.show()
# 可以看出低票价的生还率比较低

# 前面分析了一些比较重要的因素对生还率的影响，但是还是有一些隐含特征没考虑到
# 比如每个人都有一个称谓Mr、Miss(小姐)、Mrs(女士)...之前填充空值的时候应该考虑到这个，而不是取所有人的中位数
# 现在提取称谓，并加到dataFrame中，使用split和strip函数  [Braund, Mr. Owen Harris]
titanic['title'] = titanic.Name.apply(lambda name: name.split(',')[1].split('.')[0].strip())
print(titanic.title.value_counts())
# 实际上，有的没用到的列，也要考虑是否是隐含特征。
