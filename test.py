import pandas as pd
import random
# 读取文件
df = pd.read_excel(r'work.xlsx')
# 创建数字和文字相对应的字典
digit_dict={
    '1': '一',
    '2': '二',
    '3': '三',
}
# 定义改变数字的函数change_digit
def change_digit(list):
    result = []
    for i in list:
        num_str = str(i)
        chines_num = ''.join([digit_dict[digit] for digit in num_str])
        result.append(chines_num)
    return result
# 文件里的名字都是两个字的，可以进一步改善
df['姓名'] = df['姓名'].apply(lambda x: x[-2:])
# 检查文件的大概信息
# print(df.info)
# 随机生成年龄，这里可以改善为自动识别列的长度
age = [random.randint(18,70)for i in range(80)]
# 检查年龄列表
#print(age)
# 更新年龄列表
df['年龄'] = age
# 新增学历列，并给其赋值，判断是否列存在需要用到df.columns，df.columns用来获取DataFrame对象的列标签的属性
if '学历' not in df.columns:
    df['学历'] = ''
    df['学历'] = df['学历'].apply(lambda x: random.randint(1,3) if x is not None else None) # 这里需要先进行创建列，才能进行这一步的操作，lamba函数不支持赋值，但支持返回值
    df['学历'] = change_digit(df['学历'])
    df['学历'] = df['学历'].apply(lambda x: str(x)+'本')
#检查文档文件
print(df)
# 保存文件
df.to_excel(r'work.xlsx',index=False)
