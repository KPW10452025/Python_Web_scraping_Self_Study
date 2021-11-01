import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://bj.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91']
    start_urls = ['https://bj.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91']

    def parse(self, response):
        print('山东荷泽曹县')
