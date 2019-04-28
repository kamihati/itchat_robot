# coding=utf8

import itchat


# 该装饰器把函数注册成了微信消息自动响应的方法
# 只处理消息类型为itchat.content.TEXT的消息，也就是文本内容（表情使用对应文本表示。例如太阳的文本是[太阳]）
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print("text_reply")
    # 消息为一个字典，包含了收发消息双方的一些公开的帐号信息
    print(msg)
    # 返回消息的文字部分，也就是把收到的文字消息原封不动发回去
    return msg['Text']


# 注册附件的下载方法
@itchat.msg_register(itchat.content.ATTACHMENT)
def download_file(msg):
    print("download_file")
    print(msg)
    # 这时候的msg['Text']是个下载方法,接受参数为附件保存的路径
    msg['Text'](msg['FileName'])


itchat.auto_login()

# 启动itchat自动回复模式
itchat.run()
