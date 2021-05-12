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
response = response.content.decode()
html = etree.HTML(response)

# print(html)
node_list = html.xpath('//div[@class="all_de_clist"]/ul/li')

print(len(node_list))
for goods in node_list:

    # name = goods.xpath('./a[1]/@href')[0]  # 产品名称
    thumb = goods.xpath('./a[1]/img/@data-src')[0]  # 缩略图
    print(thumb)
    break
    img_src = goods.xpath('./a[1]/@href')[0]  # 轮播图
    key = goods.xpath('./a[1]/@href')[0]  # url key 与方案关联
    code = goods.xpath('./a[1]/img/@data-src')[0]  # 编码，SKU(必填)
    size = goods.xpath('./a[1]/img/@data-src')[0]  # 规格
    brand = goods.xpath('./a[1]/img/@data-src')[0]  # 品牌
    style = goods.xpath('./a[1]/img/@data-src')[0]  # 风格
    material = goods.xpath('./a[1]/img/@data-src')[0]  # 材质
    color = goods.xpath('./a[1]/img/@data-src')[0]  # 颜色
    unit_price = goods.xpath('./a[1]/img/@data-src')[0]  # 单价(必填)
    unit = goods.xpath('./a[1]/img/@data-src')[0]  # 单位
    status_sale = goods.xpath('./a[1]/img/@data-src')[0]  # 销售状态(必填)
    sale_link = goods.xpath('./a[1]/img/@data-src')[0]  # 销售网址
    supplier = goods.xpath('./a[1]/img/@data-src')[0]  # 供应商
    area = goods.xpath('./a[1]/img/@data-src')[0]  # 区域
    cost_price = goods.xpath('./a[2]/div/div/p/span/text()')[0]  # 成本价
    params = goods.xpath('./a[1]/img/@data-src')[0]  # 参数
    service = goods.xpath('./a[1]/img/@data-src')[0]  # 服务
    model = goods.xpath('./a[1]/img/@data-src')[0]  # 型号
    goods_class = goods.xpath('./a[1]/img/@data-src')[0]  # 分类
    detail = goods.xpath('./a[1]/img/@data-src')[0]  # 详情


    # print(detail_response.content.decode())



def main():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
