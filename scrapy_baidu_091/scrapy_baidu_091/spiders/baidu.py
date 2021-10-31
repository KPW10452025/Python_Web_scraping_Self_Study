import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬蟲的名稱，用於運行爬蟲的時候，使用的值
    name = 'baidu'

    # 允許訪問的域名
    allowed_domains = ['http://www.baidu.com']

    # 起始的 url 地址，指的是第一次訪問的域名
    # start_urls 是在 allowed_domains 的前面添加一個 http:// 並在後面添加一個 /

    # start_urls = ['http://http://www.baidu.com/'] 
    # 因為創建爬蟲文件時，輸入了 scrapy genspider baidu http://www.baidu.com
    # 導致雙重 http:// 問題
    # 正確輸入方法為 scrapy genspider baidu www.baidu.com
    
    start_urls = ['http://http://www.baidu.com/']

    def parse(self, response):
        pass
