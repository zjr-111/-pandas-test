import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt

# plt.rcParams['font.family']=['Noto Sans CJK JP']
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取订单表格数据
df = pd.read_csv('https://media-zip1.baydn.com/storage_media_zip/srfeae/bf6dc7d814c520c60e5e632d281f14a4.ba163c25251bd44b74bde1bb4af7abdc.csv')
# 将订单日期转为日期格式
df['订单日期'] = pd.to_datetime(df['订单日期'])
# 计算 RFM
df_rfm = df.groupby('用户名').agg({
    '订单日期': lambda x: (pd.to_datetime('2019-12-31') - x.max()).days,  # 计算 R
    '用户名': lambda x: len(x),  # 计算 F
    '订单金额': lambda x: x.sum()  # 计算 M
})
# 列名重命名
df_rfm.rename(columns={'订单日期': 'R', '用户名': 'F', '订单金额': 'M'}, inplace=True)

def r_score(x):
  if x <= 29:
    return 4
  elif x <= 58:
    return 3
  elif x <= 119:
    return 2
  else:
    return 1

def f_score(x):
  if x <= 1:
    return 1
  elif x <= 2:
    return 2
  elif x <= 3:
    return 3
  else:
    return 4

def m_score(x):
  if x <= 204:
    return 1
  elif x <= 606:
    return 2
  elif x <= 1334:
    return 3
  else:
    return 4

df_rfm['r_score'] = df_rfm['R'].apply(r_score)
df_rfm['f_score'] = df_rfm['F'].apply(f_score)
df_rfm['m_score'] = df_rfm['M'].apply(m_score)

df_rfm['R高低'] = df_rfm['r_score'].apply(lambda x: '高' if x > df_rfm['r_score'].mean() else '低')
df_rfm['F高低'] = df_rfm['f_score'].apply(lambda x: '高' if x > df_rfm['f_score'].mean() else '低')
df_rfm['M高低'] = df_rfm['m_score'].apply(lambda x: '高' if x > df_rfm['m_score'].mean() else '低')

df_rfm['RFM'] = df_rfm['R高低'] + df_rfm['F高低'] + df_rfm['M高低']

def rfm_type(x):
  if x == '高高高':
    return '重要价值用户'
  elif x == '低高高':
    return '重要唤回用户'
  elif x == '高低高':
    return '重要深耕用户'
  elif x == '低低高':
    return '重要挽留用户'
  elif x == '高高低':
    return '潜力用户'
  elif x == '高低低':
    return '新用户'
  elif x == '低高低':
    return '一般维持用户'
  elif x == '低低低':
    return '流失用户'

# 给用户打标签
df_rfm['用户类型'] = df_rfm['RFM'].apply(rfm_type)
print(df_rfm)
# 获取每类用户消费金额
df_count = df_rfm.groupby('用户类型')['M'].sum().reset_index()
# 把列表的名字改一下
df_count.rename(columns={'M':'消费金额'}, inplace=True)
print(df_count)
# 画图
df_count.plot.bar(x='用户类型', y=['消费金额'])
plt.show()
