# coding=utf-8
# Version:Python 3.8.0
# Tools:PyCharm 2020.2 x64
__date__ = '2021/3/11 15:02'
__author__ = '张勇'

from lxml import etree
import requests

url = 'http://lookdiv.com/index/index/indexcodeindex.html'
agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'
headers = {
'User-Agent': agent,
'Cookie': ''
}
data = {
    'site_id': 2
}

data = {
        'key': 7788
}


def main():
    response = requests.get(url, headers=headers, )
    cookie = requests.utils.dict_from_cookiejar(response.cookies)
    print()
    headers2 = {
        'User-Agent': agent,
        'Cookie': 'PHPSESSID=' + cookie['PHPSESSID']
    }
    # 'PHPSESSID=' + cookie['PHPSESSID']
    # print(headers2)
    # print(requests.utils.dict_from_cookiejar(response.cookies))

    # print(headers2)

    requests.post('http://lookdiv.com/index/index/indexcode.html', headers=headers2, data=data)  #重定向
    response2 = requests.get(url, headers=headers2,)
    content2 = response2.content.decode()
    # print(content2)
    html = etree.HTML(content2)
    print(html.xpath("//textarea[@class='form-control']/text()")[0])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
