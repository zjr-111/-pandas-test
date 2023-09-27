import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://media-zip1.baydn.com/storage_media_zip/qkklny/cdef8ac11cea09425c9a5ca1327b6b90.78492cd0c25f0a9a5de36b7534893657.csv')
print(df.head(5))
plt.hist(df['time_stay'], bins=10, facecolor="blue", edgecolor="black", alpha=0.7)
# 设置横轴标签
plt.xlabel("Time Staying")
# 设置纵轴标签
plt.ylabel("Number of Users")
plt.show()

# 根据直方图判断标准
threshold = 50
# 阅读时间50s以下及以上的人
under_50 = df[df['time_stay'] <= threshold]
above_50 = df[df['time_stay'] > threshold]
num_under_50 = len(under_50)
num_above_50 = len(above_50)

# 点击下一页的人数
next_under_50 = under_50[df['next_page']]
next_above_50 = above_50[df['next_page']]
num_next_under_50 = len(next_under_50)
num_next_above_50 = len(next_above_50)
# 下一页占比
ratio_under_next = num_next_under_50 / num_under_50
ratio_above_next = num_next_above_50 / num_above_50

# 购买的人数
pay_under_50 = under_50[df['pay']]
pay_above_50 = above_50[df['pay']]
num_pay_under_50 = len(pay_under_50)
num_pay_above_50 = len(pay_above_50)
# 购买占比
ratio_under_pay = num_pay_under_50 / num_under_50
ratio_above_pay = num_pay_above_50 / num_above_50

print("阅读时间在%d秒及以下，总人数为%d, 点击下一页的人数为%d，比例为%0.1f%%" % (threshold, num_under_50, num_next_under_50, 100*ratio_under_next))
print("阅读时间在%d秒以上，总人数为%d, 点击下一页的人数为%d，比例为%.0f%%" % (threshold, num_above_50, num_next_above_50, 100*ratio_above_next))
print('----------------------------------------------------------------------------')
print("阅读时间在%d秒及以下，总人数为%d, 购买的人数为%d，比例为%.0f%%" % (threshold, num_under_50, num_pay_under_50, 100*ratio_under_pay))
print("阅读时间在%d秒以上，总人数为%d, 购买的人数为%d，比例为%.0f%%" % (threshold, num_above_50, num_pay_above_50, 100*ratio_above_pay))
