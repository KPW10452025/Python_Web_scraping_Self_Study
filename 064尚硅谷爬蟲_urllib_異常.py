import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://blog.csdn.net/m0_58649824/article/details/120779356'

headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

# 請求物件訂製
request = urllib.request.Request(url=url, headers=headers)

# 模擬瀏覽器向伺服器發送請求，並獲得響應 response
response = urllib.request.urlopen(request)

# 獲得響應 response 的內容 content
content = response.read().decode('utf-8')

print(content)
# 成功獲取數據
