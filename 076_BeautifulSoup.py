from bs4 import BeautifulSoup
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 爬取星巴克菜單 https://www.starbucks.com.cn/menu/

url = 'https://www.starbucks.com.cn/menu/'

# 先測試，不使用請求物件訂製情況下，能不能直接爬取

response = urllib.request.urlopen(url)

content = response.read().decode("utf-8")

# print(content)
# 能取得數據
# 此網頁並沒有設置反爬蟲

# 步驟：
# 一、先觀察網頁源碼，發現爬取目標後分析其 html 標籤
# 二、運用 chrome 的 Xpath Helper 獲得 xpath 語法
# 三、再把 xpath 語法轉換為 bs4

# 【 運用 chrome 的 Xpath Helper 獲得 xpath 語法 】
# //ul[@class="grid padded-3 product"]//strong/text()

# 【 再把 xpath 語法轉換為 bs4 】: //ul[@class="grid padded-3 product"]//strong/text()
soup = BeautifulSoup(content, 'lxml')
name_list = soup.select('ul[class="grid padded-3 product"]')
print(name_list) # 能獲取數值
