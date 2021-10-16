import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.gamer.com.tw/'

# 尋找網頁 User Agent
# user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36

headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

request = urllib.request.Request(url = url, headers = headers)
# 藉由 command + 點擊 Request 看其定義。
# class Request:
#     def __init__(self, url, data=None, headers={},
#                  origin_req_host=None, unverifiable=False,
#                  method=None):
# 因為參數順序的問題。
# 不能直接寫 Request(url, headers)
# 這樣系統會將 headers 視為 data=headers 而報錯。
# 故需要明確寫出 Request(url = url, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
# 成功讀取數據
