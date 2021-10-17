import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 獲取 百度翻譯 playground 的網頁源碼

# 尋找請求網址 Request URL
# 須在 Network 中慢慢觀察並尋找
url = 'https://fanyi.baidu.com/sug'

# 請求對象訂製
headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

# 尋找 From Data
data = {
    'kw' : 'playground'
}

# post 請求的參數，必須要進行編碼
data = urllib.parse.urlencode(data)
# print(data)
# kw=playground 無報錯

# 如何將 Data 放入 request 中？
# 經過觀察 Request() 可以發現：

# class Request:
#     def __init__(self, url, data=None, headers={},
#                  origin_req_host=None, unverifiable=False,
#                  method=None):

# Request 中有 data=None，故可以將 data 放入其中做測試。
request = urllib.request.Request(url = url, data = data, headers = headers)
print(request)
# <urllib.request.Request object at 0x7fca602fbfd0> 無報錯

# 小結論：post 的請求參數不會拼接在 url 後面，而是需要放在請求對象訂製的參數中。
