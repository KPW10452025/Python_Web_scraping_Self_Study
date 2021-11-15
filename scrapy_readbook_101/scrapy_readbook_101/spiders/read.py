import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1188.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1188_\d+\.html'), 
                            callback='parse_item', 
                            follow=False),
    )

    def parse_item(self, response):
        # 因為可以運用 items.py 進行設定，所以以下皆可以刪除
        return item
