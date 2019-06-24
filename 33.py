# 本脚本主要用于演示各种用户信息获取方式
# coding=utf8

import itchat
from itchat.content import *


# 处理文本类消息,包括文本、位置、名片、通知、分享
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print('text_reply')
    print(msg)
    # 微信里的每个用户和群聊都是用ID来区分，msg['FromUserName']就是发送者的ID
    # 将消息的类型和文本内容返回给发送者
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

    # 接收到的消息
    msg_text = msg['Text']
    # 发送人用户id
    fromUserName = msg['FromUserName']
    # 发送人昵称
    fromUserNickName = msg['User']['NickName']

    if msg_text == "1":
        print("下面显示自己的用户信息")
        print(itchat.search_friends())
    elif msg_text == "2":
        print("获取指定UserName即用户ID的用户信息,获取到的是一个字典")
        print(itchat.search_friends(userName=fromUserName))
    elif msg_text == "3":
        print("获取备注、微信号、昵称任何一项等于name值的用户列表")
        user_list = itchat.search_friends(name=fromUserNickName)
        print(user_list)
    elif msg_text == "4":
        print("获取微信号等于对应值的用户列表")
        # 此处使用微信号获取不到数据。原因未知
        result = itchat.search_friends(wechatAccount='gnagnem1')
        print(result)
    elif msg_text == "5":
        print("结合以上两种得到的用户列表")
        # 此处使用微信号获取不到数据。原因未知
        user_list = itchat.search_friends(name=fromUserNickName, wechatAccount='gnagnem1')
        print(user_list)
    elif msg_text == "6":
        print("获取指定公众号信息")
        # 此处指定的userName为公众号AI前线的唯一标识
        print(itchat.search_mps(userName='@4e1d4f00a43db3deff4672fea6d313e0'))
        print("获取名字中含有特定字符的公众号，即模糊搜索。返回一个用户列表")
        print(itchat.search_mps(name='空白女侠'))
        print("两项都做了指定则仅返回指定UserName的公众号。相当于仅指定了userName参数")
        print(itchat.search_mps(userName='@4e1d4f00a43db3deff4672fea6d313e0', name='鼠绘译制组'))
    elif msg_text == '7':
        print("获取自己所有群聊列表")
        room_list = itchat.get_chatrooms()
        print("共%s个群聊" % len(room_list))
        print("群聊列表对象的键名")
        print(room_list[0].keys())
        if len(room_list) > 0:
            print("获取指定userName的群聊信息")
            room_list = itchat.search_chatrooms(userName=room_list[-1]['UserName'])
            print(room_list)
            print("指定群聊名称模糊搜索(未搜索到数据。原因未知)")
            # 若同时指定userName和name会忽略name
            room_list = itchat.search_chatrooms(name='创恒就业')
            print(room_list)
            print("获取指定群聊的用户列表")
            memberList = itchat.update_chatroom(room_list[-1]['UserName'])
            print(len(memberList))

    elif msg_text == "8":
        # 创建群聊和增加删除群聊用户（此类方法被严格限制了使用频率。删除群聊需要本账号为群管理员。否则失败）
        # 获取好友字典列表
        friend_list = itchat.get_friends()
        print(friend_list)
        # print("创建群聊")
        # wechatRoomUserName = itchat.create_chatroom(friend_list[1:], '测试群聊')
        # print("新创建的群聊userName为", wechatRoomUserName)
        # print("删除群聊中的指定用户,需为管理员")
        # itchat.delete_member_from_chatroom(wechatRoomUserName, friend_list[1])
        # print("增加指定用户进入群聊")
        # itchat.add_member_into_chatroom(wechatRoomUserName, friend_list[0])







# 在auto_login里面传入一个True,即hotReload=True
# 既可保留登录状态，即使程序关闭，在一定时间内重新开启也可以不重新扫码
itchat.auto_login(True)
itchat.run()
