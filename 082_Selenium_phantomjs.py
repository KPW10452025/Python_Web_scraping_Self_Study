# phantomjs 已經停止更新，目前已被淘汰
# 無介面瀏覽器 phantomjs 基本使用簡介

from selenium import webdriver
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

phantomjs_path = '/Users/kuopowei/Developer/Python/尚硅谷爬蟲/phantomjs'

browser = webdriver.PhantomJS(phantomjs_path)

url = 'https://www.baidu.com'

browser.get(url)

# 頁面截圖
browser.save_screenshot('baidu.png')

import time
time.sleep(2)

input = browser.find_element_by_id('kw')
input.send_keys('昆凌')

time.sleep(2)

browser.save_screenshot('昆凌.png')
