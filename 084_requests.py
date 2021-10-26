# pip install requests

import requests

url = 'http://ww.baidu.com'

response = requests.get(url=url)

# 一個類型、六個屬性

# 類型：Response 類型
print(type(response))
# <class 'requests.models.Response'>


