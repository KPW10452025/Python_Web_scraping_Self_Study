import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-15.html']
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html/']

    def parse(self, response):
        print("***************this is for testing***************")
