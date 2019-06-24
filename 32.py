# 本脚本主要用于演示各种消息处理
# coding=utf8

import itchat
import os
from itchat.content import *


# 处理文本类消息,包括文本、位置、名片、通知、分享
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print('text_reply')
    print(msg)
    # 微信里的每个用户和群聊都是用ID来区分，msg['FromUserName']就是发送者的ID
    # 将消息的类型和文本内容返回给发送者
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])


# 处理多媒体消息，图片、语音、附件、视频
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    print('download_files')
    print(msg)
    filename = os.path.join("download_files/", msg['FileName'])
    # msg['Text']是一个下载函数，接受的参数为文件路径,目录不存在会抛出异常
    msg['Text'](filename)
    # 把文件回发给发送人
    return '@%s@%s' % ({"Picture": "img", "Video": 'vid'}.get(msg['Type'], ' fil'), filename)


# 处理好友添加请求，收到好友邀请自动添加好友
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    print('add_friend')
    print(msg)
    # 好友添加请求的msg['Text']是添加好友所需的参数
    itchat.add_friend(**msg['Text'])
    # 加完好友后发送一条问候信息
    itchat.send_msg("你好鸭！我们现在是盆友啦！", msg['RecommendInfo']['UserName'])


# 处理群聊消息，在注册时增加isGroupChat=True将判定为群聊回复
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    print('text_reply')
    print(msg)
    # IsAt=True说明该群聊消息是 @了自己
    if msg['IsAt']:
        # msg['ActualNickName'] 为发送人的昵称
        # msg['Content'] 为消息原文
        # msg['FromUserName'] 为发送人用户唯一标识
        itchat.send(u'@%s 消息已收到: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])


# 在auto_login里面传入一个True,即hotReload=True
# 既可保留登录状态，即使程序关闭，在一定时间内重新开启也可以不重新扫码
itchat.auto_login(True)
itchat.run()
