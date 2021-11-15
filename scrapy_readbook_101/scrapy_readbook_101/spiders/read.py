import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_readbook_101.items import ScrapyReadbook101Item


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1188_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1188_\d+\.html'), 
                            callback='parse_item', 
                            follow=False),
    )

    def parse_item(self, response):
        
        # 藉由網頁 XPath Helper 得到
        # //div[@class="bookslist"]//img/@alt
        # //div[@class="bookslist"]//img/@src
        img_list = response.xpath('//div[@class="bookslist"]//img')

        for img in img_list:
            # 觀察網頁 html 時，發現有 data-original 懶加載
            name = img.xpath('./@alt').extract_first()
            src = img.xpath('./@data-original').extract_first()

            book = ScrapyReadbook101Item(name=name, src=src)
            yield book
    
# 執行爬蟲後雖成功獲得數據 json 數據
# 但觀察 json 數據時發現，數據數量無法對上
# 故程式碼邏輯上有錯誤
