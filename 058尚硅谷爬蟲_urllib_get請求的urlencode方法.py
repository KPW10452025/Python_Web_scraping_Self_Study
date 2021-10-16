import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# urlencode 應用場景：多個參數的時候。

# 上個教學 [get請求的quote方法] 中，網址中只有一個參數。
# 但實際上的網址為：
# https://www.google.com/search?q=網頁爬蟲&rlz=1C5CHFA_enJP930JP930&oq=網頁爬蟲&aqs=chrome..69i57j0i512l8.1235j0j7&sourceid=chrome&ie=UTF-8
# 除了 q= 之外，還有 oq=, rlz=, aqs=, sourceid=, ie=...等眾多參數。
# 單純使用 urllib.parse.quote() 會無法面對過於複雜的情況。

# 為方便說明，故簡化網址為：
# https://www.google.com/search?q=網頁爬蟲&country=台灣
# https://www.google.com/search?q=%E7%B6%B2%E9%A0%81%E7%88%AC%E8%9F%B2&country=%E5%8F%B0%E7%81%A3

# data = {
#     'q' : '網頁爬蟲', 
#     'country' : '台灣'
# }

# # 測試 urllib.parse.urlencode() 效果
# a = urllib.parse.urlencode(data)
# print(a)
# # q=%E7%B6%B2%E9%A0%81%E7%88%AC%E8%9F%B2&country=%E5%8F%B0%E7%81%A3
# # 經測試發現 urlencode 不僅可以將 dics 裡面的中文轉換成 Unicode 還能將英文的逗號 , 轉換成 &、冒號 : 轉換成 = 

# 獲取 [https://www.google.com/search?q=網頁爬蟲&country=台灣] 的網頁源碼

# 基礎路徑
base_url = 'https://www.google.com/search?'

# 基礎參數
data = {
    'q' : '網頁爬蟲', 
    'country' : '台灣'
}

# 將參數轉換為 Unicode
new_data = urllib.parse.urlencode(data)

# 請求資源路徑
url = base_url + new_data
# print(url)
# https://www.google.com/search?q=%E7%B6%B2%E9%A0%81%E7%88%AC%E8%9F%B2&country=%E5%8F%B0%E7%81%A3

# 請求對象訂製
headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

request = urllib.request.Request(url = url, headers = headers)

# 模擬瀏覽器向伺服器發送請求，並獲得響應 response
response = urllib.request.urlopen(request)

# 獲得響應 response 的內容 content
content = response.read().decode('utf-8')

# 打印內容 content
print(content)
