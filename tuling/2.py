from itchat.content import *
import requests
import json
import itchat


itchat.auto_login()


def tuling(info):
    """
    吧消息发送给图灵机器人并接受机器人的回复
    :param info:
    :return:
    """
    appkey = 'xxxxx'
    url_v1 = 'http://www.tuling123.com/openapi/api?key=%s&info=%s' % (appkey, info)
    req = requests.get(url_v1)
    content = req.text
    data = json.loads(content)
    answer = data['text']
    return answer


def group_id(name):
    """
    获取指定群聊名称对应的唯一标识
    :param name:
    :return:
    """
    df = itchat.search_chatrooms(name=name)
    return df[0]['UserName']


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    """
    监听微信好友发来的文本类型信息,并把图灵机器人的返回消息返回给发送人
    :param msg:
    :return:
    """
    itchat.send(tuling(msg['Text']), msg['FromUserName'])


@itchat.msg_register([PICTURE, VIDEO, RECORDING, ATTACHMENT])
def download_files(msg):
    """
    监听多媒体类微信消息。把文件下载到本地。然后返回给发送人
    :param msg:
    :return:
    """
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])


@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
    """
    监听群消息。只对指定群的消息进行回复
    :param msg:
    :return:
    """
    item = group_id('自己闹')
    if msg['FromUserName'] == item:
        itchat.send(tuling(msg['Text']), item)


itchat.run()
