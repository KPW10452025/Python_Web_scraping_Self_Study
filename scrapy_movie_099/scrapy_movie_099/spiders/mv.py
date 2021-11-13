import scrapy


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['https://www.dydytt.net/html/gndy/dyzz/index.html']
    start_urls = ['https://www.dydytt.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        # 要第一頁的名字
        # 要第二頁的圖片
        pass
