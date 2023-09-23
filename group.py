import pandas as pd
import matplotlib
from collections import Counter
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

df = pd.read_excel(r'C:\Users\17968\Desktop\pandas-test-main\work.xlsx')
# 分组
mean = df.groupby('学历')['薪资'].mean()
# 分别返回series对象的索引和值
bar_xlabel = mean.index
bar_ylabel = mean.values

age = df['学历'].reset_index(drop=True)

# 计数重复的次数
count = Counter(age)
# 将键为一个列表
keys_list = list(count.keys())
# 将值为一个列表
values_list = list(count.values())
# print(keys_list)
# print(values_list)

# 分片
ax1 = plt.subplot(2, 2, 1)
ax2 = plt.subplot(2, 2, 2)
# 柱状图
ax1.bar(bar_xlabel, bar_ylabel, width=0.3, color='red')
# 饼图
ax2.pie(values_list, labels=keys_list, autopct='%0.1f%%')
# 折线图
# plt.plot(x,y)
# 展示图像和图例
# loc参数有:
# best最佳位置 center居中
# upper right/left/center右/左/中上
# lower right/left/center右/左/中下
# center right/left左/右居中
plt.legend(loc='位置')
plt.show()
