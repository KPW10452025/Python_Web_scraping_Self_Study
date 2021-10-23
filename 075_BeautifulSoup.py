from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 通過解析本地文件，來將 bs4 的基礎語法進行講解。
soup = BeautifulSoup(open('075_BeautifulSoup.html', encoding='utf-8'), 'lxml')

print(soup)
