import urllib.request
import urllib.error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 故意寫錯 url 看會造成什麼樣的報錯
# url = 'https://blog.csdn.net/m0_58649824/article/details/1207793561'

# 這次故意亂寫，隨便創造一個 url
url = 'http://www.thisisnotaurl7777777.com'

headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

try:
    # 請求物件訂製
    request = urllib.request.Request(url=url, headers=headers)

    # 模擬瀏覽器向伺服器發送請求，並獲得響應 response
    response = urllib.request.urlopen(request)

    # 獲得響應 response 的內容 content
    content = response.read().decode('utf-8')

    print(content)
    # 由於故意修改 url 後導致以下異常
    # urllib.error.HTTPError: HTTP Error 404: Not Found
    # 亂寫 url 後導致以下異常
    # urllib.error.URLError

except urllib.error.HTTPError:
    print("系統施工升級中......")

except urllib.error.URLError:
    print("系統維護升級中......")
