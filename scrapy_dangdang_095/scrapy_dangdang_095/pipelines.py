# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 如果想使用 pipline 就必須在 settings 中開啟 pipline
class ScrapyDangdang095Pipeline:
    # 企業級開發的兩種方法：
    # 1. open & close spider

    # open_spider 在爬蟲文件開始之前，執行的一種方法
    def open_spider(self, spider):
        print("++++++++")
    
    # close_spider 在爬蟲文件開始之後，執行的一種方法
    def close_spider(self, spider):
        print("--------")
    
    # 在 terminal 運行 scrapy crawl dang 後可以得到一堆數據
    # 並且得到的數據確實是被 ++++++++ 與 -------- 所包圍

    # item 就是 yield 後面的 book 對象
    def process_item(self, item, spider):
        
        # 企業級開發中不推薦 with open 方法，因為每傳遞過來一條文件，就要開啟一次文件，對文件的開關過於頻繁，容易出問題
        
        # 一、write 發法，寫入值必須是字符串
        # 二、write 模式，每次都會打開文件，覆蓋之前內容，所以下載下來的文件只有最後一本書的資料
        # with open('book.json', mode='a', encoding='utf-8')as fp:
        #     fp.write(str(item))

        return item
