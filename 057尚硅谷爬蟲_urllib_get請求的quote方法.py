import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 在 google 搜尋 python 將網址複製後貼上
# https://www.google.com/search?q=python
# 經過觀察可以發現，python 出現在 q= 後面

# 在 google 搜尋 網頁爬蟲 將網址複製後貼上
# https://www.google.com/search?q=%E7%B6%B2%E9%A0%81%E7%88%AC%E8%9F%B2
# 這次搜尋的目標是中文，但是 q= 後面卻是一堆亂碼
# 原因是 %E7%B6%B2%E9%A0%81%E7%88%AC%E8%9F%B2 是一串 Unicode 編碼，表示：網頁爬蟲。
