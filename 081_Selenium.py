from os import path
from selenium import webdriver
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

path = '/Users/kuopowei/Developer/Python/尚硅谷爬蟲/chromedriver'

browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'

browser.get(url)

browser.close()
