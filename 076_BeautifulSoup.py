from bs4 import BeautifulSoup
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 爬取星巴克菜單 https://www.starbucks.com.cn/menu/

url = 'https://www.starbucks.com.cn/menu/'

# 先測試，不使用請求物件訂製情況下，能不能直接爬取

response = urllib.request.urlopen(url)

content = response.read().decode("utf-8")

print(content)
# 能取得數據
# 此網頁並沒有設置反爬蟲
