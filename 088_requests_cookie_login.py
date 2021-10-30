# 古詩文網
# https://so.gushiwen.cn/user/collect.aspx

# 尋找「登入接口」
# 藉由錯誤密碼做登入，在 Network 找到名為 login.aspx... 的位置

# From Data
# __VIEWSTATE: yeepjl7ZFflIVse6iz3Til11o7Ks05mKYYAg2zMWrUr9iZOAdGlHrIi3ysjpBIDEbLEWaz3LI8gnbg7cXbOO/hTfQAshm36k0PeWbXTqgXWpa7G2YAw/N6Bn2Jc=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: kuopowei@gmail.com
# pwd: powei4gushiwe
# code: 66vw
# denglu: 登录

# 觀察後得知
# __VIEWSTATE, __VIEWSTATEGENERATOR, code 這三個是變量

# 難點
# 一、__VIEWSTATE, __VIEWSTATEGENERATOR
# 二、驗證碼 code

# 一般情況下，看不的數據（__VIEWSTATE, __VIEWSTATEGENERATOR）都是在頁面源碼中
# 藉由觀看網頁原始碼，搜尋 __VIEWSTATE 後發現，__VIEWSTATE, __VIEWSTATEGENERATOR 數據都屬於 type="hidden"
# type="hidden" 隱藏域

import requests

# 登入頁面的 url 地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

# 獲取頁面的源碼
response = requests.get(url=url, headers=headers)
content = response.text
# print(content)
# 對 content 做搜尋以確認無反爬
# 成功搜尋到 __VIEWSTATE 

# 解析頁面源碼，然後獲取 __VIEWSTATE, __VIEWSTATEGENERATOR
from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')

# 獲取 __VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')

# 獲取 __VIEWSTATEGENERATOR
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# 獲取驗證碼圖片
code = soup.select('#imgCode')[0].attrs.get('src')
print(code)
# /RandCode.ashx

