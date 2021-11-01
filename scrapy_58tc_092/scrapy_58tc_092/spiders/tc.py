import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://bj.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91']
    start_urls = ['https://bj.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91']

    def parse(self, response):
        # 觀察一下 text 的功能
        # content = response.text
        # response.text 獲取的是響應的字符串
        # 觀察一下 body 的功能
        content = response.body
        # response.body 獲取的是二進制數據
        print("================Observation================")
        print(content)
        print("================Observation================")
