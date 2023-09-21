import pandas as pd
df = pd.read_excel(r'C:\Users\zzz\Desktop\-pandas-test-main\work.xlsx')
# 函数groupby()可以根据括号内的标准，进行别的列的分组，
mean = df.groupby('学历')['薪资'].mean()
# mean = df.groupby('学历')[['薪资', '年龄']].mean()
print(mean)
