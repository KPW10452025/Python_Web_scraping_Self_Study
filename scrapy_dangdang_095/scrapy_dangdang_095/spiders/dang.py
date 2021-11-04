import scrapy

# http://category.dangdang.com/cp01.01.02.00.00.00.html

class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']

    def parse(self, response):
        # pipeline 下載數據
        # items 定義數據結構的
        # src = //ul[@id="component_59"]/li/a/img/@src
        # alt = //ul[@id="component_59"]/li/a/img/@alt
        # price = //ul[@id="component_59"]/li/p[@class="price"]/span[1]/text()

        # 經過觀察發現 src, alt, price 三個目標數據的在 li 下面

        # 所有 selector 對象，都可以再次調用 xpath 方法
        li_list = response.xpath('//ul[@id="component_59"]/li')
        
        for li in li_list:
            print(li)
