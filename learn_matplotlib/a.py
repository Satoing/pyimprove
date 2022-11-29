import numpy as np
import matplotlib
# 配置后端（绘图使用的渲染器，tkinter是python自带的，无需安装其他库）
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt
import pandas as pd

# 绘图的一般步骤
## 生成两个numpy的一维数组
x = np.linspace(0, 2*np.pi, 40)
y = np.sin(x)
## 使用plot绘制图像，在show之前可以叠加
fig = plt.figure()  # figure代表接下来绘制的对象
plt.plot(x, y, 'y--')  # 可以修改图像的样式，类似于matlab
plt.plot(x, np.cos(x))  # 两个图像叠加
fig.savefig('./figure.png')  # 使用figure导出图像
plt.show()

# 使用子图，在一个窗口绘制多个图像
plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x))
## 2,1代表两行一列
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))
plt.show()

# 给图像添加修饰
plt.plot(x, np.sin(x), label='sin(x)')  # label表示图像的标签
plt.plot(x, np.cos(x), '--', label="cos(x)")
plt.legend(loc=1)  # legend表示显示标签，loc标签用于定义标签的位置
plt.show()

plt.ylim(-2, 2)  # 限定坐标范围
plt.xlim(-2, 6)
plt.plot(x, np.cos(x), '--', linewidth=4)  # 定义线的宽度
t = np.linspace(0, 2*np.pi, 8)
plt.plot(t, np.cos(t), 'r^', markersize=10)  # 定义点的大小
plt.show()

# scatter专门绘制散点图
plt.scatter(x, np.cos(x), s=10, c='blue')
plt.show()

## 为每个点设置颜色，大小
x = np.random.randn(100)  # 标准正态分布
y = np.random.randn(100)
colors = np.random.rand(100)
sizes = 100*np.random.rand(100)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.4)
plt.colorbar()  # 生成colorbar
plt.show()

# pandas自带绘图
## 绘制线性图，反映的是每一列的变化趋势
df = pd.DataFrame(np.random.rand(100, 4).cumsum(0), columns=['A', 'B', 'C', 'D'])
df.plot()  # 使用numpy生成dataFrame，四列，依次累加，所以绘制出的图像应该是递增的
plt.show()  # 最后还是要调用plt的show函数，可见这三个库之间的关联之密切
df.A.plot()  # 单独绘制一列
plt.show()
## 绘制柱状图，反映的是每一行数据的比较
df = pd.DataFrame(np.random.randint(1, 4, size=(3, 4)), index=['one', 'two', 'three'], columns=['A', 'B', 'C', 'D'])
df.plot.bar()  # 列名用于标注颜色，index用于标注每一行显示的名称（可以理解为什么很多时候index不是0开始的数字）
plt.show()
## 绘制直方图，用于统计每一列一定范围的值的个数
df = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])
df.hist()  # 每一列一个直方图，看起来应该是标准正态分布
plt.show()