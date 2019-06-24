# 微信自动回复
# coding=utf8

import time
import itchat
from itchat.content import *


# 监听微信的文本消息
@itchat.msg_register("Text")
def text_reply(msg):
    # 当消息不是自己发出的，
    if not msg["FromUserName"] == myUserName:
        # 发送一条消息给文件助手
        itchat.send_msg("[%s]收到好友@%s 的信息: %s\n" % (
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                            msg['User']['NickName'],
                            msg['Text']),
                        'filehelper')

        # 回复给好友
        return '[自动回复]我现在不在,一会儿再和您联系。\n 已经收到您的信息：%s \n' % msg['Text']


if __name__ == "__main__":
    itchat.auto_login(True)
    # 获取自己的用户id
    myUserName = itchat.get_friends(update=True)[0]['UserName']
    itchat.run()
