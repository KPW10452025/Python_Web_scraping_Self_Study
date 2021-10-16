import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# url 的組成

# 協議          主機              端口號

# http/https    www.google.com   80/443

# 常見端口號
# http      80
# https     443
# MySQL     3306
# oracle    1521
# redis     6379
# mongodb   27017

url = 'https://www.gamer.com.tw/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

print(content)

# 被反爬蟲
# urllib.error.HTTPError: HTTP Error 403: Forbidden
