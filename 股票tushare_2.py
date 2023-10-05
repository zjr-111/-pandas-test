import tushare as ts
import matplotlib.pyplot as plt
from scipy.stats import skew

# 在本地环境运行时可以替换成自己的 token
MY_TOKEN = '0123456789shanbaycoding'
ts_pro = ts.pro_api(MY_TOKEN)

# 解决图表中文乱码
plt.rcParams['font.family'] = ['Noto Sans CJK JP']

# 按天获取 2019 年上半年万集股票的数据
wanji_data = ts_pro.daily_basic(ts_code='300552.SZ', start_date='20190102', end_date='2019631')
# 按天获取 2019 年上半年茅台股票的数据
maotai_data = ts_pro.daily_basic(ts_code='600519.SH', start_date='20190102', end_date='2019631')

# 按时间排序
wanji_data = wanji_data.sort_index(ascending=False)
maotai_data = maotai_data.sort_index(ascending=False)

# 输入你的代码
wanji_returns = wanji_data['close'].pct_change()
wanji_returns = wanji_returns.dropna()
maotai_returns = maotai_data['close'].pct_change()
maotai_returns = maotai_returns.dropna()

# 计算收益率日平均值
mean_wanji_returns = wanji_returns.mean()
mean_maotai_returns = maotai_returns.mean()

# 计算收益率标准差
std_wanji_returns = wanji_returns.std()
std_maotai_returns = maotai_returns.std()

# 计算收益率偏度
skew_wanji_returns = skew(wanji_returns)
skew_maotai_returns = skew(maotai_returns)

# 绘制万集科技收益率的分布直方图
plt.hist(wanji_returns, bins=75, label='万集科技')

# 绘制茅台收益率的分布直方图
plt.hist(maotai_returns, bins=75, label='茅台')

# 将计算的值输出
print('万集科技的日平均收益率为%f',mean_wanji_returns)
print('万集科技的收益率标准差为%f',std_wanji_returns)
print('万集科技的收益率偏度为%f',skew_wanji_returns)
print('茅台的日平均收益率为%f',mean_maotai_returns)
print('茅台的收益率标准差为%f',std_maotai_returns)
print('茅台的收益率偏度为%f',skew_maotai_returns)

plt.legend(loc='best')
plt.show()
