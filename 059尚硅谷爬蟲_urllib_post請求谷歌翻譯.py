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

# 尋找參數 From Data
data = {
    'kw' : 'playground'
}

# post 請求的參數，必須要進行編碼
data = urllib.parse.urlencode(data).encode('utf-8')
# print(data)
# b'kw=playground'

# 如何將 Data 放入 request 中？
# 經過觀察 Request() 可以發現：

# class Request:
#     def __init__(self, url, data=None, headers={},
#                  origin_req_host=None, unverifiable=False,
#                  method=None):

# Request 中有 data=None，故可以將 data 放入其中做測試。
request = urllib.request.Request(url = url, data = data, headers = headers)

# 小結論：post 的請求參數不會拼接在 url 後面，而是需要放在請求對象訂製的參數中。

# 模擬瀏覽器向伺服器發送請求，並獲得響應 response
response = urllib.request.urlopen(request)

# 獲得響應 response 的內容 content
content = response.read().decode('utf-8')

# 打印內容 content
print(content)
# {"errno":0,"data":[{"k":"playground","v":"n. \u6e38\u4e50\u573a; \u64cd\u573a\uff0c\u5c24\u6307\u63d0\u4f9b\u5982\u79cb\u5343\u7b49\u8bbe\u5907\u7684\u6237\u5916\u573a\u5730; \uff08\u67d0\u4e9b\u96c6\u4f53\u805a\u4f1a\u6e38\u4e50\u7684\uff09\u56ed\u5730"},{"k":"Playground","v":"[\u7535\u5f71]\u7edd\u5bf9\u7684\u4e54\u4e39"},{"k":"playgrounds","v":"n. \u6e38\u4e50\u573a; \u64cd\u573a( playground\u7684\u540d\u8bcd\u590d\u6570 ); \u5a31\u4e50\u573a; \uff08\u67d0\u4e9b\u96c6\u4f53\u805a\u4f1a\u6e38\u4e50\u7684\uff09\u56ed\u5730"}]}

# 小結論
# post 請求參數的方式，必須編碼：data = urllib.parse.urlencode(data)
# 編碼之後，須調用 encode 方法：data = urllib.parse.urlencode(data).encode('utf-8')
# 參數是放在請求對象制定的方法中：request = urllib.request.Request(url = url, data = data, headers = headers)
