import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-15.html']
    # 當 url 後綴是 html 時，不能加 /
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']

    def parse(self, response):
        print("***************this is for testing***************")
        # ***************this is for testing*************** 爬蟲成功
