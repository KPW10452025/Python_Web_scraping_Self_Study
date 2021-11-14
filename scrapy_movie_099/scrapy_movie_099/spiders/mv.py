import scrapy


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

            yield scrapy.Request(url=url, callback=self.parse_second)
            # 自創一個 parse_second 在下方做定義

    def parse_second(self, response):
        print('========123456123456========')
        # 實行爬蟲後報錯
        # 因為目前的 allowed_domains = ['https://www.dydytt.net/html/gndy/dyzz/index.html'] 不包含 url = 'https://www.dydytt.net' + href
        # 所以須將 allowed_domains 做修改，將允許網域改大一點：allowed_domains = ['www.dydytt.net']
