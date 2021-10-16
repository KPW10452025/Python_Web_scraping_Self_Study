import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 在 google 搜尋 python 將網址複製後貼上
# https://www.google.com/search?q=python
# 經過觀察可以發現，python 出現在 q= 後面

# 在 google 搜尋 網頁爬蟲 將網址複製後貼上
# https://www.google.com/search?q=%E7%B6%B2%E9%A0%81%E7%88%AC%E8%9F%B2
# 這次搜尋的目標是中文，但是 q= 後面卻是一堆亂碼
# 原因是 %E7%B6%B2%E9%A0%81%E7%88%AC%E8%9F%B2 是一串 Unicode 編碼，表示：網頁爬蟲。

# 需求：獲得【 https://www.google.com/search?q=網頁爬蟲 】的網頁源碼

url = 'https://www.google.com/search?q='

# 請求對象訂製
headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

name = urllib.parse.quote('網頁爬蟲')
url = url + name
print(url)
# https://www.google.com/search?q=%E7%B6%B2%E9%A0%81%E7%88%AC%E8%9F%B2

# request = urllib.request.Request(url = url, headers = headers)

# # 模擬瀏覽器向伺服器發送請求，並獲得響應 response
# response = urllib.request.urlopen(request)

# # 獲得響應 response 的內容 content
# content = response.read().decode('utf-8')

# # 打印內容 content
# print(content)
