import numpy as np

trial_uids = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/91b8b8a4df4f78b7ebae222cef306f9a.5a61749229d5f45c8a3336815ab0552c.csv')
paid_uids = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/8e25e9bffcce021c90335ec6900efb4b.28080b0032a0f39617346f4eead7f548.csv')

# 先将列表转为集合
trial_uids = set(trial_uids)
paid_uids = set(trial_uids)
# 求交集
paid_with_trial_uids = trial_uids & paid_uids
num_paid_with_trial_uids = len(paid_with_trial_uids)

print("有%d位用户先试读后再购书" % num_paid_with_trial_uids)
