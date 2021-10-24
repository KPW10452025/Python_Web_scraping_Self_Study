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
# 使用 .find_element_by_id() 根據 id 來找到物件
button1 = browser.find_element_by_id('su')
# print(button1)
# <selenium.webdriver.remote.webelement.WebElement (session="943c3a752fc597456f45ae47d0f8295e", element="e1c9ccb4-91c8-4720-8674-b0c5093cf623")>
# 出現類似此數據代表有找到物件

# 檢查瀏覽器原始碼，找到「文字輸入欄位」位置的 name
# 使用 .find_element_by_name() 根據 name 來找到物件
button2 = browser.find_element_by_name('wd')
# print(button2)
# <selenium.webdriver.remote.webelement.WebElement (session="59febc09bd0a108575fbe59c6028d59f", element="cd95faaf-1f20-43e5-9d3e-b79fe832933f")>
# 出現類似此數據代表有找到物件

# 檢查瀏覽器原始碼，找到「百度一下」
# 經觀察，標籤為 input 屬性 id="su"
# 根據 xpath 語句獲取對象
# element 與 elements 使用條件稍有差異
button3_test1 = browser.find_element_by_xpath('//input[@id="su"]')
# print(button3_test1)
# <selenium.webdriver.remote.webelement.WebElement (session="da9a964f8c3263e40a97fc20e1c9e982", element="297bab08-924c-4542-9dbc-088f07dcb48b")>
button3_test2 = browser.find_elements_by_xpath('//input[@id="su"]')
# print(button3_test2)
# [<selenium.webdriver.remote.webelement.WebElement (session="da9a964f8c3263e40a97fc20e1c9e982", element="297bab08-924c-4542-9dbc-088f07dcb48b")>]

# 根據標籤的名字獲取對象
button4_test1 = browser.find_element_by_tag_name('input')
# print(button4_test1)
# 返回第一個
button4_test2 = browser.find_elements_by_tag_name('input')
# print(button4_test2)
# 返回全部

button5_test1 = browser.find_element_by_css_selector('#su')
print(button5_test1)
# <selenium.webdriver.remote.webelement.WebElement (session="d766f1bf6d10ada5293a6abb52c8e006", element="6cc5d14e-217b-4de7-b68d-1ebaa8580975")>
button5_test2 = browser.find_elements_by_css_selector('#su')
print(button5_test2)
# [<selenium.webdriver.remote.webelement.WebElement (session="d766f1bf6d10ada5293a6abb52c8e006", element="6cc5d14e-217b-4de7-b68d-1ebaa8580975")>]


browser.close()
