from itchat.content import *
import itchat


itchat.auto_login(True)


# 读取指定群聊的唯一标识和群聊名称
name_list = ['自己闹', '自己闹2']
groups = dict()
for room in itchat.get_chatrooms():
    if room['NickName'] in name_list:
        groups[room['UserName']] = room['NickName']


@itchat.msg_register([TEXT, SHARING], isGroupChat=True)
def group_reply_text(msg):
    """
    对群聊消息进行监听并同步到指定的群聊
    :param name:
    :return:
    """
    # 获取有新消息的群聊id
    source = msg['FromUserName']

    if msg['Type'] == TEXT:
        if source in groups.keys():
            for item in groups.keys():
                if source != item:
                    # group['source'] 发送消息的群聊名称
                    # msg['ActualNickName'] 发送消息的微信用户昵称
                    # msg['Content'] 消息内容
                    # item 接收消息的群聊id
                    itchat.send('%s: %s\n%s' % (groups[source], msg['ActualNickName'], msg['Content']), item)
    elif msg['Type'] == SHARING:
        # 处理分享消息
        if source in groups:
            for item in groups.keys():
                if item != source:
                    # msg['Text'] 分享文字
                    # msg['Url'] 分享地址
                    itchat.send('%s: %s\n %s\n%s' % (groups[source], msg['ActualNickName'], msg['Text'], msg['Url']),
                                item)


@itchat.msg_register([PICTURE, VIDEO], isGroupChat=True)
def group_reply_media(msg):
    """
    监听微信群聊中的多媒体信息并分发到其他群
    :param msg:
    :return:
    """
    source = msg['FromUserName']
    msg['Text'](msg['FileName'])
    if source in groups:
        for item in groups.keys():
            if item != source:
                itchat.send('@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName']),
                            item)


itchat.run()
