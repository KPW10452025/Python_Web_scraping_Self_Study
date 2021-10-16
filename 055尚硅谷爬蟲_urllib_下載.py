import urllib.request

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 下載網頁
# url_page = 'https://www.google.com/'
# urllib.request.urlretrieve(url_page, 'google.html')
# 運行後，資料夾會多出一個名為 google.html 的 html 網頁檔。

# 下載圖片
# url_img = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/480px-Python-logo-notext.svg.png'
# urllib.request.urlretrieve(url = url_img, filename = 'python.png')
# 運行後，資料夾會多出一個名為 python.png 的 png 圖片檔。

# 下載影片
# 影片來源：https://haokan.baidu.com/v?vid=8411018916249725548&pd=pcshare
# 播放影片後馬上點停，點停後右鍵開啟檢查，用滑鼠點選功能選取影片視窗，以獲得 scr 後面的網址如下
url_video = 'https://vd4.bdstatic.com/mda-mik0wqb6qu8j1ebf/sc/cae_h264_clips/1632185126189105922/mda-mik0wqb6qu8j1ebf.mp4?auth_key=1634367421-0-0-c6e2f5958c14213328251effe14be82e&bcevod_channel=searchbox_feed&pd=1&pt=3&abtest='
urllib.request.urlretrieve(url = url_video, filename = 'Python設計理念是什麼.mp4')
# 運行後，資料夾會多出一個名為 Python設計理念是什麼.mp4 的 mp4 影片檔。
