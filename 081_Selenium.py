from selenium import webdriver
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

path = '/Users/kuopowei/Developer/Python/尚硅谷爬蟲/chromedriver'

browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'

browser.get(url)

import time
time.sleep(2) # 讓程式停止運作 2 秒

# 獲取「收尋輸入匡」的對象
input = browser.find_element_by_id('kw')

# 在「收尋輸入匡」中輸入「周杰倫」
input.send_keys('周杰倫')

time.sleep(2)

# 獲取「百度一下」的按鈕
button = browser.find_element_by_id('su')

# 點擊「百度一下」的按鈕
button.click()

time.sleep(2)

# 滑動頁面到底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)

time.sleep(2)

# 獲取下一頁的按鈕
next = browser.find_element_by_xpath('//*[@id="page"]/div/a[10]')

# 點擊下一下的按鈕
next.click()

time.sleep(2)

# 回到上一頁
browser.back()

time.sleep(2)

# 去下一頁
browser.forward()

time.sleep(2)

browser.quit()

# browser.close()
