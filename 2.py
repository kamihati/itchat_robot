# coding=utf8

import itchat


# 生成二维码等待登录
# 有些微信账号会被官方禁止网页登录（原因未知）
itchat.auto_login()

# 登录成功后继续
# 把消息发送到扫码登录的微信号中的文件管理助手
itchat.send("这个有点意思", toUserName='filehelper')
