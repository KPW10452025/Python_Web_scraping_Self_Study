import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 獲取 百度翻譯 playground 的網頁源碼

# 尋找請求網址 Request URL
# 須在 Network 中慢慢觀察並尋找
url = 'https://fanyi.baidu.com/sug'
