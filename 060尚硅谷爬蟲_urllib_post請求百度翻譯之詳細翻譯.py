import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

data = {
    'from' : 'en',
    'to' : 'zh',
    'query': 'love',
    'transtype' : 'realtime',
    'simple_means_flag' : '3',
    'sign' : '198772.518981',
    'token' : 'f956b124540d1acf9353d721879c2974',
    'domain' : 'common',
}

# post 請求的參數必須進行編碼，並且要調用 encode 方法
data = urllib.parse.urlencode(data).encode('utf-8')

# 請求物件的訂製 Constructing a request object.
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模擬瀏覽器向伺服器發送請求，並獲得響應 response
response = urllib.request.urlopen(request)

# 獲得響應 response 的內容 content
content = response.read().encode('utf-8')

# 打印內容 content
print(content)
# AttributeError: 'bytes' object has no attribute 'encode'
