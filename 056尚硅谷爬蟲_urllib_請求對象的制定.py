import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.gamer.com.tw/'

# 尋找網頁 User Agent
# user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36

headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

# 藉由 command + 點擊 urlopen 看其定義。
# Open the URL url, which can be either a string or a Request object.
# 因為 urlopen 方法中不能存儲字典，所以 headers 不能傳遞進去。
# 但是 urlopen 方法可以存處 Request

# 故使用「請求對象訂製」：
request = urllib.request.Request(url, headers)

# response = urllib.request.urlopen(url, headers)
response = urllib.request.urlopen(request)
# 把設定好的 request 放入上式，替換掉 url, headers

content = response.read().decode('utf-8')

print(content)
