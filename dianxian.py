# coding=utf-8
# Version:Python 3.8.0
# Tools:PyCharm 2020.2 x64
__date__ = '2021/5/6 19:14'
__author__ = '张勇'

import os
import requests
import json
import jsonpath
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400',
    # 'Cookie': 'PHPSESSID=qjpmm1uoe36bpsc2bn095nneq1'
}
data = {
    "username": "M0005757",
    "password": "e10adc3949ba59abbe56e057f20f883e"
}


session = requests.session() # 实例化session对象


def main():
    login_response = session.post('https://demo37.gzdianxian.com/design//login/member_login', data)

    # datas = json.loads(response.content.decode())
    login_content = json.loads(login_response.content.decode())

    if login_content['status'] == 2000:
        response = session.get('https://demo37.gzdianxian.com/design//plan/pagePlanList')
        content = response.content.decode()
        print(content)


if __name__ == '__main__':
    main()
