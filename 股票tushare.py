import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt

# 在本地环境运行时可以替换成自己的 token
MY_TOKEN = '0123456789shanbaycoding'
ts_pro = ts.pro_api(MY_TOKEN)

# 获取2020年上半年的第一个交易日的股票的基本信息
start_date = '20200102'
end_date = '20200630'
start_basic = ts_pro.daily_basic(trade_date = start_date)
# 获取2020年上半年的最后一个交易日的股票的基本信息
end_basic = ts_pro.daily_basic(trade_date = end_date)
# 获得股票的基本信息
stock_basic = ts_pro.stock_basic(trade_date =end_date)

# 选取在第一天交易股价不为零的股票
start_basic = start_basic.loc[start_basic['close'] > 0]

# 根据股票识别码，关联2020上半年初和末的股票信息
growth_basic = pd.merge(left=start_basic[['ts_code','close']], right=end_basic[['ts_code','close']],on='ts_code',how='left')

# 计算上半年度的增长值
growth_basic['growth_rate'] = (growth_basic['close_y'] - growth_basic['close_x'])/growth_basic['close_x']

# 根据增长率从高到底排序
growth_basic = growth_basic.sort_values(by = 'growth_rate',ascending=False)

# 关联股票的基本信息和当日交易量
enhanced_growth_basic = pd.merge(left=growth_basic,right=stock_basic,on='ts_code',how='left')
# 找到排第一的股票
ts_code = enhanced_growth_basic.iloc[0]['ts_code']
name = enhanced_growth_basic.iloc[0]['name']
print(ts_code)
print(name)

# 按周获取过去2020上半年的过票数据
hist_weekly = ts_pro.weekly(ts_code=ts_code,start_date=start_date,end_date=end_date)
hist_weekly = hist_weekly[['trade_date','close']]
# 绘制曲线
hist_weekly.sort_index(ascending=False).plot(x='trade_date',rot=30,grid=True)
plt.show()