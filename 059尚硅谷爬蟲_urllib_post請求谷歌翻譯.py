import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 獲取 百度翻譯 playground 的網頁源碼
