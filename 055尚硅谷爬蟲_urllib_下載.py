import urllib.request

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 下載網頁
# url_page = 'https://www.google.com/'
# urllib.request.urlretrieve(url_page, 'google.html')
# 運行後，資料夾會多出一個名為 google.html 的 html 網頁檔。

# 下載圖片
url_img = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/480px-Python-logo-notext.svg.png'
urllib.request.urlretrieve(url = url_img, filename = 'python.png')
# 運行後，資料夾會多出一個名為 python.png 的 png 圖片檔。
