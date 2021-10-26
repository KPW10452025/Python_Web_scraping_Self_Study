# pip install requests

import requests

url = 'http://ww.baidu.com'

response = requests.get(url=url)

# 一個類型、六個屬性

# 類型：Response 類型
# print(type(response))
# <class 'requests.models.Response'>

# 設置響應的編碼格式
# response.encoding = 'utf-8'

# 以字符串的形式返回了網頁的源碼
# print(response.text)

# 返回二進制數據
# print(response.content)
# .text 和 .content 開頭就差一個 b'

# 返回一個 url 地址
print(response.url)
# http://www.baidu.com/

# 返回響應的狀態碼
print(response.status_code)
# 200

# 返回響應頭
print(response.headers)
# {'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Tue, 26 Oct 2021 12:34:36 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:28:12 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}

# 結論
# 通常使用 response = requests.get(url=url) 
# 再使用 response.text 獲得網頁源碼
# 搭配 xpath 、 bs4 、 jsonpath 分析出想要的數據 
