# 统计微信好友男女比例
# coding=utf8

import itchat
import numpy as ny
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


itchat.login()
# 获取好友列表
friends = itchat.get_friends(update=True)

# 初始化计数器，有男有女，也有未填写性别的
male = female = other = 0

print("自己的用户是好友列表第一个")
print(friends[0])

for i in friends[1:]:
    # 1为男，2为女
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1


# 计算好友总数
total = len(friends[1:])

# 打印好友性别比例
male_persent = (float(male) / total * 100)
female_persent = (float(female) / total * 100)
other_persend = (float(other) / total * 100)
print("男性好友: %.2f%%" % male_persent + "\n"
      + "女性好友: %.2f%%" % female_persent + "\n"
      + "不明性别好友: %.2f%%" % other_persend)

# 根据数据做出百分比圆饼图
labels = ['男', '女', '未知']
x = [male, female, other]
fig = plt.figure()

# 步骤一（替换sans-serif字体）
plt.rcParams['font.sans-serif'] = ['SimHei']
# 步骤二（解决坐标轴负数的负号显示问题），一般为步骤一引起
plt.rcParams['axes.unicode_minus'] = False

plt.pie(x, labels=labels, autopct='%1.2f%%')
plt.title('圆饼图')
plt.show()
plt.savefig("PieChart.png")
