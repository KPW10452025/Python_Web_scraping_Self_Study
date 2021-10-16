import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# urlencode 應用場景：多個參數的時候。

# 上個教學 [get請求的quote方法] 中，網址中只有一個參數。
# 但實際上的網址為：
# https://www.google.com/search?q=網頁爬蟲&rlz=1C5CHFA_enJP930JP930&oq=網頁爬蟲&aqs=chrome..69i57j0i512l8.1235j0j7&sourceid=chrome&ie=UTF-8
# 除了 q= 之外，還有 oq=, rlz=, aqs=, sourceid=, ie=...等眾多參數。
# 單純使用 urllib.parse.quote() 會無法面對過於複雜的情況。

# 為方便說明，故簡化網址為：
# https://www.google.com/search?q=網頁爬蟲&country=台灣
# https://www.google.com/search?q=%E7%B6%B2%E9%A0%81%E7%88%AC%E8%9F%B2&country=%E5%8F%B0%E7%81%A3
