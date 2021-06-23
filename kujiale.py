# coding=utf-8
# Version:Python 3.8.0
# Tools:PyCharm 2020.2 x64
'''
酷家乐爬虫项目
'''
__date__ = '2021/5/6 19:14'
__author__ = '张勇'

import os
import requests
import json
import jsonpath
import re
import time
url_lists = [
'https://yun.kujiale.com/api/page/cloud/design/3FO4C6F1084W/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C65V2TI3/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C951GRIE/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C94UTEHD/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C3BBRGS4/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C3BHIU9C/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C1AK10VL/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4BYYOSOY1/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C65J18V0/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C1RY9UJY/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C2IJUQMN/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C65RWYA8/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C643I467/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4CDLT1Y5R/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4CDGA2AX6/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C97VK014/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C68FA5RV/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C63HC5ML/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C19ETAAV/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C67YWUY7/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C0YF4SVE/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C3MRA0ND/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C3QMQ8TC/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C2P6KYG7/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C2QQVNY4/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C81AT3N4/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C66D4PRL/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C685UGRA/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C1SACWK1/show',
'https://yun.kujiale.com/api/page/cloud/design/3FO4C171YX5R/show',
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400',
    # 'Cookie': 'PHPSESSID=qjpmm1uoe36bpsc2bn095nneq1'
}
data = {
    'site_id': 2
}

arr = ['up', 'down', 'left', 'right', 'front', 'back']


def main():
    for myurl in url_lists:
        response = requests.get(myurl, headers=headers, )
        # datas = json.loads(response.content.decode())
        content = response.content.decode()
        # print(content)
        parseDJson = json.loads(content)
        name = jsonpath.jsonpath(parseDJson, '$..designName')[0]
        print(name)
        str_json = parseDJson['panoJson']
        str_json = json.loads(str_json)
        imgs_list = str_json['panoSnenes']
        print(type(imgs_list))
        for li in imgs_list:
            title = li['title']
            img_url = li['image']['cube']['url'][0:-2]
            time_str = str(time.time())
            dir_str = "C:\\Users\dxDev-ZHJ\Desktop\data\\" + time_str + name+'_' + title
            os.mkdir(dir_str)

            for key in arr:
                r = requests.get(img_url + key[0:1])
                print(r.status_code)
                print(type(img_url))
                with open(dir_str + '/' + key + '.jpg', 'wb') as f:
                    f.write(r.content)

        # reArr = re.findall(r'\\\"url\\\":\\\"(.*?)_%s', content)
        # print(type(parseDJson))
        # parseDJson['panoJson'] = json.loads(parseDJson['panoJson'])
        # data2 =  re.findall(r'rows(.*?)textarea', content)
        # print(reArr)

        # for index, img_url in enumerate(reArr):

        # print(data2)
        # print(jsonpath.jsonpath(content, '$..brandLogo'))


if __name__ == '__main__':
    main()
