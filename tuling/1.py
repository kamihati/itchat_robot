import requests
import urllib
from urllib import request
from urllib import parse
import json

KEY = '993f2b2bd823405a9d45cbb3d302aa7a'
url_v2 = 'http://openapi.tuling123.com/openapi/api/v2'
url_v1 = "http://www.tuling123.com/openapi/api"
req_info = '讲个笑话'.encode("utf8")

headers = {"Content-type": 'text/html', 'charset': 'utf-8'}


def make_data(text, user_id):
    """
    根据v2版api文档要求生成发送文字信息的请求数据
    具体参考v2版本api文档 https://www.kancloud.cn/turing/www-tuling123-com/718227
    :param text:
    :return:
    """
    return {
        "perception": {
            "inputText": {
                "text": text
            }
        },
        "userInfo": {
            "apiKey": KEY,
            "userId": user_id
        }
    }


def by_requests():
    """
    v2版本api（v2版本总是提示请求参数格式错误。未解决）
    使用requests发送请求
    :return:
    """
    query = make_data("讲个笑话", 'dream789')
    print(query)
    # v2版的api接口只接受post请求
    req = requests.post(url_v2, params=query, headers=headers)
    response = req.text
    print(response)
    data = json.loads(response)
    print(data['text'])


def by_urllib():
    """
    老版本api地址。可使用get请求
    使用urllib内置模块发送请求
    :return:
    """
    query = {"key": KEY, "info": req_info}
    # get请求需要urlencode成字符串格式，然后 数据必须为bytes类型所以要编码一下
    data = parse.urlencode(query).encode("utf-8")
    page = request.urlopen(url_v1, data)
    html = page.read()
    # 读到的响应结果为bytes类型。需要使用正确的编码解码为str
    html = html.decode("utf-8")
    data = json.loads(html)
    print(data)
    print("机器人说： " + data['text'])


def get_html(url, data):
    """
    根据请求地址和参数获取相应内容
    :param url: 请求地址
    :param data: 请求参数
    :return:
    """
    page = request.urlopen(url_v1, data)
    html = page.read()
    html = html.decode("utf-8")
    return html


if __name__ == "__main__":
    # by_urllib()
    while True:
        req_info = input("我(直接回车则退出): ")
        if not req_info:
            break
        query = {"key": KEY, 'info': req_info}
        data = parse.urlencode(query).encode('utf-8')
        response = get_html(url_v1, data)
        data = json.loads(response)
        print(data)
        print("机器人: " + data['text'])

