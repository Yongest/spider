# coding=utf-8
# Version:Python 3.8.0
# Tools:PyCharm 2020.2 x64
__date__ = '2021/3/4 17:14'
__author__ = '张勇'

import requests
import json
import jsonpath
import re
url = 'http://www.lookdiv.com/index/index/indexcodeindex.html'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400',
'Cookie': 'PHPSESSID=qjpmm1uoe36bpsc2bn095nneq1'
}
data = {
    'site_id': 2
}


def main():
   response = requests.get(url, headers=headers, )
   # datas = json.loads(response.content.decode())
   content = response.content.decode()
   print(content)
   data2 =  re.findall(r'rows(.*?)textarea', content)

   print(data2)
   # print(jsonpath.jsonpath(datas, '$..name'))

# < textarea


# class ="form-control" style="height: 200px; overflow:hidden" rows="8" >




# < / textarea >
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
