import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "http://www.baidu.com/s?wd=ip"

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.ProxyHandler()

# 觀察一下 ProxyHandler:

# class ProxyHandler(BaseHandler):
#     # Proxies must be in front
#     handler_order = 100
#     def __init__(self, proxies=None):

# 裡面有一個 proxies=None

openr = urllib.request.build_opener(handler)

response = openr.open(request)

content = response.read().decode("utf-8")

# with open("IP_Address.html", mode="w", encoding="utf-8") as fp:
#     fp.write(content)
