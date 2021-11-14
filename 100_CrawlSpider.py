# CrawlSpider

# 1. 繼承自 scrapy.Spider
# 2. 獨門祕技：CrawlSpider 可以定義規則，解析 html 內容的時候，可以根據鏈接規則提取出指定的鏈接，然後再向這些鏈接發送請求
#    所以，如果有需要跟進鏈接的需求，意思就是爬取了網頁之後，需要提取鏈接再次爬取，使用 CrawlSpider 是非常合適的

# 解說網站：讀書網 - 當代小說 https://www.dushu.com/book/1188.html
# 底下頁面共有幾頁？

# 鏈接提取器：在這裡就可以寫規則提取指定鏈接
# scrapy.linkextractors.LinkExtractor(
#     allow = (),          # 正則表達式，提取符合正則的鏈接
#     deny = (),           # （不常使用）正則表達式，不提取符合正則的鏈接
#     allow_domains = (),  # （不常使用）允許的域名
#     deny_domains = (),   # （不常使用）不允許的域名
#     restrict_xpath = (), # xpath，提取符合 xpath 規則的鏈接
#     restrict_css = ()    # css，提取符合 css 規則的鏈接
# )

# 模擬使用
# 正則用法：link = LinkExtractor(allow=r'list_23_\d+\.html')
# xpath 用法：link = LinkExtractor(restrict_xpaths=r'//div[@class="x"]')
# css 用法：link = LinkExtractor(restrict_css='.x')

# 鏈接提取
# link.extract_links(response)

# 在 terminal 開啟 scrapy shell
# 輸入 scrapy shell https://www.dushu.com/book/1188.html

# 載入 LinkExtractor
# >>> from scrapy.linkextractors import LinkExtractor

# 使用正則表達式建立規則，提取鏈接
# >>> link = LinkExtractor(allow=r'/book/1188_\d+\.html')

# >>> link
# <scrapy.linkextractors.lxmlhtml.LxmlLinkExtractor object at 0x7fa67059cdc0>

# >>> link.extract_links(response)
# [Link(url='https://www.dushu.com/book/1188_2.html', text='2', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_3.html', text='3', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_4.html', text='4', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_5.html', text='5', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_6.html', text='6', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_7.html', text='7', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_8.html', text='8', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_9.html', text='9', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_10.html', text='10', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_11.html', text='11', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_12.html', text='12', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_13.html', text='13', fragment='', nofollow=False)]

# >>> for link in link.extract_links(response):
# ...     print(link)
# ... 
# Link(url='https://www.dushu.com/book/1188_2.html', text='2', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_3.html', text='3', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_4.html', text='4', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_5.html', text='5', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_6.html', text='6', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_7.html', text='7', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_8.html', text='8', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_9.html', text='9', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_10.html', text='10', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_11.html', text='11', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_12.html', text='12', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_13.html', text='13', fragment='', nofollow=False)

# 使用正則的 xpath 建立規則，提取鏈接
# >>> link1=LinkExtractor(restrict_xpaths=r'//div[@class="pages"]/a/@href')

# 這個寫法會報錯 AttributeError: 'str' object has no attribute 'iter'
# The problem is that restrict_xpaths should point to elements - either the links directly or containers containing links, not attributes:
# 這個錯誤的原因是 restrict_xpaths 應該指向元素，也就是直接鏈接或包含鏈接的容器，而不是它的屬性，而我們的代碼中用的是 a/@href，修改如下

# >>> link1=LinkExtractor(restrict_xpaths=r'//div[@class="pages"]/a')
# >>> link1.extract_links(response)
# [Link(url='https://www.dushu.com/book/1188_2.html', text='2', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_3.html', text='3', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_4.html', text='4', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_5.html', text='5', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_6.html', text='6', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_7.html', text='7', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_8.html', text='8', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_9.html', text='9', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_10.html', text='10', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_11.html', text='11', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_12.html', text='12', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_13.html', text='13', fragment='', nofollow=False), Link(url='https://www.dushu.com/book/1188_2.html', text='下一页»', fragment='', nofollow=False)]

# >>> for link in link1.extract_links(response):
# ...     print(link)
# ... 
# Link(url='https://www.dushu.com/book/1188_2.html', text='2', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_3.html', text='3', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_4.html', text='4', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_5.html', text='5', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_6.html', text='6', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_7.html', text='7', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_8.html', text='8', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_9.html', text='9', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_10.html', text='10', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_11.html', text='11', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_12.html', text='12', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_13.html', text='13', fragment='', nofollow=False)
# Link(url='https://www.dushu.com/book/1188_2.html', text='下一页»', fragment='', nofollow=False)
