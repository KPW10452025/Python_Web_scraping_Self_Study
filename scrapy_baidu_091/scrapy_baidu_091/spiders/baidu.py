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

    # 是執行了 start_urls 之後，執行的方法
    # 方法中的 response 就是返回的那個對象
    # 相當於 response = urllib.request.urlopen()
    # 相當於 response = requests.get()
    def parse(self, response):
        print('This is for testing.')

# 在 terminal 輸入 scrapy crawl baidu 後得到一堆數據
# 搜尋 This is for testing. 後，無任何結果
# 得知網站有反爬蟲手段
