import requests

# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://www.baidu.com/s?'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

data = {
    'wd' : 'ip'
}

proxy = {
    'http://' : '211.65.197.93:80'
}

response = requests.get(url=url,params=data,headers=headers,proxies=proxy)
# response = requests.get(url=url,params=data,headers=headers)

content = response.text

with open('daili.html', mode='w', encoding='utf-8') as fp:
    fp.write(content)

# 搜尋關鍵字「本机IP」
