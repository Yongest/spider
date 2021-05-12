import scrapy
import json


class DianxianSpider(scrapy.Spider):
    name = 'dianxian'
    allowed_domains = ['demo37.gzdianxian.com']
    start_urls = ['https://demo37.gzdianxian.com/login/index.html#/']

    def parse(self, response):
        # 构造POST请求，传递给引擎
        yield scrapy.FormRequest(
            url= "https://demo37.gzdianxian.com/login/login/user_login",
            formdata={
                "username": "M0005757",
                "password": "VDAiZIxUMl7nPINuyX1uBNFiq+AsbV+Xl6r9D/IIsDQUa3KzClEZBkfIlJn22LoR"
            },
            callback=self.parse_login,

        )

    def parse_login(self, response):
        print(response.text)
        yield scrapy.Request('https://demo37.gzdianxian.com/design//account/getMember', callback=self.check_login)

    def check_login(self,response):
        js =response.text
        print(js)