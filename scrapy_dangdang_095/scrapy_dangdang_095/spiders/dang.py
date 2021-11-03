import scrapy


class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']

    def parse(self, response):
        print("******************************")
        print("******************************")
        print("******************************")
