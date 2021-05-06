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
url = 'https://yun.kujiale.com/api/page/cloud/design/3FO4C643I467/show'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400',
# 'Cookie': 'PHPSESSID=qjpmm1uoe36bpsc2bn095nneq1'
}
data = {
    'site_id': 2
}


def main():
    response = requests.get(url, headers=headers, )
    # datas = json.loads(response.content.decode())
    content = response.content.decode()
    # parseDJson = json.dumps(content)
    # parseDJson = json.loads(content)
    reArr = re.findall(r'\\\"url\\\":\\\"(.*?)_%s', content)
    # print(type(parseDJson))
    # parseDJson['panoJson'] = json.loads(parseDJson['panoJson'])
    # data2 =  re.findall(r'rows(.*?)textarea', content)
    print(reArr)
    arr = ['up','down','left','right','front','back']

    for index,img_url in enumerate(reArr):
        dir_index = str(index)
        os.mkdir('./'+ dir_index)

        for key in arr:
            r = requests.get(img_url +'_'+ key[0:1])
            print(r.status_code)
            print(type(img_url))
            with open('./'+dir_index+'/'+key+'.jpg', 'wb') as f:
                f.write(r.content)


    # print(data2)
    # print(jsonpath.jsonpath(content, '$..brandLogo'))

# < textarea


# class ="form-control" style="height: 200px; overflow:hidden" rows="8" >




# < / textarea >
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
