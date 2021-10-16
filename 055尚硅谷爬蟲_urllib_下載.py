import urllib.request

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 下載網頁
url_page = 'https://www.google.com/'
urllib.request.urlretrieve(url_page, 'google.html')
# 運行後，資料夾會多出一個名為 google.html 的文件
