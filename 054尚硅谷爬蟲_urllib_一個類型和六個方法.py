import urllib.request

import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.baidu.com/'

response = urllib.request.urlopen(url)

# 一個類型和六個方法

# 一個類型
print(type(response))
# <class 'http.client.HTTPResponse'>
# response 的類型是 HTTPResponse

# 第一個方法：read()
# read 是按照一個字節一個字節的慢慢去讀
# content = response.read()
# print(content)

# 第一個方法改良：read(數字)
# content = response.read(5)
# print(content)
# b'<!DOC'
# read(5) 裡面的 5 就是指：只讀取五個字節 <!DOC，但此法仍是按照字節返回。

# 第二個方法：readline()
# content = response.readline()
# print(content)
# b'<!DOCTYPE html><!--STATUS OK-->\n')
# 運用 readline() 可以讀取一行，但速度比單純 read() 快很多。

# 第三個方法：readlines()
content = response.readlines()
print(content)
