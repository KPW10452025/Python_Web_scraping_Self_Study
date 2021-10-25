from os import path
from selenium import webdriver
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

path = '/Users/kuopowei/Developer/Python/尚硅谷爬蟲/chromedriver'

browser = webdriver.Chrome(path)

url = 'http://www.baidu.com'

browser.get(url)

# 【 元素定位 】
# 檢查瀏覽器原始碼，找到「百度一下」按鈕的位置的 id
# 使用 .find_element_by_id() 根據 id 來找到物件
input = browser.find_element_by_id('su')

# 使用 .get_attribute('class') 返回查詢 class 的屬性值
print(input.get_attribute('class'))
# bg s_btn

# 使用 .tap_name 返回查詢標籤名稱
print(input.tag_name)
# input

# 使用 .text 返回標籤內容、元素文本
print(input.text) 
# 沒有返回值
# 因為「百度一下」這四個字並非夾在兩個標籤中
# 百度一下是屬性 value 的屬性值
# <input type="submit" id="su" value="百度一下" class="bg s_btn">

# <a href="http://news.baidu.com" target="_blank" class="mnav c-font-normal c-color-t">新闻</a>
a =browser.find_element_by_link_text('新闻')
print(a.text)
# 新闻

browser.close()
