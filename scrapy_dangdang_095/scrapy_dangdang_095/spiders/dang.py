import scrapy
from scrapy_dangdang_095.items import ScrapyDangdang095Item

# http://category.dangdang.com/cp01.01.02.00.00.00.html

class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']

    def parse(self, response):
        # pipeline 下載數據
        # items 定義數據結構的
        # src = //ul[@id="component_59"]/li//img/@src
        # alt = //ul[@id="component_59"]/li//img/@alt
        # price = //ul[@id="component_59"]/li/p[@class="price"]/span[1]/text()

        # 經過觀察發現 src, alt, price 三個目標數據的在 li 下面

        # 所有 selector 對象，都可以再次調用 xpath 方法
        li_list = response.xpath('//ul[@id="component_59"]/li')
        
        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()

            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('./p[@class="price"]/span[1]/text()').extract_first()
            print(src, name, price)
            # 雖然成功爬取數據
            # 但是發現圖片都一模一樣，圖片有設置反爬蟲
            # 經觀察發現這是網頁的圖片懶加載
            # <img data-original="//img3m3.ddimg.cn/97/36/29289643-1_b_6.jpg" src="images/model/guan/url_none.png"...>
            # 觀察發現，當使用者頁面滑到該圖片時，圖片的的 src 才會從 none.png 轉變成真實的 .jpg
            # <img data-original="//img3m3.ddimg.cn/97/36/29289643-1_b_6.jpg" src="//img3m3.ddimg.cn/97/36/29289643-1_b_6.jpg"...>
            # 再次觀察又發現，真正的 src 其實就是 data-original
            
            # 再次觀察回傳數據
            # 發現一個問題：回傳數據中，第一個 src 是 None
            # 重新觀察網頁源碼發現，第一個 img 標籤中的第一個屬性是 src，並非 data-original
            # <img src="//img3m2.ddimg.cn/71/20/28541672-1_b_6.jpg"...>
            # 而第二個開始的 img 標籤的第一個屬性就是 data-original 並且第二個是 src
            # 也就是說，第一張圖片的 src 可以使用，其他要使用 data-original

            book = ScrapyDangdang095Item(src=src, name=name, price=price)
            