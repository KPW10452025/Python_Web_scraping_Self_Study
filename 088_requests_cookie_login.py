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
code_url = 'https://so.gushiwen.cn' + code
# print(code_url)
# https://so.gushiwen.cn/RandCode.ashx
# 將以上 url 放到瀏覽器中查詢，發現可以得到驗證碼的圖片，並且可以不斷刷新，獲得新的驗證碼圖片

# requests 裡面有一個方法 session()
# 通過 session() 的返回值，就能使用請求變成一個對象

session = requests.session()
# 驗證碼 url 的內容
response_code = session.get(code_url)
# 注意此時要用二進制數據，因為我們要使用的是圖片的下載
content_code = response_code.content
# wb 模式就是將二進制數據寫入到文件
with open('code.jpg', 'wb')as fp:
    fp.write(content_code)

# 獲取驗證碼圖片後，下載到本地，然後觀察驗證碼，
# 在控制台輸入驗證碼，就可將值傳給 code 參數後，做登入動作
code_name = input('請輸入驗證碼')

# 點擊登入
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': 'kuopowei@gmail.com',
    'pwd': 'powei4gushiwen',
    'code': code_name,
    'denglu': '登录'
}

response_post = session.post(url=url, headers=headers, data=data_post)

content_post = response_post.text

with open('gushiwen.html', 'w', encoding='utf-8')as fp:
    fp.write(content_post)

