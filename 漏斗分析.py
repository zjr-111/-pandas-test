import numpy as np
import matplotlib.pyplot as plt

# active_uids活跃用户的ID; enterbook_uids进入书籍页面的ID; trial_uids试读用户的ID; paid_uids购书用户的ID
active_uids = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/22f0e6eaefcfb277176d59e8125cf505.f75f6a24bf8052409e4a0ca5b52c951a.csv')
enterbook_uids = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/aa3af5c54faea4567e02056fb96f0d09.d6312693cb816c2454eba79e46d9ba8c.csv')
trial_uids = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/91b8b8a4df4f78b7ebae222cef306f9a.5a61749229d5f45c8a3336815ab0552c.csv')
paid_uids = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/8e25e9bffcce021c90335ec6900efb4b.28080b0032a0f39617346f4eead7f548.csv')

active = set(active_uids)
enterbook = set(enterbook_uids)
trial = set(trial_uids)
paid = set(paid_uids)

# 请补充代码
enterbook_num = len(enterbook_uids)
trial_num = len(trial_uids)
trial_with_pay = trial & paid
trial_with_pay_num = len(trial_with_pay)
paid_num = len(paid_uids)
trial_without_pay = paid - trial_with_pay
trial_without_pay_num = len(trial_without_pay)

# 绘制总体数量的柱形图
x = ['enterbook', 'trial_or_pay', 'trial_then_pay']
y_1 = [enterbook_num, 0, 0]
y_2 = [0, trial_num, trial_with_pay_num]
y_3 = [0, trial_without_pay_num, 0]
# 画图
plt.bar(x, y_1)
plt.bar(x, y_2, label = 'trial')
plt.bar(x, y_3, label = 'trial_without_pay')
plt.legend()
plt.show()
