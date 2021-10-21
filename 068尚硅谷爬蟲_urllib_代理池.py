import urllib.request
import random
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "http://baidu.com/s?wd=ip"

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

proxies_pool = [
    {"http" : "88.151.251.195:6969"},
    {"http" : "23.251.138.105:8080"},
    {"http" : "18.139.163.152:443"},
    {"http" : "77.40.252.172:8080"}
]

# 用 random 產生隨機抽選效果
proxies = random.choice(proxies_pool)

handler = urllib.request.ProxyHandler(proxies = proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode("utf-8")

print(content)

# with open("IP_Address.html", mode="w", encoding="utf-8") as fp:
    # fp.write(content)
