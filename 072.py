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
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    }
    request = urllib.request.Request(url=url, headers= headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    print(content)

if __name__ == "__main__":
    start_page = int(input("請輸入起始頁碼："))
    end_page = int(input("請輸入結束頁碼："))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        get_content(request)