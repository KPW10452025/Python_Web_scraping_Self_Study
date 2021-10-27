import requests

url = 'https://www.baidu.com/s?'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

data = {
    'wd' : 'ip'
}

response = requests.get(url=url,params=data,headers=headers)

content = response.text

with open('daili.html', mode='w', encoding='utf-8') as fp:
    fp.write(content)
