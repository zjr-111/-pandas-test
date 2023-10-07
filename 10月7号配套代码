import pandas as pd
import matplotlib.pyplot as plt
# 画图幕布分区
fig, ax = plt.subplots(nrows=2)
# 防止中文乱码
plt.rcParams['font.family'] = ['Noto Sans CJK JP']
# 导入文件
df = pd.read_csv('data.csv')
# 设置指标列为行索引
df.set_index('指标',inplace=True)

df = df[df.columns[::-1]]
# 将['居民消费水平','农村居民消费水平','城镇居民消费水平']转置并绘制折线图。
df.T[['居民消费水平','农村居民消费水平','城镇居民消费水平']].plot(ax=ax[0])
# 计算增长率并转置
df_pct = df.pct_change(axis=1).T
# 更改名称
df_pct.rename(columns={
  '居民消费水平':'居民消费水平增长率',
  '农村居民消费水平':'农村居民消费水平增长率',
  '城镇居民消费水平':'城镇居民消费水平增长率',
},inplace=True)
df_pct.plot(ax = ax[1])
plt.show()
