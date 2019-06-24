# 红包提醒
import itchat
from itchat.content import *


# 监听群内提醒NOTE
@itchat.msg_register(NOTE, isGroupChat=True)
def receive_red_packet(msg):
    if '收到红包' in msg['Content']:
        groups = itchat.get_chatrooms(update=True)
        # 把红包消息通知给这个群
        users = itchat.search_chatrooms(name='自己闹')
        # 获取这个群的唯一标识id
        userName = users[0]['UserName']
        for g in groups:
            if msg['FromUserName'] == g['UserName']:
                # 根据群消息的FromUserName匹配是哪个群
                group_name = g['NickName']
        msgbody = '有人在群"%s"发了红包， 请立即打电话给我，让我去抢' % group_name
        # 提醒自己有人在群里发红包
        itchat.send(msgbody, toUserName=myUserName)
        # 把红包消息通知给'自己闹'群,与对指定用户发送消息一样,证明群聊对象和用户对象类似
        itchat.send(msgbody, toUserName=userName)


itchat.auto_login(True)
myUserName = itchat.get_friends(update=True)[0]['UserName']
itchat.run()
