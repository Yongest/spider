import scrapy
import re

class GithubLoginSpider(scrapy.Spider):
    name = 'github_login'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
        commit = response.xpath("//input[@name='commit']/@value").extract_first()

        # 构造POST请求，传递给引擎
        yield scrapy.FormRequest(
            "https://github.com/session",
            formdata={
                "authenticity_token": authenticity_token,
                "utf8": utf8,
                "commit": commit,
                "login": "yongest",
                "password": ""
            },
            callback=self.parse_login
        )

    def parse_login(self, response):
        # ret = re.findall(r"noobpythoner|NoobPythoner", response.text)
        print(response.text)
