import pandas as pd
df = pd.read_excel(r'work.xlsx')
# 函数groupby()可以根据括号内的标准，进行别的列的分组，
mean = df.groupby('学历')['薪资'].mean()
# mean = df.groupby('学历')[['薪资', '年龄']].mean()
print(mean)
# 查看总体信息
print(df.info())
# 查看平均值、最大值、最小值那一类的信息
print(df.describe())
# 删除所有包含NaN的行
# df.dropna()
# 参数inplace=True直接在原表格删除 格式：df.describe(inplace=True)
