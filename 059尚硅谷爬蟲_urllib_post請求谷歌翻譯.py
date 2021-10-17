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
