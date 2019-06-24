# 统计微信好友的所在省份信息到Excel
# coding=utf8
import itchat
from pandas import DataFrame


itchat.login()
# 获取好友列表
friends = itchat.get_friends(update=True)

# 初始化计数器，有男有女，也有未填写性别的
male = female = other = 0

print("自己的用户是好友列表第一个")
print(friends[0])


def get_var(var):
    """
    获取微信好友列表中每个好友指定属性并写入新列表
    :param var:
    :return:
    """
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable


nickName = get_var("NickName")
sex = get_var('Sex')
province = get_var("Province")
city = get_var("City")
signature = get_var("Signature")

data = {"NickName": nickName,
        "Sex": sex,
        "Province": province,
        "City": city,
        "Signature": signature}

print(data)

frame = DataFrame(data)
# 保存后的文件为utf8编码，可用记事本打开，但excel打开中文会显示乱码，用记事本另存为ANSI编码的文件既可正常
frame.to_csv("data.csv", index=True)
