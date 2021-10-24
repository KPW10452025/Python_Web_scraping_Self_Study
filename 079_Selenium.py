from selenium import webdriver
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 什麼是 selenium 元素定位？
# 元素定位：自動化要做的就是模擬滑鼠和鍵盤來操作這些元素：點擊、輸入...等等
# 操作這些元素前，首先要找到他們
# WebDriver 提供很多元素定位方法，常用有六種

path = '/Users/kuopowei/Developer/Python/尚硅谷爬蟲/chromedriver'

browser = webdriver.Chrome(path)

url = 'https://www.baidu.com/'

browser.get(url)

# 【 元素定位 】
# 檢查瀏覽器原始碼，找到「百度一下」按鈕的位置的 id
button = browser.find_element_by_id('su')
