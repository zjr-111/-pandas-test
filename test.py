import pandas as pd
df = pd.read_excel(r'C:\Users\\17968\Desktop\works.xlsx')
df['姓名'] = df['姓名'].apply(lambda x: x[-2:])
df.to_excel(r'C:\Users\\17968\Desktop\work.xlsx',index=False)