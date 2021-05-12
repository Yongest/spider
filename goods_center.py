# coding=utf-8
# Version:Python 3.8.0
# Tools:PyCharm 2020.2 x64
__date__ = '2021/5/12 14:14'
__author__ = '张勇'
import requests
from lxml import etree
domain = 'https://www.jiazhuangpei.com'


def get(url):
    return requests.get(domain+url)


response = get('/to-kzz/search')

# while True:
# print(response.content.decode())
html = etree.HTML(response.content.decode())
print(response.content.decode())
node_list = html.xpath('//div[@class="all_de_clist"]/ul/li')

print(len(node_list))
for goods in node_list:

    link_detail = goods.xpath('./a[1]/@href')[0]  # 方案详情链接
    img_src_origin = goods.xpath('./a[1]/img/@data-src')[0]  # 方案原图链接
    vr_links_origin = goods.xpath('./div/div/div/a/@href')  # 方案vr原来的链接

    img_src = ''
    h3 = goods.xpath('./a[2]/div/h3/text()')[0].split(' | ')
    name = h3[0]  # 方案名称
    style = h3[1]  # 方案style
    price = goods.xpath('./a[2]/div/p[2]/span/text()')[0].split('￥')[1]  # 方案价格
    mark = goods.xpath('./a[2]/div/p[1]/span[1]/text()')[0]  # 方案标签

    detail_response = get(link_detail)
    print(detail_response.content.decode())
    break


def main():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
