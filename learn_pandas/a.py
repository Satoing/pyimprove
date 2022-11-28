import pandas as pd

std = pd.read_csv('./student.csv')  # 读取csv文件
print(std.head(10))  # 使用head查看前n行
print(type(std))  # std的类型是dataFrame，是pandas的核心

# dataFrame的创建，可以直接向pd.dataFrame传入字典，字典的值为列表
scores = {
  "姓名": ["小唐", "小王", "小李"],
  "语文": [70, 80, 90], 
  "数学": [100, 90, 80]
}
df = pd.DataFrame(scores, index=['one', 'two', 'three'])  # 自定义索引
print(df)

# dataFrame的操作
print(std.columns)  # 获取列名
print(std.学号)  # 根据列名访问数据
print(std[["数学", "语文"]].head())  # 访问多列的数据
print(std.index)  # 获取索引范围
print(std.loc[0])  # 根据索引获取行
print(std.loc[2:4])  # 范围索引，亦可以省略一边
print(std[2:4])  # 和前面的范围访问的区别是前者右边的索引也能取到，而这个是左闭右开
# 访问单行数据不能直接取下标：print(std[0])

## 筛选
print(std.语文 > 80)  # 一串bool，结果类似于numpy结果的大小
print(type(std.语文>80))  # 类型是series
print(std[std.语文 > 80])  # 可以在外面再套一层dataFrame来获得具体的列

## 排序
print(std.sort_values(["数学", "语文"]))  # 先按数学排序，数学相等的再按语文排序

## 统计
print(std.数学.value_counts())  # 对每个值的个数进行统计
def grade(score):
  if score >= 85: return "优秀"
  elif score >= 70: return "良好"
  elif score >= 60: return "及格"
  else: return "不及格"
# map方法非常重要，它的作用是根据一列生成新列
std["数学等级"] = std.数学.map(grade)  # map将每一行对应的值传入函数
print(std)  # 增加数学的等级
print(df.applymap(lambda x: str(x)+'-'))  # 对所有元素进行操作
# 类似的函数还有apply，它的作用是根据多列生成新列
std['理综'] = std.apply(lambda x: x.物理+x.化学+x.生物, axis=0)
print(std.head())