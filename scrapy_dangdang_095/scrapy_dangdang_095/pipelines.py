# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 如果想使用 pipline 就必須在 settings 中開啟 pipline
class ScrapyDangdang095Pipeline:
    # item 就是 yield 後面的 book 對象
    def process_item(self, item, spider):
        
        with open('book.json', mode='w', encoding='utf-8')as fp:
            fp.write(item)

        return item
