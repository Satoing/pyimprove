# python中数组和列表的区别是数组中元素的类型必须相同
import array
a = array.array('i', range(10))  # 'i'表示数组元素的类型为int
print(a[9])  # 通过下标访问元素
# 报错，只能赋值为int型：a[0] = 'test'
a[0] = 11
print(a)

# python自带的数组一起来很繁琐，常常直接用numpy封装的数组
import numpy as np

# numpy数组的创建
a = list(range(10))
b = np.array(a)  # 将列表转换为数组
print(b)
print(np.array(['1', 1, 1.0, "test", True]))  # 如果列表中的元素类型不同，则会都转换为字符串
print(type(b))  # numpy中数组的类型为numpy.ndarray

# numpy生成数组的方法
## np.zeros()、np.ones()。np.eye()生成特殊元素的矩阵
a = np.zeros(10, dtype=int)  # dtype指定元素类型，默认为float64
print(type(a))
print(a)  # a的shape为一维，10个元素
print(np.zeros((2, 3)))  # 最里层3个元素

## np.full()指定其中的元素
print(np.full((2, 3), 11.4, dtype=float))

## 使用_like传入ndarray可以生成形状相同的新ndarray
print(np.ones_like(a))  # 默认两个ndarray的dtype也是相等的，可以传入修改

# 随机数
# np.random相当于python中radom的加强，即可以生成多维的随机数组
print(np.random.random((2, 4)))  # 生成2*4的0~1之间的ndarray
print(np.random.randint(1, 10, (2, 4)))  # 需要传入低位与高位，左闭右开

# 范围取值
print(np.arange(1, 9, 2))  # 类似于range()
print(np.linspace(0, 3, 100))  # start到end之间分为num份

# dtype
## 使用引号指定类型，如果越界则会溢出
print(np.full(10, 128, dtype='int8'))
## int8、int16、int32、int64（默认的int可能为32，也可能为64，所以最好显示指定）
## uint8、uint16、uint32、uint64
## float16、float32、float64（默认的float为float64）

# 访问元素
a = np.array([[1, 2, 3], [4, 5, 6]], dtype='int8')
print(a[0][2])  # 和列表的访问方式相同
print(a[-1][-2])  # 也可以使用python的负下标访问
print(a[0, 2])  # 也可以这样访问

# 数组运算
