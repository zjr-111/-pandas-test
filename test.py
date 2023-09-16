import pandas as pd
import random
# 读取文件，最开始读取的文件是works.xlsx文件,更改名字。
df = pd.read_excel(r'C:\Users\\17968\Desktop\work.xlsx')
# 文件里的名字都是两个字的，需要进一步改善
df['姓名'] = df['姓名'].apply(lambda x: x[-2:])
# 检查文件的大概信息
print(df.info)
# 随机生成年龄
age = [random.randint(18,70)for i in range(81)]
# 检查年龄列表
print(age)
# 更新年龄列表
df['年龄'] = age
#检查文档文件
print(df)
# 保存文件
df.to_excel(r'C:\Users\\17968\Desktop\work.xlsx',index=False)
