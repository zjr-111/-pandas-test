import pandas as pd
df = pd.read_excel(r'C:\Users\zzz\Desktop\-pandas-test-main\work.xlsx')
mean = df.groupby('学历')['薪资'].mean()
# mean = df.groupby('学历')[['薪资', '年龄']].mean()
print(mean)