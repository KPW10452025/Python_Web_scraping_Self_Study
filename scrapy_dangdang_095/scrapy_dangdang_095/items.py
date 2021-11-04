# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDangdang095Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 通俗的說，就是要下載的數據有什麼
    
    # 圖片
    src = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 價格
    price = scrapy.Field()
