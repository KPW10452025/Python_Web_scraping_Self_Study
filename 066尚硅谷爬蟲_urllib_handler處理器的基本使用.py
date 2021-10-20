# 需求：使用 handler 來訪問百度，獲取網頁源碼。

import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.baidu.com"

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

request = urllib.request.Request(url = url, headers = headers)

# handler 處理器的基本使用三步驟：
# handler      build_opener      open

# (1) 獲取 handler 對象
handler = urllib.request.HTTPHandler()

# (2) 獲取 opener 對象
opener = urllib.request.build_opener(handler)

# (3) 調用 open 方法
response = opener.open(request)

content  = response.read().decode("utf-8")

print(content)

# 為什麼要學習 handler 處理器？
    # urllib.request.urlopen(url)
    # 以上方法不能做請求物件訂製
    # urllib.request.Request(url=url, headers=headers, data=data)
    # 以上方法可以請求物件訂製，無法處理動態 cookie、代理...等較複雜請求
    # handler
    # 可以製作更高級的物件訂製，可以處理動態 cookie、代理...等較複雜請求
