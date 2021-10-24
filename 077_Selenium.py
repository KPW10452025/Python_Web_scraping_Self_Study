import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.jd.com/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

print(content)

# 雖然有獲得 content 但是在瀏覽器複製 class="lc-goods-seckill__left-title"
# 卻無法在 terminal 中找到 lc-goods-seckill__left-title
# 回傳的數據不完整

# 這個網站會檢驗請求方式不是完整的瀏覽器
# 而這只是一個爬蟲程式，而非完整的瀏覽器
# 所以才導致被反爬蟲，數據不完整

# Selenium 可以讓爬蟲程式偽裝成瀏覽器
