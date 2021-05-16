# coding=utf-8
# Version:Python 3.8.0
# Tools:PyCharm 2020.2 x64
__date__ = '2021/5/12 14:14'
__author__ = '张勇'
import requests
import re
import json
import time

from lxml import etree
domain = 'https://www.jiazhuangpei.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400',
    'Cookie': 'PHPSESSID=dd8f7f1bdcf0c216a4fee0f82d3435f7; SERVERID=44eaeffc8bad2a92fe4cdc77619b902d|1621175211|1621175'
}
# 94 60
# 92 20
# 2  30

def get(url):
    return requests.get(domain+url,headers=headers,timeout=30)


index0 = 3


while True:
    err_link = []
    jsonfile = open('./data/new_goods_' + str(index0) + '.json', 'w', encoding='utf-8')
    step_arr = []
    response = get('/to-kzz/search?ob=default&page='+str(index0)+'#page_anchor')
    print('页开始第几页：',index0)
    # while True:
    response = response.content.decode()
    html = etree.HTML(response)

    # print(html)
    node_list = html.xpath('//div[@class="all_de_clist"]/ul/li')
    for goods_index,goods in enumerate(node_list):

        print('正在爬第',index0,'页',goods_index+1,'条开始爬取',)
        obj = {}
        obj["thumb"] = goods.xpath('./a[1]/img/@data-src')[0]  # 缩略图
        obj["key"] = goods.xpath('./a[1]/@href')[0].split('/to-kzz/goods/')[1]  # url key 与方案关联
        obj["sale_link_all"] = domain+str(goods.xpath('./a[1]/@href')[0])  # 销售网址
        obj["sale_link"] = goods.xpath('./a[1]/@href')[0]  # 销售网址
        response_detail_origin = get(obj['sale_link'])
        try:
            response_detail = response_detail_origin.content.decode()
            detail = etree.HTML(response_detail)
        except:
            print( obj['sale_link'],'orror------------,等待两秒，重新请求')
            time.sleep(2)

            err_link.append(obj['sale_link'])
            # print(xxx)

        obj["default_code"] = detail.xpath('//p[@class="goods_code"]/text()')[0]  # 编码，SKU(必填)
        obj["vr_link"] = detail.xpath('//div[@class="VR_btn"]/a/@href')  # vr 链接
        obj["brand"] = detail.xpath('//span[@class="brand_name fl"]/text()')[0]  # 品牌
        obj["brand_link"] = detail.xpath('//a[@class="brand_link fl"]/@href')[0]  # 品牌系列链接
        obj["name"] = detail.xpath('//div[@class="top_r fr"]/h3/text()')[0]  # 产品名称

        # 2.获取参数 S
        params_div_node_list = detail.xpath('//div[@class="attr_table_box"]/div[@class="table_item"]')  # 参数列表节点,table_div
        obj['params'] = params_list = []
        if len(params_div_node_list):
            for table_div in params_div_node_list:
                params = {}
                params['list'] = list = []
                tr_list = table_div.xpath('./table/tr')

                for index, tr in enumerate(tr_list):
                    # print(index,tr)
                    if index == 0:
                        title = tr.xpath('./th[1]/text()')[0]
                        params['title'] = title
                    else:
                        params_obj = {}
                        params_obj["name"] = tr.xpath('./td[1]/text()')[0]
                        if tr.xpath('./td[2]/a'):
                            if tr.xpath('./td[2]/a/span'):
                                params_obj["value"] = tr.xpath('./td[2]/a/span/text()')[0]
                            else:
                                params_obj["value"] = tr.xpath('./td[2]/a/text()')[0]

                        else:
                            if tr.xpath('./td[2]/text()'):
                                params_obj["value"] = tr.xpath('./td[2]/text()')[0]
                            else:
                                params_obj["value"] = ''
                        list.append(params_obj)

                params_list.append(params)
        # 2.获取参数 E



        # 3.获取对应的产品的规格、型号、颜色、编码、价格
        goods_json = re.findall(r'var goods_list =(.*?);', response_detail)
        goods_json_arr = []
        if len(goods_json):
            try:
                for goods_item in goods_json:
                    goods_json_arr.append(json.loads(goods_item))
            except:
                err_link.append(obj["sale_link"])
        goods_json_str = json.dumps(goods_json_arr, ensure_ascii=False, )
        obj['goods_list'] = json.loads(goods_json_str)

        step_arr.append(obj)

        # col.insert(obj)
        # obj['default_img_list'] = detail.xpath('//li[@class="item responsive"]')  # 获取默认轮播图片

        # print(obj['default_img_list'])
        # style = goods.xpath('./a[1]/img/@data-src')[0]  # 风格

        # material = goods.xpath('./a[1]/img/@data-src')[0]  # 材质
        # color = goods.xpath('./a[1]/img/@data-src')[0]  # 颜色
        # img_src = goods.xpath('./a[1]/@href')[0]  # 轮播图

        # unit = goods.xpath('./a[1]/img/@data-src')[0]  # 单位
        # status_sale = goods.xpath('./a[1]/img/@data-src')[0]  # 销售状态(必填)
        #
        # supplier = goods.xpath('./a[1]/img/@data-src')[0]  # 供应商
        # area = goods.xpath('./a[1]/img/@data-src')[0]  # 区域
        #
        #
        # service = goods.xpath('./a[1]/img/@data-src')[0]  # 服务
        #
        # # goods_class = goods.xpath('./a[1]/img/@data-src')[0]  # 分类
        # detail = goods.xpath('./a[1]/img/@data-src')[0]  # 详情



        # unit_price = goods.xpath('./a[1]/img/@data-src')[0]  # 单价(必填)
        # size = goods.xpath('./a[1]/img/@data-src')[0]  # 规格
        # model = goods.xpath('./a[1]/img/@data-src')[0]  # 型号
        # print(detail_response.content.decode())
    print(index0,'spider:over')


    # 大
    step_arr = json.dumps(step_arr, ensure_ascii=False)
    jsonfile.write(step_arr)
    jsonfile.close()

    index0 = index0+1

