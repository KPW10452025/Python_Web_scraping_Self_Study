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
        self.fp = open('book.json', 'w', encoding='utf-8')
        # 這裡不使用 a 使用 w 的原因為，因為並非使用 with open 所以文件不會自動關閉
    
    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item
    
    # close_spider 在爬蟲文件開始之後，執行的一種方法
    def close_spider(self, spider):
        self.fp.close()
    
    # 在 terminal 運行 scrapy crawl dang 後可以得到檔案 book.json
    # 檢查數據沒問題，爬蟲成功
    # 小結論：這個方法能有效避免文件被多次開啟關閉

import urllib.request

# 多條管道同時開啟

# 一、定義管道類
# 二、在 settings 中開啟管道

# 新增一個名為 DangDangDownload 的 pipline
class DangDangDownloadPipline:
    # 以下為默認寫法
    def process_item(self, item, spider):

        url = item.get('src')

        filename = './books' + item.get('name') + '.jpg'

        urllib.request.urlretrieve(url=url, filename=filename)

        return item
