# 一、獲取網頁源碼
# 二、解析源碼 etree.HTML
# 三、pinrt()

import urllib.request
from lxml import etree
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "http://www.baidu.com"

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

# 解析服務器的問件
tree = etree.HTML(content)

# 獲取想要的文件
# tree.xpath() 括號中的路徑，可以配合 chrome 瀏覽器的插件 Xpath helper 尋找
result = tree.xpath('//input[@id="su"]/@value')

# xpath 的返回值是一個列表類型的數據
print(result)
# ['百度一下']

result = tree.xpath('//input[@id="su"]/@value')[0]
print(result)
# 百度一下
