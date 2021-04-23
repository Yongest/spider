# coding=utf-8
# Version:Python 3.8.0
# Tools:PyCharm 2020.2 x64
__date__ = '2021/3/4 15:51'
__author__ = '张勇'

import requests

url = 'http://www.baidu.com'
headers = {

}


def main():
    response = requests.get(url, headers=headers)
    print(response.content.decode())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

