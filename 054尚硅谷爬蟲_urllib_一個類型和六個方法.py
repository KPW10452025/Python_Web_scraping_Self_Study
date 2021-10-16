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
# content = response.readlines()
# print(content)
# 比起 readline() 只能讀取一行代碼，readlines() 能讀取所有代碼。
# 讀取速度也比 read() 快許多。

# 第四個方法：getcode()
# 返回「狀態碼」。
# print(response.getcode())
# 200
# 返回 200 只的是網路順暢無錯誤。

# 第五個方法：geturl()
# print(response.geturl())
# https://www.baidu.com/
# 返回「網址」

# 第六個方法：getheaders()
print(response.getheaders())
# [('Bdpagetype', '1'), ('Bdqid', '0x8bcc24b70000041c'), ('Cache-Control', 'private'), ('Content-Type', 'text/html;charset=utf-8'), ('Date', 'Sat, 16 Oct 2021 04:45:28 GMT'), ('Expires', 'Sat, 16 Oct 2021 04:45:28 GMT'), ('P3p', 'CP=" OTI DSP COR IVA OUR IND COM "'), ('P3p', 'CP=" OTI DSP COR IVA OUR IND COM "'), ('Server', 'BWS/1.1'), ('Set-Cookie', 'BAIDUID=785ED912AB14622AD33E640EE0D87133:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com'), ('Set-Cookie', 'BIDUPSID=785ED912AB14622AD33E640EE0D87133; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com'), ('Set-Cookie', 'PSTM=1634359528; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com'), ('Set-Cookie', 'BAIDUID=785ED912AB14622A26963A0F829F8297:FG=1; max-age=31536000; expires=Sun, 16-Oct-22 04:45:28 GMT; domain=.baidu.com; path=/; version=1; comment=bd'), ('Set-Cookie', 'BDSVRTM=8; path=/'), ('Set-Cookie', 'BD_HOME=1; path=/'), ('Set-Cookie', 'H_PS_PSSID=34067_31253_34711_34525_34584_34518_34832_34806_34578_26350_34424_34473_34691_34673; path=/; domain=.baidu.com'), ('Strict-Transport-Security', 'max-age=172800'), ('Traceid', '1634359528059018317810073466834918573084'), ('Vary', 'Accept-Encoding'), ('Vary', 'Accept-Encoding'), ('X-Frame-Options', 'sameorigin'), ('X-Ua-Compatible', 'IE=Edge,chrome=1'), ('Connection', 'close'), ('Transfer-Encoding', 'chunked')]
# 獲取一些狀態訊息

# 一個類型 HTTPresponse
# 六個方法 read() readline() readlines() getcode() geturl() getheaders()
