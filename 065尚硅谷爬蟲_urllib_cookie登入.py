# 適用場景，在數據採集的時候需要繞過登入。

# 常見反爬蟲手段之一
# 需登入後才有訪問權的頁面雖然是 utf-8 編碼，但是登入頁面卻不是 utf-8

import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://ecvip.pchome.com.tw/web/order/all'

headers = {
    # cookie 中攜帶著個人登入訊息，如果有登入之後 cookie，那我們就可以帶著 cookid 進入各個頁面
    "cookie": "_gcl_au=1.1.849564370.1631752926; venguid=e918ff76-b85d-4d49-a07d-70c0365cc1a3.wgc-7l7c20210916; U=8bdef3b2872697c56d8dc3b5fdb3b7c26a62d69e; fpc=e07d13737483fda32228f7d349844647-_KU6WTU6BHOYBR; aqM=Y; _pafp=6534e5c9e121504aecdf731dcfcd5ca1; _pafp_t=1633005949; uuid=xxx-f67b0a66-edda-45d0-a354-1e0c409833cf; puuid=P.20210930204550.0; _ga_QB624SM9W2=GS1.1.1633005940.1.0.1633006102.0; recomdId=rg1-hh06_pc_p_coocpn_LastCS8_mbe_cap_tp_1633034912_1349954514; ECC=6f0fa21695a38017ba8041aaca1ebc3c33be0e9f.1633006164; _gcl_aw=GCL.1634105498.Cj0KCQjw5JSLBhCxARIsAHgO2SeIJ9vEWooImiAWwWT4YzgDxh08nCilK0JvbS1sfOaPXrwDZMLSBK8aAqqOEALw_wcB; _gac_UA-115564493-1=1.1634105500.Cj0KCQjw5JSLBhCxARIsAHgO2SeIJ9vEWooImiAWwWT4YzgDxh08nCilK0JvbS1sfOaPXrwDZMLSBK8aAqqOEALw_wcB; HistoryEC=%7B%22P%22%3A%5B%7B%22Id%22%3A%22DRAA5K-A900BO6K9%22%2C%20%22M%22%3A1634105575%7D%2C%20%7B%22Id%22%3A%22DRAA6H-A900AI3OM%22%2C%20%22M%22%3A1634105546%7D%2C%20%7B%22Id%22%3A%22DSABKO-A900A4G3D%22%2C%20%22M%22%3A1634105498%7D%2C%20%7B%22Id%22%3A%22DGBN51-A900AWRPD%22%2C%20%22M%22%3A1634105448%7D%2C%20%7B%22Id%22%3A%22DSBE02-A900BE94X%22%2C%20%22M%22%3A1633948865%7D%2C%20%7B%22Id%22%3A%22DRAA5C-A900BSTNE%22%2C%20%22M%22%3A1633576277%7D%2C%20%7B%22Id%22%3A%22DYAP59-A900BEYDK%22%2C%20%22M%22%3A1633005902%7D%2C%20%7B%22Id%22%3A%22DPAE1X-A900BBDLS%22%2C%20%22M%22%3A1633004687%7D%5D%2C%20%22T%22%3A1%7D; gsite=shopping; vensession=65a28d52-9af5-4309-b785-2ab245ee21cb.wgc-1w1g20211020.se; _gid=GA1.3.1801915437.1634711331; PCHOMEUNIQID=e59bdfed2770526bd2d54f971202b659; ECWEBSESS=3a05e62d6a.da52c873bbd40cab10125494b595f5b211924bc7.1634711418; CID=31b18c9ecb5bd254369bb452a5188a6c160e6e89; MBR=kuopowei%40gmail.com; X=12112829; E=zRHrOYjNV72DcEKG9ysZXv02CZCJy%2FLymjh9dIrKt%2BxVZnbvZAGcbj1XDz0Whjzx6gqryRwbo2OUEmzBm06cc4afkkEgNWHS; _ga=GA1.3.1281972745.1631752926; _ga_9CE1X6J1FG=GS1.1.1634711330.9.1.1634711474.4",
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    # referer：判斷當前物鏡是不是由 referer 表示的路徑而來，很多網站會把 referer 當作圖片防盜鏈
    "referer": "https://ecvip.pchome.com.tw/login/v3/login.htm?rurl=https%3A%2F%2Fecvip.pchome.com.tw%2Fweb%2Forder%2Fall",
}

request = urllib.request.Request(url = url, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)

with open("typing_web.html", mode = "w", encoding="utf-8") as fp:
    fp.write(content)

# 小結論
# 通常 headers 中弄好 user-agent, cookie, referer 就能搞定八成左右的網站
