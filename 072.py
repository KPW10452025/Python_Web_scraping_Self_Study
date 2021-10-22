from os import stat_result
import urllib.request
from lxml import etree
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 請求物件訂製
# 獲取網頁源碼
# 下載
# 需求：下載前十頁的圖片

# Request URL: https://sc.chinaz.com/tupian/qinglvtupian.html
# Request URL: https://sc.chinaz.com/tupian/qinglvtupian_2.html
# Request URL: https://sc.chinaz.com/tupian/qinglvtupian_3.html

def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'
    print(url)

if __name__ == "__main__":
    start_page = int(input("請輸入起始頁碼："))
    end_page = int(input("請輸入結束頁碼："))

    for page in range(start_page, end_page + 1):
        create_request(page)
