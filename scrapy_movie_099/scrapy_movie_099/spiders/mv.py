import scrapy

from scrapy_movie_099.items import ScrapyMovie099Item

class MvSpider(scrapy.Spider):
    name = 'mv'
    # allowed_domains = ['https://www.dydytt.net/html/gndy/dyzz/index.html']
    allowed_domains = ['www.dydytt.net']
    start_urls = ['https://www.dydytt.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        # 要第一頁的名字
        # 要第二頁的圖片

        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a')

        for a in a_list:
            # 獲取第一頁 name 和第二頁 href
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()

            # /html/gndy/dyzz/20211031/61990.html
            # 經觀察獲取的 href 並非常規的 url 所以需要稍微修正
            url = 'https://www.dydytt.net' + href
            
            # 有第二頁地址就需要做訪問
            # 怎麼訪問？用 yield

            # 現在已成功爬取 name 和 src
            # 但是 name 在 def parse 裡面，而 src 在 def parse_second 裡面，兩者是分開的
            # 要怎麼把兩個數據做結合？
            # 運用新功能 Request 裡面的 meta
            # meta 能將數據強轉成 dict
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name':name})
            # 自創一個 parse_second 在下方做定義

    def parse_second(self, response):
        # 注意：如果拿不到數據的情況下，第一個要檢查的就是 xpath 語法是否正確
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        
        # 接收到請求的 meta 參數值
        name = response.meta['name']
        
        movie = ScrapyMovie099Item(src=src, name=name)

        yield movie
